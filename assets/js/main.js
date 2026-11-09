/* ==========================================================================
   Millstone & Co. — main.js  (vanilla JS, no dependencies besides Bootstrap's
   own bundle for dropdowns / collapse / offcanvas / accordion / modals)

   Every behaviour is switched on by a data-* attribute in the markup. Pages
   never need inline <script> blocks. NOTHING here talks to a server — every
   form, login and order is a FRONT-END DEMO.

   MARKUP CONTRACTS
   ----------------
   [data-theme-toggle]            button: light <-> dark, saved in localStorage "mm-theme"
   [data-dir-toggle]              button: toggles LTR <-> RTL, saved in "mm-dir" (ltr|rtl).
     [data-dir-code]              ...child that shows the current direction (LTR / RTL)
   [data-reveal]                  fade/slide-in when scrolled into view
   [data-count-up="1200"]         animated number; optional data-suffix="+" data-prefix="$"
   [data-year]                    filled with the current year

   FILTER / SEARCH (products, blog)
   [data-filter-group="NAME"]     wrapper of buttons  <button data-filter="grain">
   [data-filter-item="NAME"]      cards; data-category="grain blend" (space-separated)
                                  optional data-search="extra searchable words"
   [data-filter-search="NAME"]    <input type="search"> for live text search
   [data-filter-count="NAME"]     element that shows "N results"
   [data-filter-empty="NAME"]     element revealed when nothing matches (use hidden attr)

   [data-table-filter="#id"]      <input> that filters the rows of the table with that id
   [data-billing-toggle]          wrapper with buttons [data-billing="monthly|annual"];
                                  prices:  <span data-price-monthly="24" data-price-annual="20">
   [data-estimate]                wrapper: [data-estimate-unit] <select> whose <option
                                  data-price="2.5">, [data-estimate-qty] number input,
                                  [data-estimate-out] receives the demo total
   [data-countdown="ISO date"]    children [data-cd="days|hours|mins|secs"]
   [data-password-toggle]         button with aria-controls="inputId": show/hide password
   [data-add-to-basket]            product button: adds the card to the browser's saved basket
   [data-demo-toast="message"]    any button/link: shows a toast instead of navigating
   form[data-demo-form]           validated with Bootstrap classes; on success shows a toast
                                  (data-demo-message) and optionally data-redirect="page.html"
   [data-back-to-top]             floating button, appears after scrolling
   ========================================================================== */
(function () {
  'use strict';

  var doc = document.documentElement;
  var BS_CSS = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap';

  /* Safe localStorage (private windows / blocked storage must not break the page) */
  function store(key, val) {
    try {
      if (val === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, val);
    } catch (e) { /* ignore */ }
    return null;
  }
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }

  /* ---- Toast (live region so screen readers announce it) ------------------ */
  var toastZone;
  function toast(message) {
    if (!toastZone) {
      toastZone = document.createElement('div');
      toastZone.className = 'toast-zone';
      toastZone.setAttribute('role', 'status');
      toastZone.setAttribute('aria-live', 'polite');
      document.body.appendChild(toastZone);
    }
    var t = document.createElement('div');
    t.className = 'toast-mm';
    t.innerHTML = '<i class="bi bi-check-circle-fill" aria-hidden="true"></i><span></span>';
    t.lastChild.textContent = message;
    toastZone.appendChild(t);
    setTimeout(function () { t.remove(); }, 4200);
  }

  /* ---- Product basket ---------------------------------------------------- */
  var basket = $('[data-basket]');
  if (basket) {
    var basketKey = 'mm-basket';
    var basketItems = [];
    var basketList = $('[data-basket-items]', basket);
    var basketEmpty = $('[data-basket-empty]', basket);
    var basketCount = $('[data-basket-count]', basket);
    var basketTotal = $('[data-basket-total]', basket);
    var clearBasket = $('[data-basket-clear]', basket);

    try {
      var savedBasket = localStorage.getItem(basketKey);
      if (savedBasket) {
        var parsedBasket = JSON.parse(savedBasket);
        if (Array.isArray(parsedBasket) && parsedBasket.every(function (item) {
          return item && typeof item.name === 'string' && item.name.length <= 120 &&
            typeof item.price === 'number' && isFinite(item.price) && item.price >= 0 &&
            typeof item.quantity === 'number' && isFinite(item.quantity) &&
            Math.floor(item.quantity) === item.quantity && item.quantity > 0;
        })) {
          basketItems = parsedBasket;
        } else {
          toast('Your saved basket could not be read. Start a new basket below.');
        }
      }
    } catch (e) {
      toast('Your saved basket could not be read. Start a new basket below.');
    }

    function saveBasket() {
      try {
        localStorage.setItem(basketKey, JSON.stringify(basketItems));
        return true;
      } catch (e) {
        toast('Basket changes could not be saved in this browser.');
        return false;
      }
    }

    function renderBasket() {
      basketList.textContent = '';
      var quantity = 0;
      var subtotal = 0;
      basketItems.forEach(function (item, index) {
        quantity += item.quantity;
        subtotal += item.price * item.quantity;

        var row = document.createElement('li');
        row.className = 'd-flex justify-content-between align-items-center gap-3 py-1';
        var description = document.createElement('span');
        description.textContent = item.name + ' × ' + item.quantity + ' — $' + (item.price * item.quantity).toFixed(2);
        var remove = document.createElement('button');
        remove.type = 'button';
        remove.className = 'btn btn-ghost btn-sm';
        remove.setAttribute('data-basket-remove', String(index));
        remove.setAttribute('aria-label', 'Remove ' + item.name + ' from basket');
        remove.textContent = 'Remove';
        row.appendChild(description);
        row.appendChild(remove);
        basketList.appendChild(row);
      });

      basket.hidden = basketItems.length === 0;
      basketEmpty.hidden = basketItems.length !== 0;
      basketCount.textContent = '(' + quantity + (quantity === 1 ? ' item' : ' items') + ')';
      basketTotal.textContent = '$' + subtotal.toFixed(2);
      clearBasket.hidden = basketItems.length === 0;
    }

    $$('[data-add-to-basket]').forEach(function (button) {
      button.addEventListener('click', function () {
        var card = button.closest('.product-card');
        var nameElement = card && $('h3', card);
        var priceElement = card && $('.price', card);
        var match = priceElement && priceElement.textContent.match(/\$([\d]+(?:\.\d{1,2})?)/);
        if (!nameElement || !match) {
          toast('This product could not be added. Please try again.');
          return;
        }

        var name = nameElement.textContent.trim();
        var price = Number(match[1]);
        var item = basketItems.filter(function (entry) { return entry.name === name; })[0];
        if (item) item.quantity += 1;
        else basketItems.push({ name: name, price: price, quantity: 1 });

        renderBasket();
        if (saveBasket()) toast(name + ' added to your basket.');
      });
    });

    basketList.addEventListener('click', function (e) {
      var remove = e.target.closest ? e.target.closest('[data-basket-remove]') : null;
      if (!remove) return;
      basketItems.splice(Number(remove.getAttribute('data-basket-remove')), 1);
      renderBasket();
      saveBasket();
    });

    clearBasket.addEventListener('click', function () {
      basketItems = [];
      renderBasket();
      saveBasket();
    });

    renderBasket();
  }

  /* ---- Theme -------------------------------------------------------------- */
  function applyTheme(theme) {
    doc.setAttribute('data-bs-theme', theme);
    $$('[data-theme-toggle]').forEach(function (b) {
      b.setAttribute('aria-pressed', theme === 'dark' ? 'true' : 'false');
      b.setAttribute('aria-label', theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
      b.setAttribute('title', theme === 'dark' ? 'Light theme' : 'Dark theme');
    });
  }
  $$('[data-theme-toggle]').forEach(function (b) {
    b.addEventListener('click', function () {
      var next = doc.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
      store('mm-theme', next);
      applyTheme(next);
    });
  });
  applyTheme(doc.getAttribute('data-bs-theme') || 'light');

  /* ---- Text direction (LTR <-> RTL) --------------------------------------- *
   * The copy stays in English; only layout direction changes. Bootstrap ships a
   * separate RTL build, so the stylesheet is swapped when direction changes.   */
  var DIRS = ['ltr', 'rtl'];
  var DIR_NAMES = { ltr: 'left-to-right (LTR)', rtl: 'right-to-left (RTL)' };
  function applyDir(dir) {
    var rtl = dir === 'rtl';
    doc.setAttribute('lang', 'en');
    doc.setAttribute('dir', rtl ? 'rtl' : 'ltr');
    var link = document.getElementById('bs-css');
    var isRtlCss = link ? /\.rtl\.min\.css$/.test(link.href) : false;
    if (link && isRtlCss !== rtl) link.setAttribute('href', BS_CSS + (rtl ? '.rtl' : '') + '.min.css');
    var next = rtl ? 'ltr' : 'rtl';
    $$('[data-dir-code]').forEach(function (c) { c.textContent = dir.toUpperCase(); });
    $$('[data-dir-toggle]').forEach(function (b) {
      b.setAttribute('aria-label', 'Text direction: ' + DIR_NAMES[dir] + '. Switch to ' + DIR_NAMES[next]);
      b.setAttribute('title', 'Switch to ' + (next === 'rtl' ? 'RTL' : 'LTR') + ' layout');
    });
  }
  var dir = store('mm-dir') || 'ltr';
  if (dir === 'ar' || dir === 'he') dir = 'rtl';
  if (DIRS.indexOf(dir) < 0) dir = 'ltr';
  applyDir(dir);
  $$('[data-dir-toggle]').forEach(function (b) {
    b.addEventListener('click', function () {
      var next = doc.getAttribute('dir') === 'rtl' ? 'ltr' : 'rtl';
      store('mm-dir', next);
      applyDir(next);
    });
  });

  /* ---- Year, scroll-reveal, count-up ------------------------------------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  var reduceMotion = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window && !reduceMotion) {
    doc.classList.add('js-reveal');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); }
      });
    }, { threshold: .12, rootMargin: '0px 0px -5% 0px' });
    $$('[data-reveal]').forEach(function (el) { io.observe(el); });
    /* Safety net: never leave content hidden if the observer misfires */
    setTimeout(function () { $$('[data-reveal]:not(.is-visible)').forEach(function (el) { el.classList.add('is-visible'); }); }, 4000);
  }
  function runCount(el) {
    var end = parseFloat(el.getAttribute('data-count-up')) || 0;
    var pre = el.getAttribute('data-prefix') || '', suf = el.getAttribute('data-suffix') || '';
    var dec = (String(end).split('.')[1] || '').length;
    if (reduceMotion) { el.textContent = pre + end.toLocaleString('en-US') + suf; return; }
    var t0 = null;
    function tick(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / 1200, 1), v = end * (1 - Math.pow(1 - p, 3));
      el.textContent = pre + v.toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  var counters = $$('[data-count-up]');
  counters.forEach(function (el) { /* real value in the markup first = no-JS fallback */ });
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { runCount(e.target); cio.unobserve(e.target); } });
    }, { threshold: .4 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---- Filter groups + search (products & blog) -------------------------- */
  $$('[data-filter-group]').forEach(function (group) {
    var name = group.getAttribute('data-filter-group');
    var items = $$('[data-filter-item="' + name + '"]');
    var search = $('[data-filter-search="' + name + '"]');
    var count = $('[data-filter-count="' + name + '"]');
    var empty = $('[data-filter-empty="' + name + '"]');
    var active = 'all';
    function run() {
      var q = search ? search.value.trim().toLowerCase() : '';
      var shown = 0;
      items.forEach(function (it) {
        var cats = (it.getAttribute('data-category') || '').split(/\s+/);
        var okCat = active === 'all' || cats.indexOf(active) > -1;
        var hay = ((it.getAttribute('data-search') || '') + ' ' + it.textContent).toLowerCase();
        var ok = okCat && (!q || hay.indexOf(q) > -1);
        it.hidden = !ok;
        if (ok) shown++;
      });
      if (count) count.textContent = shown + (shown === 1 ? ' result' : ' results');
      if (empty) empty.hidden = shown !== 0;
    }
    $$('[data-filter]', group).forEach(function (btn) {
      btn.setAttribute('aria-pressed', btn.getAttribute('data-filter') === 'all' ? 'true' : 'false');
      btn.addEventListener('click', function () {
        active = btn.getAttribute('data-filter');
        $$('[data-filter]', group).forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        run();
      });
    });
    if (search) {
      search.addEventListener('input', run);
      var f = search.form; if (f) f.addEventListener('submit', function (e) { e.preventDefault(); run(); });
    }
    run();
  });

  /* ---- Table filter ------------------------------------------------------- */
  $$('[data-table-filter]').forEach(function (input) {
    var table = $(input.getAttribute('data-table-filter'));
    if (!table) return;
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      $$('tbody tr', table).forEach(function (tr) { tr.hidden = q && tr.textContent.toLowerCase().indexOf(q) < 0; });
    });
  });

  /* ---- Monthly / annual billing toggle ----------------------------------- */
  $$('[data-billing-toggle]').forEach(function (wrap) {
    var btns = $$('[data-billing]', wrap);
    function set(mode) {
      btns.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-billing') === mode ? 'true' : 'false'); });
      $$('[data-price-monthly]').forEach(function (el) { el.textContent = el.getAttribute(mode === 'annual' ? 'data-price-annual' : 'data-price-monthly'); });
      $$('[data-billing-label]').forEach(function (el) { el.textContent = mode === 'annual' ? '/mo, billed yearly' : '/month'; });
    }
    btns.forEach(function (b) { b.addEventListener('click', function () { set(b.getAttribute('data-billing')); }); });
    set('monthly');
  });

  /* ---- Demo price estimator (schedule grinding) -------------------------- */
  $$('[data-estimate]').forEach(function (wrap) {
    var unit = $('[data-estimate-unit]', wrap), qty = $('[data-estimate-qty]', wrap), out = $('[data-estimate-out]', wrap);
    function calc() {
      var opt = unit.options[unit.selectedIndex];
      var total = (parseFloat(opt && opt.getAttribute('data-price')) || 0) * (parseFloat(qty.value) || 0);
      out.textContent = '$' + total.toFixed(2);
    }
    unit.addEventListener('change', calc); qty.addEventListener('input', calc); calc();
  });

  /* ---- Countdown (coming soon) ------------------------------------------- */
  $$('[data-countdown]').forEach(function (wrap) {
    var target = new Date(wrap.getAttribute('data-countdown')).getTime();
    function pad(n) { return String(n).padStart(2, '0'); }
    function tick() {
      var d = Math.max(0, target - Date.now()), s = Math.floor(d / 1000);
      var parts = { days: Math.floor(s / 86400), hours: Math.floor(s % 86400 / 3600), mins: Math.floor(s % 3600 / 60), secs: s % 60 };
      Object.keys(parts).forEach(function (k) { var el = $('[data-cd="' + k + '"]', wrap); if (el) el.textContent = pad(parts[k]); });
    }
    tick(); setInterval(tick, 1000);
  });

  /* ---- Password reveal ---------------------------------------------------- */
  $$('[data-password-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var input = document.getElementById(btn.getAttribute('aria-controls'));
      if (!input) return;
      var show = input.type === 'password';
      input.type = show ? 'text' : 'password';
      btn.setAttribute('aria-pressed', show ? 'true' : 'false');
      btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
      var i = $('.bi', btn); if (i) i.className = 'bi ' + (show ? 'bi-eye-slash' : 'bi-eye');
    });
  });

  /* ---- Demo toasts on buttons/links -------------------------------------- */
  document.addEventListener('click', function (e) {
    var el = e.target.closest ? e.target.closest('[data-demo-toast]') : null;
    if (!el) return;
    e.preventDefault();
    toast(el.getAttribute('data-demo-toast'));
  });

  /* ---- Demo forms: validate, never submit anywhere ----------------------- */
  $$('form[data-demo-form]').forEach(function (form) {
    form.setAttribute('novalidate', '');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) {
        form.classList.add('was-validated');
        var bad = $(':invalid', form); if (bad) bad.focus();
        return;
      }
      form.classList.remove('was-validated');
      toast(form.getAttribute('data-demo-message') || 'This action is not available yet; nothing was sent or saved.');
      var modalEl = form.closest('.modal');
      if (modalEl && window.bootstrap) { var inst = bootstrap.Modal.getInstance(modalEl); if (inst) inst.hide(); }
      var go = form.getAttribute('data-redirect');
      if (go) setTimeout(function () { location.href = go; }, 900);
      else form.reset();
    });
  });

  /* ---- In-place Customer Portal Login (stays on same page, gives success) - */
  var authLoginForm = $('form[data-auth-login]');
  if (authLoginForm) {
    authLoginForm.setAttribute('novalidate', '');
    authLoginForm.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!authLoginForm.checkValidity()) {
        authLoginForm.classList.add('was-validated');
        var bad = $(':invalid', authLoginForm); if (bad) bad.focus();
        return;
      }
      authLoginForm.classList.remove('was-validated');
      var emailEl = $('#l-email', authLoginForm);
      var emailVal = (emailEl && emailEl.value.trim()) || 'anita@example.com';
      var namePart = emailVal.split('@')[0];
      var displayName = emailVal.toLowerCase().indexOf('anita') > -1 ? 'Anita Sharma' : (namePart.charAt(0).toUpperCase() + namePart.slice(1));

      toast('Welcome back, ' + displayName + '. Your customer portal preview is ready.');

      var cardBody = document.getElementById('auth-card-body');
      if (cardBody) {
        cardBody.innerHTML =
          '<div class="auth-success-state text-center py-2">' +
            '<div class="auth-success-badge mb-3">' +
              '<i class="bi bi-check-circle-fill" aria-hidden="true"></i>' +
            '</div>' +
            '<div class="auth-pill-status mb-2">' +
              '<span class="pulse-dot"></span> Customer Session Active' +
            '</div>' +
            '<h2 class="h3 fw-bold mb-2">Login Successful!</h2>' +
            '<p class="text-muted mb-4">Welcome back, <strong>' + displayName + '</strong>.</p>' +
            '<div class="auth-session-details text-start mb-4">' +
              '<div class="d-flex justify-content-between align-items-center py-2 border-bottom">' +
                '<span class="text-muted small">Account Email</span>' +
                '<span class="fw-semibold small font-monospace">' + emailVal + '</span>' +
              '</div>' +
              '<div class="d-flex justify-content-between align-items-center py-2 border-bottom">' +
                '<span class="text-muted small">Account Role</span>' +
                '<span class="badge text-bg-success">Customer (Family Plan)</span>' +
              '</div>' +
              '<div class="d-flex justify-content-between align-items-center py-2 border-bottom">' +
                '<span class="text-muted small">Customer Record ID</span>' +
                '<span class="font-monospace small">#MM-20418</span>' +
              '</div>' +
              '<div class="d-flex justify-content-between align-items-center py-2">' +
                '<span class="text-muted small">Session Status</span>' +
                '<span class="text-success fw-bold small d-inline-flex align-items-center gap-1">' +
                  '<i class="bi bi-shield-check" aria-hidden="true"></i> Authenticated (Same Page)' +
                '</span>' +
              '</div>' +
            '</div>' +
            '<div class="d-grid gap-2">' +
              '<button type="button" class="btn btn-outline-secondary" onclick="window.location.reload()">' +
                '<i class="bi bi-box-arrow-left me-1" aria-hidden="true"></i> Sign in as a different user' +
              '</button>' +
            '</div>' +
          '</div>';
      }
    });
  }

  /* ---- Back to top -------------------------------------------------------- */
  $$('[data-back-to-top]').forEach(function (btn) {
    function vis() { btn.classList.toggle('show', window.scrollY > 600); }
    window.addEventListener('scroll', vis, { passive: true }); vis();
    btn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' }); });
  });

  /* ---- Close the mobile menu with Escape and after choosing a link ------- */
  var nav = document.getElementById('mainNav');
  if (nav) {
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('show')) {
        var t = $('.navbar-toggler'); if (t) { t.click(); t.focus(); }
      }
    });
  }
})();
