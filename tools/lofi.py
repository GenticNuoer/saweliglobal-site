import numpy as np, soundfile as sf
from scipy.signal import fftconvolve, butter, sosfilt
SR=48000; BPM=76; beat=60/BPM; bar=4*beat; NB=18; L=int(NB*bar*SR)+SR*3
rng=np.random.default_rng(7)
L_=np.zeros(L); R_=np.zeros(L)
def add(sig,t,pan=0.0,g=1.0):
    i=int(t*SR); n=min(len(sig),L-i)
    if n<=0: return
    L_[i:i+n]+=sig[:n]*g*np.sqrt(0.5*(1-pan)); R_[i:i+n]+=sig[:n]*g*np.sqrt(0.5*(1+pan))
def hz(m): return 440*2**((m-69)/12)
def ep(m,dur=2.4,vel=1.0):
    n=int(dur*SR); t=np.arange(n)/SR; f=hz(m)*(1+rng.normal(0,.0008))
    s=np.sin(2*np.pi*f*t)+.28*np.sin(2*np.pi*2*f*t)*np.exp(-t*3)+.08*np.sin(2*np.pi*3*f*t)*np.exp(-t*6)
    env=np.minimum(1,t/0.006)*np.exp(-t*1.25)
    trem=1+.12*np.sin(2*np.pi*4.2*t)
    return s*env*trem*vel*.16
def pad(ms,dur):
    n=int(dur*SR); t=np.arange(n)/SR; s=np.zeros(n)
    for m in ms:
        for d in (-.0025,.0025):
            f=hz(m)*(1+d)
            for h in range(1,7): s+=np.sin(2*np.pi*f*h*t+rng.uniform(0,6))/h**1.6
    env=np.minimum(1,t/1.4)*np.minimum(1,(dur-t)/1.2).clip(0,1)
    sos=butter(2,900,'low',fs=SR,output='sos'); return sosfilt(sos,s*env)*.018
def bass(m,dur):
    n=int(dur*SR); t=np.arange(n)/SR; f=hz(m)
    s=np.sin(2*np.pi*f*t)+.15*np.sin(2*np.pi*2*f*t)
    return s*np.minimum(1,t/.01)*np.exp(-t*1.1)*.30
def kick():
    n=int(.35*SR); t=np.arange(n)/SR; f=45+80*np.exp(-t*28)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*9)*.55
def snare():
    n=int(.25*SR); t=np.arange(n)/SR; s=rng.normal(0,1,n)
    sos=butter(2,[1200,5200],'band',fs=SR,output='sos'); return sosfilt(sos,s)*np.exp(-t*20)*.10
def hat(v=1):
    n=int(.06*SR); t=np.arange(n)/SR; s=rng.normal(0,1,n)
    sos=butter(2,7000,'high',fs=SR,output='sos'); return sosfilt(sos,s)*np.exp(-t*70)*.045*v
def bell(m):
    n=int(2.2*SR); t=np.arange(n)/SR; f=hz(m)
    s=np.sin(2*np.pi*f*t)+.4*np.sin(2*np.pi*f*2.76*t)*np.exp(-t*4)+.2*np.sin(2*np.pi*f*5.4*t)*np.exp(-t*8)
    return s*np.minimum(1,t/.003)*np.exp(-t*2.2)*.07
# Fmaj9 - Em7 - Dm9 - Cmaj7(add9)
CH=[([53,57,60,64,67],41),([52,55,59,62,66-1],40),([50,53,57,60,64],38),([48,52,55,59,62],36)]
mel=[(0,76),(1.5,79),(2.5,77),(4.5,74),(6,72),(8,76),(9.5,81),(10.5,79),(12.5,77),(14,76)]
for b in range(NB):
    t0=b*bar; ch,root=CH[b%4]
    add(pad(ch[:4],bar+1.2),t0,0,1)
    for k,(off,vel) in enumerate([(0,1),(2.5,.7)]):
        for j,m in enumerate(ch):
            add(ep(m,2.6,vel*(1-.07*j)),t0+off*beat+j*0.012,pan=(j-2)*.18)
    if b>=1:
        add(bass(root,beat*2),t0,0,1); add(bass(root+7 if b%2 else root,beat*1.5),t0+2*beat+ (beat*.5 if b%4==3 else 0),0,.8)
    if 2<=b<NB-1:
        for q in range(4):
            if q in (0,2): add(kick(),t0+q*beat,0,1)
            if q in (1,3): add(snare(),t0+q*beat+0.012,.1,1)
        if b%4==3: add(kick(),t0+2.5*beat,0,.7)
        for e in range(8):
            sw=0.06*beat if e%2 else 0
            add(hat(.6 if e%2 else 1),t0+e*beat/2+sw,.35,1)
    if b>=4 and b<NB-1 and b%2==0:
        for off,m in mel:
            if off< 8: add(bell(m+(12 if b%8==4 else 0)),t0+off*beat,-.3,1)
# vinyl
crack=np.zeros(L); idx=rng.integers(0,L,int(L/SR*14)); crack[idx]=rng.normal(0,.5,len(idx))
sos=butter(2,2500,'high',fs=SR,output='sos'); crack=sosfilt(sos,crack)*.05+sosfilt(butter(2,[300,3000],'band',fs=SR,output='sos'),rng.normal(0,1,L))*.0035
L_+=crack; R_+=np.roll(crack,37)
# reverb
ir_n=int(2.4*SR); tt=np.arange(ir_n)/SR
irL=rng.normal(0,1,ir_n)*np.exp(-tt*2.6); irR=rng.normal(0,1,ir_n)*np.exp(-tt*2.6)
irL=sosfilt(butter(2,4500,'low',fs=SR,output='sos'),irL); irR=sosfilt(butter(2,4500,'low',fs=SR,output='sos'),irR)
irL/=np.sqrt((irL**2).sum()); irR/=np.sqrt((irR**2).sum())
wL=fftconvolve(L_,irL)[:L]; wR=fftconvolve(R_,irR)[:L]
outL=L_*.78+wL*.38; outR=R_*.78+wR*.38
sos=butter(1,7500,'low',fs=SR,output='sos'); outL=sosfilt(sos,outL); outR=sosfilt(sos,outR)
st=np.stack([outL,outR],1); st/=np.abs(st).max()*1.12
sf.write('lofi.wav',st,SR); print(L/SR)
