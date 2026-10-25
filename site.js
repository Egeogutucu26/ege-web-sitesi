'use strict';

(() => {
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.getElementById('mobile-nav');
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());

  function setMenu(open) {
    if (!toggle || !menu) return;
    toggle.setAttribute('aria-expanded', String(open));
    toggle.dataset.open = String(open);
    toggle.setAttribute('aria-label', open ? toggle.dataset.closeLabel : toggle.dataset.openLabel);
    menu.dataset.open = String(open);
  }

  if (toggle && menu) {
    toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
    menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', event => {
      if (!event.target.closest('.site-header')) setMenu(false);
    });
    const desktop = window.matchMedia('(min-width: 981px)');
    desktop.addEventListener('change', event => { if (event.matches) setMenu(false); });
  }

  const copy = document.querySelector('[data-copy]');
  const toast = document.getElementById('toast');
  let toastTimer;
  function notify(message) {
    if (!toast) return;
    clearTimeout(toastTimer);
    toast.textContent = message;
    toast.hidden = false;
    toastTimer = setTimeout(() => { toast.hidden = true; }, 4500);
  }
  if (copy) {
    copy.addEventListener('click', async () => {
      try {
        if (!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(copy.dataset.copy);
        notify(copy.dataset.success);
      } catch {
        // Keep the visible address selectable rather than claiming an unsuccessful copy worked.
        const address = document.querySelector('.contact-email');
        if (address) {
          const range = document.createRange();
          range.selectNodeContents(address);
          const selection = window.getSelection();
          selection.removeAllRanges();
          selection.addRange(range);
        }
        notify(copy.dataset.failure);
      }
    });
  }

  if ('IntersectionObserver' in window) {
    const navLinks = document.querySelectorAll('.desktop-nav [data-section]');
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        navLinks.forEach(link => {
          const current = link.dataset.section === entry.target.id;
          if (current) link.setAttribute('aria-current', 'page');
          else link.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-18% 0px -55% 0px', threshold: 0 });
    document.querySelectorAll('main section[id]').forEach(section => observer.observe(section));
  }
})();
