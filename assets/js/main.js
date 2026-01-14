// SwapBox Website JavaScript

// Sticky header on scroll
window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Mobile menu toggle
function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            // Close mobile menu if open
            document.querySelector('.nav-links').classList.remove('active');
        }
    });
});

// FAQ toggle
function toggleFAQ(element) {
    element.classList.toggle('active');
}

// Scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

// Zip code checker
function checkZip() {
    const zipInput = document.getElementById('zipInput');
    const zipResult = document.getElementById('zipResult');
    const zip = zipInput.value.trim();

    // Validate zip code format
    if (!/^\d{5}$/.test(zip)) {
        zipResult.className = 'error';
        zipResult.textContent = 'Please enter a valid 5-digit zip code.';
        return;
    }

    // Load service areas from Jekyll data
    fetch('/content/service-areas.json')
        .then(response => response.json())
        .then(data => {
            const serviceZips = data.zip_codes || [];
            const isServed = serviceZips.some(item => item.zip === zip);

            if (isServed) {
                zipResult.className = 'success';
                zipResult.innerHTML = '🎉 Great news! We service your area.<br><a href="#signup" style="color: inherit; font-weight: bold;">Sign up now!</a>';
            } else {
                zipResult.className = 'error';
                zipResult.innerHTML = 'Sorry, we don\'t service this area yet.<br>Join our waitlist to be notified when we expand!';
            }
        })
        .catch(error => {
            console.error('Error loading service areas:', error);
            zipResult.className = 'error';
            zipResult.textContent = 'Unable to check availability. Please try again.';
        });
}

// Allow Enter key to submit zip code
document.getElementById('zipInput')?.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        checkZip();
    }
});

// Form submission handler
function handleSignup(event) {
    event.preventDefault();

    // Get form data
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    console.log('Form submitted:', data);

    // Here you would normally send to a backend
    // For now, show success message
    alert('Thank you for signing up! We\'ll contact you shortly to confirm your first delivery.');

    // Reset form
    event.target.reset();

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('SwapBox website loaded successfully!');
});
