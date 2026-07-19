/* ============================================================================
   Kopo · Shared scripts · Brand Guide V1.4
   - kobot eyes follow + blink + grab/drag pendulum
   - reveal-on-scroll (IntersectionObserver)
   - nav scroll background opacity
   - animated counters (data-count)
   - mobile drawer (burger + ESC + close on link click)
   ============================================================================ */
(function () {
  'use strict';

  function initKobots() {
    const kobots = document.querySelectorAll('.kobot[data-interactive]');
    if (!kobots.length) return;

    kobots.forEach((kobot) => {
      const scheduleBlink = () => {
        const next = 2500 + Math.random() * 4500;
        setTimeout(() => {
          kobot.classList.add('blinking');
          setTimeout(() => kobot.classList.remove('blinking'), 140);
          scheduleBlink();
        }, next);
      };
      scheduleBlink();
    });

    window.addEventListener('mousemove', (e) => {
      kobots.forEach((kobot) => {
        if (kobot.classList.contains('is-grabbed') || kobot.classList.contains('is-pleading')) return;
        const pupil = kobot.querySelector('.pupil');
        const zone = kobot.querySelector('.pupil-zone');
        if (!pupil || !zone) return;
        const rect = zone.getBoundingClientRect();
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;
        const dx = e.clientX - cx;
        const dy = e.clientY - cy;
        const dist = Math.hypot(dx, dy);
        const maxPct = 34;
        const factor = Math.min(1, dist / 600);
        const angle = Math.atan2(dy, dx);
        const ox = Math.cos(angle) * maxPct * factor;
        const oy = Math.sin(angle) * maxPct * factor;
        pupil.style.transform = `translate(calc(-50% + ${ox}%), calc(-50% + ${oy}%))`;
      });
    });
  }

  function initReveal() {
    const els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('in-view');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.18, rootMargin: '0px 0px -60px 0px' });
    els.forEach((el) => io.observe(el));
  }

  function initSectionInView() {
    const sections = document.querySelectorAll('[data-section-reveal]');
    if (!sections.length) return;
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) e.target.classList.add('in-view');
      });
    }, { threshold: 0.3 });
    sections.forEach((s) => io.observe(s));
  }

  function initNav() {
    const nav = document.querySelector('.nav');
    if (!nav) return;
    const onScroll = () => {
      if (window.scrollY > 30) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  function initCounters() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const to = parseFloat(el.dataset.count);
        const decimals = parseInt(el.dataset.decimals || '0', 10);
        const dur = 1600;
        const start = performance.now();
        const tick = (now) => {
          const t = Math.min(1, (now - start) / dur);
          const eased = 1 - Math.pow(1 - t, 3);
          el.textContent = (to * eased).toFixed(decimals);
          if (t < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        io.unobserve(el);
      });
    }, { threshold: 0.4 });
    counters.forEach((el) => io.observe(el));
  }

  /* Hero kobot · grab & drag (vrai pendule virtuel) */
  function initKobotGrab() {
    const kobot = document.getElementById('heroKobot');
    if (!kobot) return;

    const CABLE_RATIO = 6;
    const MAX_ANGLE   = 12;
    const MAX_PULL_Y  = 70;
    const SWEAT_DELAY = 1400;
    const PLEAD_HOLD  = 900;

    let dragging = false;
    let sweatTimer = null;
    let pleadTimer = null;

    function getPoint(e) {
      if (e.touches && e.touches[0]) return { x: e.touches[0].clientX, y: e.touches[0].clientY };
      return { x: e.clientX, y: e.clientY };
    }

    const layoutHost = kobot.closest('.hero-kobot-wrap');
    if (!layoutHost) return;

    function computeAngle(mx, my) {
      const rect = layoutHost.getBoundingClientRect();
      const pivotX = rect.left + rect.width / 2;
      const pivotY = rect.top - CABLE_RATIO * rect.height;
      const dx = mx - pivotX;
      const dy = my - pivotY;
      let deg = -Math.atan2(dx, dy) * (180 / Math.PI);
      if (deg >  MAX_ANGLE) deg =  MAX_ANGLE;
      if (deg < -MAX_ANGLE) deg = -MAX_ANGLE;
      return deg;
    }

    function computePullY(my) {
      const rect = layoutHost.getBoundingClientRect();
      const naturalY = rect.top + rect.height / 2;
      let pull = my - naturalY;
      if (pull < 0) pull = 0;
      if (pull > MAX_PULL_Y) pull = MAX_PULL_Y;
      return pull;
    }

    function onDown(e) {
      const pt = getPoint(e);
      dragging = true;
      if (pleadTimer) { clearTimeout(pleadTimer); pleadTimer = null; }
      kobot.classList.remove('is-returning', 'is-pleading');
      kobot.classList.add('is-grabbed');
      document.body.classList.add('kobot-dragging');
      kobot.style.setProperty('--drag-rotate', computeAngle(pt.x, pt.y) + 'deg');
      kobot.style.setProperty('--drag-y', computePullY(pt.y) + 'px');
      sweatTimer = setTimeout(() => { if (dragging) kobot.classList.add('is-sweating'); }, SWEAT_DELAY);
      e.preventDefault();
    }

    function onMove(e) {
      if (!dragging) return;
      const pt = getPoint(e);
      kobot.style.setProperty('--drag-rotate', computeAngle(pt.x, pt.y) + 'deg');
      kobot.style.setProperty('--drag-y', computePullY(pt.y) + 'px');
    }

    function onUp() {
      if (!dragging) return;
      dragging = false;
      clearTimeout(sweatTimer); sweatTimer = null;
      kobot.classList.remove('is-grabbed', 'is-sweating');
      kobot.classList.add('is-returning', 'is-pleading');
      document.body.classList.remove('kobot-dragging');
      const pupil = kobot.querySelector('.pupil');
      if (pupil) pupil.style.transform = '';
      kobot.offsetHeight;
      kobot.style.setProperty('--drag-rotate', '0deg');
      kobot.style.setProperty('--drag-y', '0px');
      setTimeout(() => kobot.classList.remove('is-returning'), 1000);
      pleadTimer = setTimeout(() => {
        kobot.classList.remove('is-pleading');
        pleadTimer = null;
      }, PLEAD_HOLD);
    }

    kobot.addEventListener('mousedown', onDown);
    kobot.addEventListener('touchstart', onDown, { passive: false });
    document.addEventListener('mousemove', onMove);
    document.addEventListener('touchmove', onMove, { passive: false });
    document.addEventListener('mouseup', onUp);
    document.addEventListener('touchend', onUp);
    document.addEventListener('touchcancel', onUp);
    window.addEventListener('blur', onUp);
  }

  function initMobileMenu() {
    const burger = document.getElementById('navBurger');
    const drawer = document.getElementById('navMobile');
    if (!burger || !drawer) return;

    function setOpen(isOpen) {
      drawer.classList.toggle('is-open', isOpen);
      document.body.classList.toggle('menu-open', isOpen);
      burger.setAttribute('aria-expanded', String(isOpen));
      drawer.setAttribute('aria-hidden', String(!isOpen));
    }
    const close = () => setOpen(false);
    const toggle = () => setOpen(!drawer.classList.contains('is-open'));

    burger.addEventListener('click', toggle);
    drawer.querySelectorAll('a').forEach((a) => a.addEventListener('click', close));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) close();
    });
    const mq = window.matchMedia('(min-width: 801px)');
    mq.addEventListener('change', (e) => { if (e.matches) close(); });
  }

  document.addEventListener('DOMContentLoaded', () => {
    initKobots();
    initKobotGrab();
    initReveal();
    initSectionInView();
    initNav();
    initCounters();
    initMobileMenu();
  });
})();
