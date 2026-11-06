/* Millstone template — contract-check.js
   Paste into the browser console on any page served over http (python -m http.server), or run via a
   browser tool. It loads every page in a hidden iframe at 375 px and 1280 px, in LTR and RTL, and
   asserts the template's behaviour contracts. Returns a list of failures (empty = clean).
   Usage:  await mmCheck(['index.html', 'about.html'])  — or call mmCheck() for all pages. */
window.mmCheck = async function (pages, opts) {
  opts = opts || {};
  const ALL = ['index.html','home-2.html','about.html','products.html','product-details.html','delivery-plans.html','pricing.html','blog.html','blog-details.html','blog-details-2.html','blog-details-3.html','blog-details-4.html','blog-details-5.html','blog-details-6.html','blog-details-7.html','blog-details-8.html','blog-details-9.html','contact.html','login.html','register.html','404.html','coming-soon.html','dashboard.html','dashboard-schedule.html','dashboard-recurring.html','dashboard-orders.html','dashboard-billing.html','dashboard-profile.html','dashboard-support.html'];
  pages = pages || ALL;
  const fails = [];
  const wait = ms => new Promise(r => setTimeout(r, ms));
  async function load(page, width, lang) {
    const f = document.createElement('iframe');
    f.style.cssText = 'position:fixed;left:0;top:0;border:0;visibility:hidden;height:900px;width:' + width + 'px';
    document.body.appendChild(f);
    try { localStorage.setItem('mm-dir', lang); localStorage.setItem('mm-theme', 'light'); } catch (e) {}
    f.src = page + '?cc=' + Date.now();
    await new Promise(r => { f.onload = r; });
    await wait(700);
    return f;
  }
  for (const page of pages) {
    for (const [width, lang] of [[375, 'ltr'], [1280, 'ltr'], [375, 'rtl'], [1280, 'rtl']]) {
      const tag = page + ' @' + width + '/' + lang;
      const f = await load(page, width, lang);
      const d = f.contentDocument, w = f.contentWindow, root = d.documentElement;
      const bad = m => fails.push(tag + ': ' + m);
      if (root.scrollWidth > w.innerWidth + 1) {
        const off = [...d.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.width && (r.right > w.innerWidth + 1 || r.left < -1) && getComputedStyle(e).position !== 'fixed' && !e.closest('.table-wrap,.table-responsive,.offcanvas,.visually-hidden,.sr-only'); }).slice(0, 3).map(e => e.tagName + '.' + String(e.className).slice(0, 30));
        if (off.length) bad('horizontal overflow ' + off.join(' | '));
      }
      if (root.dir !== lang) bad('dir=' + root.dir);
      const rtlCss = (d.getElementById('bs-css') || {}).href || '';
      if ((lang === 'rtl') !== rtlCss.includes('.rtl.')) bad('bootstrap css build mismatch');
      if (d.querySelectorAll('h1').length !== 1) bad('h1 count ' + d.querySelectorAll('h1').length);
      if (!d.title || d.title.length > 70) bad('title length ' + (d.title || '').length);
      if (!d.querySelector('meta[name=description]')) bad('no meta description');
      if (!d.getElementById('main')) bad('no #main');
      d.querySelectorAll('.ph:not([aria-label])').forEach(() => bad('.ph without aria-label'));
      d.querySelectorAll('img:not([alt])').forEach(() => bad('img without alt'));
      const ids = {}; d.querySelectorAll('[id]').forEach(e => { ids[e.id] = (ids[e.id] || 0) + 1; });
      Object.keys(ids).filter(k => ids[k] > 1).forEach(k => bad('duplicate id ' + k));
      d.querySelectorAll('input:not([type=hidden]):not([type=radio]):not([type=checkbox]),select,textarea').forEach(el => {
        const ok = el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || (el.id && d.querySelector('label[for="' + el.id + '"]')) || el.closest('label');
        if (!ok) bad('unlabelled field ' + (el.name || el.id || el.type));
      });
      d.querySelectorAll('input[type=radio],input[type=checkbox]').forEach(el => {
        const ok = el.getAttribute('aria-label') || (el.id && d.querySelector('label[for="' + el.id + '"]')) || el.closest('label');
        if (!ok) bad('unlabelled ' + el.type + ' ' + (el.name || el.id));
      });
      d.querySelectorAll('button:not([aria-label])').forEach(b => { if (!b.textContent.trim()) bad('button with no name'); });
      d.querySelectorAll('a[href]').forEach(a => { if (!a.textContent.trim() && !a.getAttribute('aria-label')) bad('link with no name ' + a.getAttribute('href')); });
      d.querySelectorAll('script:not([src])').forEach((s, i) => { if (i > 0) bad('extra inline <script>'); });
      d.querySelectorAll('[data-filter-group]').forEach(g => {
        const n = g.getAttribute('data-filter-group'), items = d.querySelectorAll('[data-filter-item="' + n + '"]');
        if (!items.length) bad('filter group ' + n + ' has no items');
        const chip = g.querySelector('[data-filter]:not([data-filter=all])');
        if (chip) { chip.click(); const vis = [...items].filter(i => !i.hidden).length; if (!vis || vis === items.length) bad('filter ' + chip.dataset.filter + ' shows ' + vis + '/' + items.length); g.querySelector('[data-filter=all]').click(); }
      });
      d.querySelectorAll('[data-billing-toggle]').forEach(t => {
        const a = t.querySelector('[data-billing=annual]'); a.click();
        const el = d.querySelector('[data-price-monthly]'); if (el.textContent !== el.getAttribute('data-price-annual')) bad('billing toggle did not switch price');
        t.querySelector('[data-billing=monthly]').click();
      });
      if (width === 375 && d.querySelector('.navbar-toggler')) {
        d.querySelector('.navbar-toggler').click(); await wait(500);
        if (!d.getElementById('mainNav').classList.contains('show')) bad('mobile menu did not open');
      }
      if (width === 375 && d.getElementById('appSidebar')) {
        d.querySelector('[data-bs-toggle="offcanvas"]').click(); await wait(500);
        if (!d.getElementById('appSidebar').classList.contains('show')) bad('dashboard offcanvas did not open');
      }
      if (lang === 'ltr' && width === 1280) {
        const tt = d.querySelector('[data-theme-toggle]'); if (tt) { tt.click(); if (root.getAttribute('data-bs-theme') !== 'dark') bad('theme toggle failed'); }
        d.querySelectorAll('a[href$=".html"]').forEach(a => { const h = a.getAttribute('href'); if (ALL.indexOf(h) < 0 && h.indexOf('/') < 0) bad('link to missing page ' + h); });
      }
      f.remove();
    }
  }
  try { localStorage.removeItem('mm-dir'); localStorage.removeItem('mm-theme'); } catch (e) {}
  return fails.length ? fails : 'CLEAN (' + pages.length + ' pages × 4 viewports)';
};
