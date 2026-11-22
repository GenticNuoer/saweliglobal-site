import soundfile as sf, numpy as np, json
from kokoro_onnx import Kokoro
k=Kokoro('kokoro-v1.0.onnx','voices-v1.0.bin')
v=0.55*k.get_voice_style('bf_emma')+0.45*k.get_voice_style('af_heart')
L=[('intro',"Two markets. One trusted route. This is how Saweli works."),
('order',"Tell us what you need: the product, the quantity, and the port. You see the full cost before you pay anything."),
('verify',"Before any money moves, we check the supplier. Their licence, their factory, their export history. If they fail, they are out."),
('inspect',"Your goods are inspected before they ship. Quantity, quality, packing and labels, with a photo report sent straight to you."),
('ship',"Then we ship to your port. From Ningbo or Guangzhou, to Mogadishu, Mombasa or Djibouti, with every document travelling alongside."),
('pay',"Payment goes through a partner bank, with the invoice and inspection report attached. Everyone sees the same record."),
('end',"Saweli. Where two markets meet. Start your order at saweli dot com.")]
out={}
for n,t in L:
    ph=k.tokenizer.phonemize(t,'en-gb').replace('sˈɔːli','sɑwˈɛli')
    print(n,ph)
    a,sr=k.create(ph,voice=v,speed=0.94,lang='en-gb',is_phonemes=True)
    sf.write(f'vo_{n}.wav',a,sr);out[n]=round(len(a)/sr,2)
print(json.dumps(out),sr)
