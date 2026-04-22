/* Sanskriti Handicraft Studio - Script */
document.addEventListener('DOMContentLoaded', () => {

  // AOS init
  if (typeof AOS !== 'undefined') {
    AOS.init({ duration: 900, easing: 'ease-out-cubic', once: true, offset: 40 });
  }

  // Navbar scroll
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    });
  }

  // Mobile menu
  const menuToggle = document.querySelector('.menu-toggle');
  const closeMenu = document.querySelector('.close-menu');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', () => mobileMenu.classList.add('active'));
  }
  if (closeMenu && mobileMenu) {
    closeMenu.addEventListener('click', () => mobileMenu.classList.remove('active'));
  }
  document.querySelectorAll('.mobile-menu a').forEach(a => {
    a.addEventListener('click', () => mobileMenu && mobileMenu.classList.remove('active'));
  });

  // Year
  const yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();

  // Contact form
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', async e => {
      e.preventDefault();

      const emailInput = form.querySelector('input[type="email"]');
      const emailVal = emailInput ? emailInput.value : '';
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      if (emailInput && !emailPattern.test(emailVal)) {
        alert("Please enter a valid email address.");
        emailInput.focus();
        return;
      }

      const btn = form.querySelector('button[type=submit]');
      const orig = btn.innerHTML;
      btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending…';
      btn.disabled = true;

      try {
        const response = await fetch(form.action, {
          method: form.method,
          body: new FormData(form),
          headers: {
            'Accept': 'application/json'
          }
        });

        if (response.ok) {
          btn.innerHTML = '<i class="fas fa-check"></i> Sent Successfully!';
          btn.style.background = 'linear-gradient(135deg,#4CAF50,#2e7d32)';
          form.reset();
        } else {
          throw new Error('Form submission failed');
        }
      } catch (error) {
        btn.innerHTML = '<i class="fas fa-times"></i> Error Sending';
        btn.style.background = '#e53935';
      } finally {
        setTimeout(() => {
          btn.innerHTML = orig;
          btn.style.background = '';
          btn.disabled = false;
        }, 3500);
      }
    });
  }

  // WhatsApp product buttons
  document.querySelectorAll('.wa-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const product = btn.getAttribute('data-product') || 'your product';
      const phone = '919699071424';
      const msg = encodeURIComponent(`Hi! I'm interested in ${product}. Could you share more details?`);
      window.open(`https://wa.me/${phone}?text=${msg}`, '_blank');
    });
  });

});

