# Millstone & Co. — Design System & Build Brief

Commercial HTML template: flour mill + fresh atta delivery. **Bootstrap 5.3.3 (CDN) + Bootstrap Icons + a hand-written
`assets/css/style.css` + one vanilla `assets/js/main.js`.** No build step, no jQuery, no npm. Local photo assets
are used throughout the pages; image credits and licences are recorded in `assets/images/credits.json`.
Everything is a FRONT-END DEMO — never imply a real backend, payment, login or analytics.

Reference page: **`index.html`** (Home 1). Open it and copy its patterns. Read `assets/css/style.css` and the
contract comment at the top of `assets/js/main.js` before writing a page.

## 1. Page skeleton (every page)

```html
<!doctype html>
<html lang="en" dir="ltr">
<head>
<!-- @head {"title": "…", "description": "…", "file": "about.html"} -->
<!-- @head:end -->
</head>
<body>
<!-- @header {"nav": "about"} -->
<!-- @header:end -->
<main id="main"> … </main>
<!-- @footer -->
<!-- @footer:end -->
<!-- @scripts -->
<!-- @scripts:end -->
</body>
</html>
```
After writing run `python docs/sync-partials.py <your-files>.html` (ONLY your own files). It fills the marker regions.
- `nav` keys: `home1 home2 about products plans pricing blog contact dashboard none`
  (product-details → `products`; blog-details → `blog`; login/register/404/coming-soon use their own layouts, see §5).
- Add `"robots": "noindex"` to head JSON for login, register, 404, coming-soon and every dashboard page.
- Title ≤ 60 chars ending `| Millstone & Co.`; description 120–160 chars. **No inline `<script>` blocks, no inline `<style>` blocks**
  (tiny `style="--c1:…"` on `.avatar` is the only accepted inline style, plus `style="color:var(--mm-wheat)"` on dark sections).
- Exactly one `<h1>`; headings descend in order; every section has an `aria-labelledby` heading or `aria-label`.
- Subpages use a `.page-hero` with a pill-style `eyebrow`, a centered large h1 and a lead. Do not add a breadcrumb bar to the hero. Hero content is centered; the Contact hero uses a local background photo with a dark overlay and a light, constrained rounded content card, while other heroes remain photo-free. Hero sections share a minimum height matched to Home 1 and use a warm glow without grid lines. Use `<em>` in the home hero headline for its warm highlighted phrase. Keep ghost CTAs readable in both theme modes, and place homepage trust metrics within the hero content.

## 2. Brand facts (canonical — reuse exactly)

- **Millstone & Co. — Fresh Atta & Flour Mill**, est. **1987**, founded by the Becker family. Tagline: *Milled this morning. At your door tomorrow.*
- Address: **21 Granary Lane, Sunridge** · Mon–Sat 7:00 am – 7:00 pm · **+1 (555) 014-2290** · **hello@millstone.example** · support: **support@millstone.example**
- Promise: stone-ground in small batches, packed same day, delivered within 24 hours of milling, no preservatives.
- Delivery days **Tuesday, Thursday, Saturday**; windows **Morning 7–10 am, Midday 11 am–2 pm, Evening 5–8 pm**. Free delivery over $20 and on every plan. Pause/skip/change up to 6 pm the evening before.
- 12 partner farms, 3,200+ families, 37+ years, 4.9/5 rating. Sharbati wheat, protein 12%+, moisture 11–12%, ground below 40 °C.
- Team: **Harold Becker** (Founder & Master Miller), **Meera Kapoor** (Head Miller), **Daniel Okafor** (Operations & Delivery), **Layla Haddad** (Customer Care), **Noa Levi** (Quality & Sourcing).
- History: 1987 first chakki opens in a garage · 1998 move to Granary Lane · 2009 millet range launched · 2018 first home-delivery vans · 2021 online subscriptions · 2026 12 partner farms, 3,200+ families.
- Customers: **Anita Sharma** (Family plan, dashboard persona, customer ID MM-20418), Daniel Okafor (café, Kitchen plan), Layla Haddad (Household plan).
- Currency **$**; dates in 2026 (today is **Wed 4 Nov 2026** — real weekdays only: Tue 3, Thu 5, Sat 7, Tue 10, Thu 12, Sat 14, Tue 17, Thu 19, Sat 21 Nov).

### Products (name — category — size — price)
Whole grain (`grain`): **Sharbati Whole Wheat Atta** 5 kg $12.50 / 10 kg $23.90 · **Sharbati Chakki Atta (sifted)** 5 kg $13.20 · **Khapli Emmer Wheat Atta** 2 kg $9.80 · **Whole Wheat Dalia (cracked)** 1 kg $4.20 ·
Millets (`millet`): **Jowar Flour** 2 kg $7.20 · **Bajra Flour** 2 kg $6.80 · **Ragi Flour** 1 kg $5.90 · **Foxtail Millet Flour** 1 kg $6.60 ·
Pulses & gram (`pulse`): **Fresh Besan** 1 kg $6.40 · **Moong Dal Flour** 1 kg $6.90 ·
Flour blends (`blend`): **7-Grain Multigrain Atta** 5 kg $15.90 · **High-Fibre Roti Blend** 5 kg $14.60 · **Puri & Paratha Blend** 5 kg $13.90 · **Soft Phulka Blend** 5 kg $13.50.
Custom grinding: bring your own grain (wheat, jowar, bajra, ragi, rice, maize); **$0.45 / kg** grinding fee, minimum 5 kg, fine / medium / coarse.

### Plans (monthly price; annual = 15% off, shown as the lower number)
| Plan | Monthly | Annual (per mo) | Includes |
|---|---|---|---|
| **Household** | $24 | $20 | 10 kg atta/month (2 × 5 kg, fortnightly), 1 free product swap, Tue/Thu/Sat delivery |
| **Family** (featured) | $44 | $37 | 20 kg/month (weekly 5 kg), 1 multigrain or millet swap per delivery, priority slots, free bag returns |
| **Kitchen** | $119 | $101 | 60 kg/month, custom grind, business invoice, dedicated contact, bulk 25 kg sacks |
Delivery cadences: **Weekly Fresh**, **Fortnightly Fill**, **Monthly Pantry**, **Custom Grind** (customer's own grain).

### Blog categories (`data-category` values): `milling`, `nutrition`, `recipes`, `sourcing`, `news`

## 3. Class inventory (all defined in style.css — do not invent new CSS)

- **Sections:** `section`, `section-sm`, `section-alt`, `section-dark`, `section-head` (centred intro), `page-hero` (shared dark-grid page intro), `utility-hero` (404 / coming-soon intro), `grain-divider`, `cta-band`.
- **Type:** `h-hero`, `h-section`, `lead-lg`, `eyebrow`, `display-font`, `text-muted`, `meta`.
- **Cards:** `mm-card` (+ `mm-card-hover`), `product-card`, `blog-card`, `team-card`, `quote-card` (use `<figure>`), `price-card` (+ `featured`, `.flag`), `step` inside `steps`, `feature-row` + `icon-tile` (`green|blue|red`), `stat-card`.
- **Photos:** `.ph` + colourway (`ph-wheat ph-flour ph-sack ph-mill ph-field ph-roti ph-van ph-team ph-grain ph-night`) + shape (`ph-wide ph-square ph-tall ph-fill`) — use a local `<img class="ph-photo" src="assets/images/…" alt="descriptive alt text">`; optional `<span class="ph-tag">`. Page-intro photos use `.page-feature-photo`. See `assets/images/credits.json` before reusing photos. `avatar` / `avatar-lg` for people with `style="--c1:#…;--c2:#…"` initials.
- **Lists:** `check-list` (`.no` for crosses), `timeline` (li > `.year`), `list-clean`, `date-chip`.
- **Badges/status:** `badge-soft`, `badge-fresh`, `status status-ok|warn|info|bad|muted` (dot + text).
- **Forms:** Bootstrap `form-control`, `form-select`, `form-check`, `form-label`, `form-text`, `input-icon` (+ `.bi` first child, `.btn-pw` for passwords), `choice` tiles (`<label class="choice"><input type="radio"…><span class="choice-body">…</span></label>`), `demo-note`, `demo-banner`. Bootstrap validation: `.invalid-feedback`, `required`.
- **Filtering:** `filter-bar` > `filter-chip` buttons (`data-filter`), items `data-filter-item` — see main.js contract. Always provide a `data-filter-empty` message (`hidden`) and a `data-filter-count`.
- **Pricing:** `billing-toggle` buttons, `price-amount` with `<span data-price-monthly="44" data-price-annual="37">44</span>` and `<small data-billing-label>/month</small>`, `compare-table` inside `<div class="table-responsive">`.
- **FAQ:** Bootstrap `accordion` with unique ids per page.
- **Dashboard:** `app-layout`, `app-main`, `app-content`, `table-wrap > table.table`, `mini-bars`, `progress`, `nav-pills-mm`, `chat-bubble`, `stat-card`, `list-clean`, `date-chip`.
- **Utility pages:** `auth-layout`, `auth-aside`, `auth-form-wrap`, `auth-card`, `error-code`, `countdown`.
- **Icons:** Bootstrap Icons only (`bi bi-…`), `aria-hidden="true"` unless the icon is the only content (then give the control an `aria-label`).
- Layout: `container-xxl` for page width; Bootstrap grid (`row g-4`, `col-md-6 col-xl-3`). **Use logical utilities only** (`ms-/me-/ps-/pe-/text-start/text-end/float-start`) — never `left/right` hard-coding. Cards in a grid get `h-100` via `.mm-card` already.
- Scroll reveal: add `data-reveal` on grid columns / sections below the fold (never on the hero).

## 4. JS hooks (see header of main.js for full contract)
`data-theme-toggle`, `data-dir-toggle` (in header/app-top partials — don't re-add), `data-reveal`, `data-count-up`, `data-filter-group/-item/-search/-count/-empty`, `data-table-filter="#id"`,
`data-billing-toggle` + `data-billing`, `data-estimate` (+ `-unit -qty -out`), `data-countdown`, `data-password-toggle`, `data-demo-toast`, `form[data-demo-form]` (+ `data-demo-message`, `data-redirect`).
Every `<form>` must be `data-demo-form`, have `<label for>` on every field, and sit next to a visible `demo-note`.

## 5. Special layouts
- **Auth pages (login, register):** no header/footer. `<body>` → `<main id="main" class="auth-layout">` with `<aside class="auth-aside">` (brand lockup + testimonial) and `.auth-form-wrap > .auth-card`. Include a small top bar inside the form column with "← Back to website" (`index.html`) and theme + direction toggle buttons copied from `docs/partials/app-top.html` (the two `icon-btn` buttons). Login `data-redirect="dashboard.html"`. Prominent demo banner: "Demo only — any email and password open the sample dashboard." Use `@head` + `@scripts` only.
- **404 / coming-soon:** use `@header {"nav":"none"}`, `@footer`, `@scripts`; centred content with the `error-code` / `countdown` classes and helpful links. coming-soon countdown target `2027-01-15T09:00:00`; includes a notify-me demo form.
- **Dashboard pages (`dashboard*.html`):** no public header/footer. Structure:
```html
<body>
<div class="app-layout">
  <!-- @appnav {"active": "overview"} -->
  <!-- @appnav:end -->
  <div class="app-main">
    <!-- @apptop -->
    <!-- @apptop:end -->
    <main id="main" class="app-content"> <h1>…</h1> … </main>
  </div>
</div>
<!-- @scripts -->
<!-- @scripts:end -->
</body>
```
  `active` keys: `overview schedule recurring orders billing profile support`. Files: `dashboard.html`, `dashboard-schedule.html`, `dashboard-recurring.html`, `dashboard-orders.html`, `dashboard-billing.html`, `dashboard-profile.html`, `dashboard-support.html`. Each page starts with a `demo-banner` and an h1 + one-line intro. Persona: **Anita Sharma**, Family plan, MM-20418, next delivery **Thu 5 Nov 2026, Morning 7–10 am**, 10 kg Sharbati + 5 kg 7-Grain.

## 6. Accessibility & quality — definition of done
1. Loads with no console errors; no horizontal scroll at 375 px; works at 1280 px; LTR and RTL; light and dark.
2. Colour is never the only status signal; all text ≥ 4.5:1 (use the tokens — never raw hex for text).
3. Every control keyboard-reachable with visible focus; icon-only buttons have `aria-label`; tables have `<caption class="visually-hidden">`, `<th scope>`.
4. Every photo has descriptive `<img alt>` text; image sources are local and unique across the site.
5. Links descriptive ("Read the full story", not "click here"); `href="#"` is forbidden except social icons in the footer — use real page links or `data-demo-toast`.
6. Realistic flour-milling content (grains, extraction rates, milling, storage, recipes) — no lorem ipsum.
7. Demo features say so: forms carry `demo-note` ("Front-end demo — nothing is sent or saved"), checkout/payment cards say "sample".
