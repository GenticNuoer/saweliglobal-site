# saweli.com

Source for the Saweli website, deployed to Cloudflare Pages (project `saweli`).

- `build3.py` builds the English site into `site/` (pages, assets, sitemap, headers).
- `src/` holds the stylesheet, scripts, the how-it-works film and the Pages worker (enquiry form, subscribe, admin inbox).
- `site/zh`, `site/so`, `site/sw` are the Chinese, Somali and Swahili pages.
- `deploy.js` pulls this repo into the Cloudflare dashboard, downloads the photos listed in `site/img.json` so they are served from saweli.com, and creates a Pages deployment.
