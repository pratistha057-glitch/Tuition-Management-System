document.addEventListener("DOMContentLoaded", function () {
    // 1. Mobile navigation toggle
    const navToggle = document.querySelector(".nav-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (navToggle && navLinks) {
        navToggle.addEventListener("click", function () {
            const isOpen = navLinks.classList.toggle("open");

            navToggle.setAttribute("aria-expanded", String(isOpen));
        });

        // Close the navigation after clicking a link
        navLinks.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () {
                navLinks.classList.remove("open");
                navToggle.setAttribute("aria-expanded", "false");
            });
        });
    }

    // 2. Homepage contact form
    const contactForm = document.getElementById("contactForm");
    const formAlert = document.getElementById("formAlert");

    if (contactForm && formAlert) {
        contactForm.addEventListener("submit", function (event) {
            event.preventDefault();

            // Show a success message
            formAlert.hidden = false;

            // Clear the form fields
            contactForm.reset();

            // Hide the message after five seconds
            window.setTimeout(function () {
                formAlert.hidden = true;
            }, 5000);
        });
    }

    // 3. Homepage navigation active-link highlighting
    const homeNavLinks = document.querySelectorAll(
        '.nav-links a[href*="#"]'
    );

    const sections = document.querySelectorAll(
        ".home-hero[id], .home-section[id]"
    );

    if (homeNavLinks.length && sections.length) {
        function updateActiveLink() {
            let currentSection = "";

            sections.forEach(function (section) {
                const sectionTop = section.getBoundingClientRect().top;

                if (sectionTop <= 160) {
                    currentSection = section.id;
                }
            });

            homeNavLinks.forEach(function (link) {
                const linkUrl = new URL(link.href, window.location.href);
                const sectionId = linkUrl.hash.substring(1);

                link.classList.toggle(
                    "active",
                    sectionId !== "" && sectionId === currentSection
                );
            });
        }

        window.addEventListener("scroll", updateActiveLink);
        updateActiveLink();
    }
});