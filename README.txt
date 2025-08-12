
# GitHub Pages Redirects Pack

**Що це:** клієнтські редіректи для GitHub Pages без плагінів.
- `redirects.json` — список `{ "source": "/old/path.html", "destination": "/new/path.html", "type": 308 }`
- `404.html` — ловить старі шляхи і перенаправляє на нові.

## Як використати
1) Скопіювати **404.html** і **redirects.json** у **корінь** вашого сайту (`bbs-website/`).
2) (Опційно) додайте **.nojekyll** у корінь, щоб відключити Jekyll.
3) Закомітити в `main` → перевірити старі URL (має перекидати).

> Якщо сайт у підпапці `/bbs-website/`, обидва файли теж мають лежати у цій підпапці.
