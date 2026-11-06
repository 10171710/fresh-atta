# Millstone & Co. — Flour Mill & Fresh Atta Delivery · HTML Template

A warm, premium, responsive **Bootstrap 5.3** template for a flour mill and fresh-atta delivery business:
21 pages, a customer dashboard, light/dark themes, and an LTR ↔ RTL layout switch (English copy, mirrored layout).

> **Important — front-end demo.** Login, registration, ordering, scheduling, billing, payments, support chat and
> analytics are **visual demos only**. Nothing is sent to a server, stored, or charged; every form shows a
> confirmation toast and (for login/registration) opens the sample dashboard. Connect your own backend and
> payment provider before going live — the billing pages contain sample card text only, never real card fields.

## Quick start

No build step and no installs. You only need a browser and an internet connection (Bootstrap, Bootstrap Icons
and Google Fonts load from CDNs).

```bash
cd millstone-atta-template
python -m http.server 8851
# open http://localhost:8851
```
Any static server works (`npx serve`, VS Code Live Server, …). Opening `index.html` directly with `file://` also
works for most pages.

## Folder structure

```
millstone-atta-template/
├── index.html                 Home 1 — fresh flour, grain quality, milling process, products, testimonials
├── home-2.html                Home 2 — digital-first: online ordering, subscriptions, delivery scheduling
├── about.html                 Story, mission, history timeline, team, testimonials
├── products.html              Filterable catalogue (whole grain, millets, pulses, blends) + custom grinding
├── product-details.html       Product detail: sizes, nutrition, how to use, pricing table, FAQ, reviews
├── delivery-plans.html        Cadences, scheduling windows, service areas, rules, FAQ
├── pricing.html               Monthly/annual toggle, plan cards, comparison table, add-ons, FAQ
├── blog.html                  Searchable + filterable blog listing, pagination
├── blog-details.html          Full article with sidebar, author box, comments form
├── contact.html               Info cards, accessible form, labelled map placeholder, hours
├── login.html · register.html Auth screens (demo)
├── dashboard.html             Overview: summary cards, next delivery, usage chart, orders
├── dashboard-schedule.html    Schedule grain grinding + deliveries
├── dashboard-recurring.html   Recurring orders: pause / skip / edit
├── dashboard-orders.html      Order history with search and detail modal
├── dashboard-billing.html     Plan, sample payment method, invoices, credits
├── dashboard-profile.html     Profile, addresses, preferences, security
├── dashboard-support.html     Support options, tickets, chat, help FAQ
├── 404.html · coming-soon.html   Error page; Coming Soon / Maintenance page
├── assets/
│   ├── css/style.css          Design tokens + all components (numbered sections, commented)
│   ├── js/main.js             Every behaviour, switched on by data-* attributes (contract in file header)
│   └── images/                Locally stored, unique photos; credits and licence details in credits.json
└── docs/
    ├── DESIGN_SYSTEM.md       Colours, type, components, class inventory, page skeletons, checklist
    ├── sync-partials.py       Re-applies shared head / header / footer / scripts / dashboard shell to all pages
    ├── contract-check.js      Console test: overflow, RTL, landmarks, labels, filters, toggles at 375/1280 px
    └── partials/              head · header · footer · scripts · app-nav · app-top
```

## Customising

| I want to… | Do this |
|---|---|
| Change brand colours, fonts, radius | Edit the CSS variables in **section 1** of `assets/css/style.css` (light and dark blocks). |
| Rename the business / change address, phone | Edit `docs/partials/*.html` (header, footer, head) then run `python docs/sync-partials.py`. Page copy is plain HTML. |
| Add / reorder navigation | Edit `docs/partials/header.html` (and `NAV_HREF` in `docs/sync-partials.py` for a new key), then re-sync. |
| Replace photos | Update the relevant local image path in the page's `<img>` element. The `.ph` frame preserves the image crop; page-intro photos use `.page-feature-photo`. See `assets/images/credits.json` for source and licence details. |
| Set the canonical URL / social card | Edit `docs/partials/head.html` (`https://www.example.com/millstone/…`) and add `assets/img/social-card.jpg` (1200×630). |
| Enable RTL layout | The header/footer/dashboard controls toggle `dir="ltr"` ↔ `dir="rtl"` and swap Bootstrap's RTL stylesheet. The layout already mirrors via logical CSS; translate page copy yourself if you localise the template. |
| Change the map | `contact.html` includes a live OpenStreetMap embed. Update the `bbox` and `marker` values in the `.map-embed` URL (or swap in your own embed) and update the directions link beside it. Dark mode tints the map automatically. |
| Hook up forms | Every form is `<form data-demo-form>`. Remove that attribute, set `action`/`method`, and add your handler. |

`python docs/sync-partials.py` (Python 3, no packages) rewrites only the regions between
`<!-- @head -->`, `@header`, `@footer`, `@scripts`, `@appnav`, `@apptop` markers.

## Features

- **Themes & direction:** theme icon (light/dark, remembers choice and respects the OS setting) and an LTR ↔ RTL icon that swaps alignment and Bootstrap's RTL stylesheet; both persist in `localStorage` and apply before first paint (no flash).
- **Accessibility:** skip link, semantic landmarks, one `h1` per page, visible focus rings, ≥ 4.5:1 text contrast in both themes, labelled forms with validation messages, status shown by icon + text (never colour alone), `prefers-reduced-motion` respected, keyboard-friendly menus, accordions, tabs and modals.
- **SEO:** unique titles/descriptions, canonical, Open Graph and Twitter tags; `noindex` on login, registration, dashboard, 404 and coming-soon.
- **Mobile-first:** collapsing navigation with always-visible theme/direction controls, off-canvas dashboard menu, responsive tables.
- **Interactions (vanilla JS):** product/blog filtering and search, monthly/annual price toggle, demo price estimator, table search, countdown, count-up stats, password reveal, toasts, scroll-reveal, back-to-top.

## Libraries & dependencies (all via CDN, no npm)

| Library | Version | Purpose |
|---|---|---|
| [Bootstrap](https://getbootstrap.com) (CSS + RTL CSS + JS bundle) | 5.3.3 | grid, components, dropdowns, collapse, offcanvas, modals, accordion, tabs |
| [Bootstrap Icons](https://icons.getbootstrap.com) | 1.11.3 | icon font |
| [Google Fonts](https://fonts.google.com) | — | Playfair Display, Inter |

To work offline or self-host, download these files into `assets/vendor/` and update `docs/partials/head.html`,
`docs/partials/scripts.html` and the `BS_CSS` constant at the top of `assets/js/main.js`.

## Browser support
Current Chrome, Edge, Firefox and Safari (uses CSS variables, `aspect-ratio`, logical properties).

## Testing
Serve the folder, open any page, paste `docs/contract-check.js` into the console and run
`await mmCheck()` — it loads every page at 375 px and 1280 px in LTR and RTL and reports failures.

## Licence & credits
Template code © Millstone & Co. demo brand. Photo source-page links and licence details are recorded in
`assets/images/credits.json`; follow each source licence if you reuse an image outside this demo. Bootstrap
(MIT), Bootstrap Icons (MIT), Google Fonts (OFL).
All names, addresses, prices and testimonials are fictional sample content.
