document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', () => {
            const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
            navToggle.setAttribute('aria-expanded', !isExpanded);
            navLinks.classList.toggle('active');
        });

        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                navToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // 2. Optimized Bidirectional Scroll Zoom (Lightweight & Fluid)
    const zoomElements = document.querySelectorAll(
        '.content-card, .stat-card, .section-heading, .hero-content, .hero-image-wrapper'
    );

    zoomElements.forEach(el => el.classList.add('scroll-zoom-element'));

    let isTicking = false;

    function updateScrollZoom() {
        const viewportHeight = window.innerHeight;

        zoomElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            
            // Calculate progress based on element position relative to viewport center
            const elementCenter = rect.top + rect.height / 2;
            const distanceToCenter = elementCenter - viewportHeight / 2;
            
            // Normalize progress between 0 (far below/above) and 1 (fully centered)
            let progress = 1 - Math.min(Math.abs(distanceToCenter) / (viewportHeight * 0.75), 1);
            progress = Math.max(0, Math.min(1, progress)); // Clamp between 0 and 1

            // Inject smooth progress value into CSS variable
            el.style.setProperty('--scroll-progress', progress.toFixed(3));
        });

        isTicking = false;
    }

    window.addEventListener('scroll', () => {
        if (!isTicking) {
            window.requestAnimationFrame(updateScrollZoom);
            isTicking = true;
        }
    }, { passive: true });

    // Initial trigger on load
    updateScrollZoom();

    // 3. Contact Form Mock Handler
    const contactForm = document.getElementById('contactForm');
    const formAlert = document.getElementById('formAlert');

    if (contactForm && formAlert) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            formAlert.hidden = false;
            contactForm.reset();
            setTimeout(() => {
                formAlert.hidden = true;
            }, 5000);
        });
    }
});

// Global function for the portals dropdown toggle
function togglePortalMenu(event) {
    event.stopPropagation();

    const button = event.currentTarget;
    const dropdown = button.closest('.portal-dropdown');
    const menu = dropdown.querySelector('.portal-dropdown-menu');

    const isOpen = menu.classList.toggle('open');

    button.setAttribute('aria-expanded', isOpen);
}

// Close dropdown when clicking outside
document.addEventListener('click', () => {
    const dropdowns = document.querySelectorAll('.portal-dropdown');

    dropdowns.forEach(dropdown => {
        const menu = dropdown.querySelector('.portal-dropdown-menu');
        const button = dropdown.querySelector('.portal-dropdown-btn');

        if (menu) {
            menu.classList.remove('open');
        }

        if (button) {
            button.setAttribute('aria-expanded', 'false');
        }
    });
});