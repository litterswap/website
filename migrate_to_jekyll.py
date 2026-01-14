#!/usr/bin/env python3
"""
SwapBox Website - Jekyll Migration Script
This script creates all necessary Jekyll files and populates content collections
"""

import os
import json
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

def create_directory(path):
    """Create directory if it doesn't exist"""
    Path(path).mkdir(parents=True, exist_ok=True)
    print(f"✓ Created directory: {path}")

def write_file(path, content):
    """Write content to file"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Created file: {path}")

def write_json(path, data):
    """Write JSON data to file"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"✓ Created JSON: {path}")

def create_config_yml():
    """Create Jekyll _config.yml"""
    config = """# SwapBox Jekyll Configuration
title: SwapBox
description: Never Scoop Cat Litter Again - Weekly SwapBox delivery service
baseurl: "" # Leave empty for GitHub Pages on username.github.io/repo
url: "https://litterswap.github.io" # Change to your GitHub Pages URL

# Collections - point to content directory
collections_dir: content
collections:
  steps:
    output: false
  features:
    output: false
  pricing:
    output: false
  benefits:
    output: false
  faq:
    output: false
  testimonials:
    output: false

# Defaults
defaults:
  - scope:
      path: ""
    values:
      layout: "default"

# Build settings
markdown: kramdown
plugins:
  - jekyll-feed
  - jekyll-seo-tag

# Exclude from build
exclude:
  - Gemfile
  - Gemfile.lock
  - node_modules
  - vendor
  - migrate_to_jekyll.py
  - README.md
  - admin/
"""
    write_file(BASE_DIR / '_config.yml', config)

def create_gemfile():
    """Create Gemfile for Jekyll"""
    gemfile = """source "https://rubygems.org"

gem "jekyll", "~> 4.3"
gem "webrick", "~> 1.7"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
end
"""
    write_file(BASE_DIR / 'Gemfile', gemfile)

def create_layouts():
    """Create _layouts/default.html"""
    create_directory(BASE_DIR / '_layouts')

    layout = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title | default: site.title }}</title>
    <meta name="description" content="{{ page.description | default: site.description }}">

    <!-- SEO -->
    {% seo %}

    <!-- Favicon -->
    <link rel="icon" href="{{ '/images/favicon.ico' | relative_url }}" type="image/x-icon">

    <!-- CSS -->
    <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    {{ content }}

    <!-- JavaScript -->
    <script src="{{ '/assets/js/main.js' | relative_url }}"></script>
</body>
</html>
"""
    write_file(BASE_DIR / '_layouts' / 'default.html', layout)

def create_css():
    """Create CSS file"""
    create_directory(BASE_DIR / 'assets' / 'css')

    css = """/* SwapBox Website Styles */
:root {
    --primary: #10B981;
    --primary-dark: #059669;
    --secondary: #3B82F6;
    --accent: #8B5CF6;
    --text-dark: #1F2937;
    --text-light: #6B7280;
    --bg-light: #F9FAFB;
    --bg-white: #FFFFFF;
    --border: #E5E7EB;
    --success: #10B981;
    --warning: #F59E0B;
    --error: #EF4444;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    color: var(--text-dark);
    line-height: 1.6;
    background: var(--bg-white);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
}

/* Navigation */
header {
    position: sticky;
    top: 0;
    background: var(--bg-white);
    border-bottom: 1px solid var(--border);
    z-index: 1000;
    transition: box-shadow 0.3s ease;
}

header.scrolled {
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary);
}

.nav-links {
    display: flex;
    list-style: none;
    gap: 2rem;
    align-items: center;
}

.nav-links a {
    text-decoration: none;
    color: var(--text-dark);
    font-weight: 500;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: var(--primary);
}

.mobile-menu {
    display: none;
    flex-direction: column;
    gap: 5px;
    cursor: pointer;
}

.mobile-menu span {
    width: 25px;
    height: 3px;
    background: var(--text-dark);
    transition: 0.3s;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    color: white;
    padding: 6rem 2rem;
    text-align: center;
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
}

.hero h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}

.hero p {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    opacity: 0.95;
}

.hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

/* Buttons */
.cta-primary, .cta-secondary, .cta-button, .submit-button {
    padding: 0.875rem 2rem;
    border-radius: 0.5rem;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
    font-size: 1rem;
}

.cta-primary, .submit-button {
    background: var(--bg-white);
    color: var(--primary);
}

.cta-primary:hover, .submit-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.cta-secondary {
    background: rgba(255,255,255,0.1);
    color: white;
    border: 2px solid white;
}

.cta-secondary:hover {
    background: rgba(255,255,255,0.2);
}

.cta-button {
    background: var(--primary);
    color: white;
}

.cta-button:hover {
    background: var(--primary-dark);
}

/* Section Styles */
section {
    padding: 5rem 2rem;
}

.section-title {
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 1rem;
    color: var(--text-dark);
}

.section-subtitle {
    font-size: 1.125rem;
    text-align: center;
    color: var(--text-light);
    margin-bottom: 3rem;
}

/* How It Works */
.steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    max-width: 1000px;
    margin: 0 auto;
}

.step {
    text-align: center;
    padding: 2rem;
    background: var(--bg-light);
    border-radius: 1rem;
    transition: transform 0.3s ease;
}

.step:hover {
    transform: translateY(-5px);
}

.step-number {
    width: 60px;
    height: 60px;
    background: var(--primary);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0 auto 1rem;
}

.step h3 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
}

/* Features Grid */
.feature-grid, .benefits-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    max-width: 1100px;
    margin: 0 auto;
}

.feature-card, .benefit {
    padding: 2rem;
    background: white;
    border: 1px solid var(--border);
    border-radius: 1rem;
    text-align: center;
    transition: all 0.3s ease;
}

.feature-card:hover, .benefit:hover {
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    transform: translateY(-5px);
}

.feature-icon, .benefit-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.feature-card h3, .benefit h3 {
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
}

/* Pricing */
.pricing-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    max-width: 1100px;
    margin: 0 auto;
}

.pricing-card {
    background: white;
    border: 2px solid var(--border);
    border-radius: 1rem;
    padding: 2.5rem 2rem;
    text-align: center;
    position: relative;
    transition: all 0.3s ease;
}

.pricing-card:hover {
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    transform: translateY(-10px);
}

.pricing-card.featured {
    border-color: var(--primary);
    box-shadow: 0 10px 30px rgba(16, 185, 129, 0.2);
}

.featured-badge {
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--primary);
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 2rem;
    font-size: 0.875rem;
    font-weight: 600;
}

.plan-name {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.plan-price {
    font-size: 3rem;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 0.5rem;
}

.plan-period {
    color: var(--text-light);
    margin-bottom: 2rem;
}

.plan-features {
    list-style: none;
    margin-bottom: 2rem;
    text-align: left;
}

.plan-features li {
    padding: 0.75rem 0;
    border-bottom: 1px solid var(--bg-light);
}

.plan-features li:before {
    content: "✓ ";
    color: var(--primary);
    font-weight: 700;
    margin-right: 0.5rem;
}

/* FAQ */
.faq-list {
    max-width: 800px;
    margin: 0 auto;
}

.faq-item {
    background: white;
    border: 1px solid var(--border);
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.faq-item:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.faq-question {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem;
    font-weight: 600;
}

.faq-toggle {
    transition: transform 0.3s ease;
}

.faq-item.active .faq-toggle {
    transform: rotate(180deg);
}

.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
}

.faq-item.active .faq-answer {
    max-height: 500px;
}

.faq-answer p {
    padding: 0 1.5rem 1.5rem;
    color: var(--text-light);
}

/* Testimonials */
.testimonial-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    max-width: 1100px;
    margin: 0 auto;
}

.testimonial {
    background: white;
    border: 1px solid var(--border);
    border-radius: 1rem;
    padding: 2rem;
}

.stars {
    color: #FFC107;
    font-size: 1.25rem;
    margin-bottom: 1rem;
}

.testimonial-text {
    font-style: italic;
    color: var(--text-dark);
    margin-bottom: 1.5rem;
    line-height: 1.7;
}

.testimonial-author {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.author-avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: var(--primary);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
}

.author-avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

.author-info h4 {
    margin-bottom: 0.25rem;
}

.author-info p {
    color: var(--text-light);
    font-size: 0.875rem;
}

/* Sign Up Form */
.signup {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
}

.signup-form {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 2.5rem;
    border-radius: 1rem;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: var(--text-dark);
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 0.875rem;
    border: 1px solid var(--border);
    border-radius: 0.5rem;
    font-size: 1rem;
    font-family: inherit;
    transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary);
}

.submit-button {
    width: 100%;
    background: var(--primary);
    color: white;
}

/* Zip Checker */
.zip-checker {
    max-width: 500px;
    margin: 0 auto 2rem;
    display: flex;
    gap: 1rem;
}

.zip-checker input {
    flex: 1;
    padding: 0.875rem 1.25rem;
    border: 2px solid var(--border);
    border-radius: 0.5rem;
    font-size: 1rem;
}

.zip-checker button {
    padding: 0.875rem 2rem;
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 0.5rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.3s ease;
}

.zip-checker button:hover {
    background: var(--primary-dark);
}

#zipResult {
    text-align: center;
    margin-top: 1rem;
    padding: 1rem;
    border-radius: 0.5rem;
}

#zipResult.success {
    background: #D1FAE5;
    color: #065F46;
}

#zipResult.error {
    background: #FEE2E2;
    color: #991B1B;
}

/* Footer */
footer {
    background: var(--text-dark);
    color: white;
    padding: 4rem 2rem 2rem;
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 3rem;
    max-width: 1200px;
    margin: 0 auto 3rem;
}

.footer-section h3 {
    margin-bottom: 1.5rem;
    color: var(--primary);
}

.footer-section ul {
    list-style: none;
}

.footer-section ul li {
    margin-bottom: 0.75rem;
}

.footer-section a {
    color: rgba(255,255,255,0.8);
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-section a:hover {
    color: var(--primary);
}

.footer-bottom {
    text-align: center;
    padding-top: 2rem;
    border-top: 1px solid rgba(255,255,255,0.1);
    color: rgba(255,255,255,0.7);
}

/* Animations */
.fade-in {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.6s ease, transform 0.6s ease;
}

.fade-in.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Responsive */
@media (max-width: 768px) {
    .nav-links {
        position: fixed;
        top: 70px;
        left: -100%;
        flex-direction: column;
        background: white;
        width: 100%;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: left 0.3s ease;
    }

    .nav-links.active {
        left: 0;
    }

    .mobile-menu {
        display: flex;
    }

    .hero h1 {
        font-size: 2rem;
    }

    .hero p {
        font-size: 1rem;
    }

    .section-title {
        font-size: 2rem;
    }

    .hero-buttons {
        flex-direction: column;
    }

    .zip-checker {
        flex-direction: column;
    }
}
"""
    write_file(BASE_DIR / 'assets' / 'css' / 'style.css', css)

def create_js():
    """Create JavaScript file"""
    create_directory(BASE_DIR / 'assets' / 'js')

    js = """// SwapBox Website JavaScript

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
    if (!/^\\d{5}$/.test(zip)) {
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
                zipResult.innerHTML = 'Sorry, we don\\'t service this area yet.<br>Join our waitlist to be notified when we expand!';
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
    alert('Thank you for signing up! We\\'ll contact you shortly to confirm your first delivery.');

    // Reset form
    event.target.reset();

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('SwapBox website loaded successfully!');
});
"""
    write_file(BASE_DIR / 'assets' / 'js' / 'main.js', js)

def create_sample_content():
    """Create sample content for all collections"""

    # Create content directories
    dirs = ['content/_steps', 'content/_features', 'content/_pricing',
            'content/_benefits', 'content/_faq', 'content/_testimonials',
            'content/_data/settings']

    for d in dirs:
        create_directory(BASE_DIR / d)

    # Hero content
    hero_data = {
        "headline": "Never Scoop Cat Litter Again",
        "subheadline": "Weekly SwapBox delivery with fresh litter boxes and premium litter. We pick up, you relax. Zero effort, zero odor.",
        "primary_cta": "Start Free Trial",
        "secondary_cta": "See How It Works"
    }
    write_json(BASE_DIR / 'content' / 'hero.json', hero_data)

    # Steps
    steps = [
        {
            "step_number": 1,
            "title": "We Deliver Your SwapBox",
            "description": "Receive your first SwapBox with 7 clean litter boxes and 7 bags of fresh, premium litter.",
            "icon": "📦"
        },
        {
            "step_number": 2,
            "title": "Your Cat Uses Fresh Litter Daily",
            "description": "Simply swap out the litter box each day. Drop the used one back in the SwapBox—no scooping needed!",
            "icon": "🐱"
        },
        {
            "step_number": 3,
            "title": "Leave It Outside on Pickup Day",
            "description": "Get a text reminder 1-2 days before. Just leave your SwapBox outside—we'll grab it, no need to be home.",
            "icon": "🚪"
        },
        {
            "step_number": 4,
            "title": "We Swap with a Fresh SwapBox",
            "description": "We take the old, leave the new. Repeat weekly. It's that simple!",
            "icon": "🔄"
        }
    ]

    for step in steps:
        filename = f"step-{step['step_number']}.json"
        write_json(BASE_DIR / 'content' / '_steps' / filename, step)

    # Features
    features = [
        {
            "title": "Odor-Sealing Design",
            "description": "Heavy-duty Sterilite 40-gallon wheeled tote keeps odors completely contained.",
            "icon": "🛡️",
            "order": 1
        },
        {
            "title": "Easy to Use",
            "description": "Large wheels for easy transport. No heavy lifting required.",
            "icon": "✨",
            "order": 2
        },
        {
            "title": "Durable & Reusable",
            "description": "Industrial-grade materials designed for years of weekly swaps.",
            "icon": "♻️",
            "order": 3
        },
        {
            "title": "Perfect for Travel",
            "description": "Leave your cats alone for up to 7 days with daily fresh litter boxes ready to go.",
            "icon": "✈️",
            "order": 4
        }
    ]

    for i, feature in enumerate(features):
        filename = f"feature-{i+1}.json"
        write_json(BASE_DIR / 'content' / '_features' / filename, feature)

    # Pricing
    pricing = [
        {
            "name": "Single Cat",
            "price": 35,
            "period": "per week",
            "featured": False,
            "features": [
                "1 SwapBox delivered weekly",
                "7 disposable litter boxes with lids",
                "7 bags (8lb each) of premium litter",
                "Weekly pickup & disposal",
                "Text reminders",
                "Cancel anytime"
            ],
            "order": 1
        },
        {
            "name": "Multi-Cat",
            "price": 45,
            "period": "per week",
            "featured": True,
            "badge": "Most Popular",
            "features": [
                "1 SwapBox delivered weekly",
                "14 disposable litter boxes with lids",
                "14 bags (8lb each) of premium litter",
                "Weekly pickup & disposal",
                "Perfect for 2-3 cats",
                "Text reminders",
                "Cancel anytime"
            ],
            "order": 2
        },
        {
            "name": "Cat Colony",
            "price": 65,
            "period": "per week",
            "featured": False,
            "features": [
                "2 SwapBoxes delivered weekly",
                "21+ disposable litter boxes",
                "21+ bags of premium litter",
                "Weekly pickup & disposal",
                "Perfect for 4+ cats",
                "Priority scheduling",
                "Text reminders",
                "Cancel anytime"
            ],
            "order": 3
        }
    ]

    for i, plan in enumerate(pricing):
        filename = f"{plan['name'].lower().replace(' ', '-')}.json"
        write_json(BASE_DIR / 'content' / '_pricing' / filename, plan)

    # Benefits
    benefits = [
        {
            "title": "Completely Odor-Free Home",
            "description": "No stinky garbage cans or litter smell in your house. Everything sealed and removed weekly.",
            "icon": "😌",
            "order": 1
        },
        {
            "title": "Never Clean a Litter Box",
            "description": "No more scrubbing boxes or scooping clumps. Just swap and go!",
            "icon": "🚫",
            "order": 2
        },
        {
            "title": "No More Store Trips",
            "description": "Stop lugging heavy litter bags and plastic boxes. We bring everything to you.",
            "icon": "🏠",
            "order": 3
        },
        {
            "title": "Eco-Conscious Disposal",
            "description": "We handle all waste responsibly. All containers are reused—zero landfill waste from packaging.",
            "icon": "🌱",
            "order": 4
        },
        {
            "title": "Dust-Free Environment",
            "description": "Premium low-dust litter and no pouring from bags means cleaner air for you and your cats.",
            "icon": "💨",
            "order": 5
        },
        {
            "title": "Perfect for Vacations",
            "description": "Leave 7 fresh boxes out and your cats are set for a week. No pet sitter needed for litter duty!",
            "icon": "🏖️",
            "order": 6
        }
    ]

    for i, benefit in enumerate(benefits):
        filename = f"benefit-{i+1}.json"
        write_json(BASE_DIR / 'content' / '_benefits' / filename, benefit)

    # FAQ
    faqs = [
        {
            "question": "What if I miss pickup day?",
            "answer": "No worries! We send text reminders 1-2 days before pickup. If you miss it, contact us and we'll reschedule at no extra charge.",
            "order": 1
        },
        {
            "question": "What type of litter is used?",
            "answer": "We use premium clumping, lightly scented clay litter that's veterinarian-approved and safe for all cats.",
            "order": 2
        },
        {
            "question": "How big are the SwapBoxes?",
            "answer": "We use Sterilite 40-gallon wheeled industrial totes. They're approximately 32\" long x 19\" wide x 17\" tall—plenty of room for a week's worth of litter boxes.",
            "order": 3
        },
        {
            "question": "What if I have multiple cats?",
            "answer": "Simply upgrade to our Multi-Cat plan or add additional SwapBoxes. Each box contains enough for 7 daily litter changes.",
            "order": 4
        },
        {
            "question": "Where do I leave the bin?",
            "answer": "Anywhere outside your home that's accessible—front porch, side of house, driveway, garage, etc. Just let us know your preferred spot during signup.",
            "order": 5
        },
        {
            "question": "Can I cancel anytime?",
            "answer": "Absolutely! There's no long-term contract. Cancel anytime with one week's notice.",
            "order": 6
        },
        {
            "question": "What happens to the used litter?",
            "answer": "We dispose of it responsibly at licensed facilities. All our SwapBoxes and litter boxes are reused to minimize environmental impact.",
            "order": 7
        },
        {
            "question": "Do I need to be home for pickup/delivery?",
            "answer": "Nope! That's the beauty of SwapBox. Just leave your full box outside and we'll swap it with a fresh one. You don't need to be home at all.",
            "order": 8
        }
    ]

    for i, faq in enumerate(faqs):
        filename = f"faq-{i+1}.json"
        write_json(BASE_DIR / 'content' / '_faq' / filename, faq)

    # Testimonials
    testimonials = [
        {
            "name": "Sarah Johnson",
            "role": "Cat mom of 2",
            "text": "SwapBox has been a game changer! I used to dread cleaning litter boxes every day. Now I just swap them out and forget about it. My house smells fresh and I have so much more free time.",
            "rating": 5,
            "initials": "SJ",
            "order": 1
        },
        {
            "name": "Michael Chen",
            "role": "Busy professional with 3 cats",
            "text": "As someone who travels for work, SwapBox is perfect. I can leave for a week knowing my cats have fresh litter every day. No more expensive pet sitters just for litter box duty!",
            "rating": 5,
            "initials": "MC",
            "order": 2
        },
        {
            "name": "Emily Rodriguez",
            "role": "Senior cat owner",
            "text": "I'm 72 and lifting heavy litter bags was getting difficult. SwapBox delivers everything and takes it all away. It's given me independence and kept my home odor-free. Highly recommend!",
            "rating": 5,
            "initials": "ER",
            "order": 3
        }
    ]

    for i, testimonial in enumerate(testimonials):
        filename = f"testimonial-{i+1}.json"
        write_json(BASE_DIR / 'content' / '_testimonials' / filename, testimonial)

    # Service areas
    service_areas = {
        "zip_codes": [
            {"zip": "94102"},
            {"zip": "94103"},
            {"zip": "94104"},
            {"zip": "94105"},
            {"zip": "94107"},
            {"zip": "94108"},
            {"zip": "94109"},
            {"zip": "94110"},
            {"zip": "94111"},
            {"zip": "94112"}
        ]
    }
    write_json(BASE_DIR / 'content' / 'service-areas.json', service_areas)

    # Signup form
    signup_form = {
        "title": "Ready to Never Scoop Again?",
        "subtitle": "Start your free trial today. No credit card required for first week.",
        "button_text": "Start Free Trial",
        "success_message": "Thank you for signing up! We'll contact you within 24 hours to schedule your first delivery.",
        "action_url": "",
        "show_trial": True
    }
    write_json(BASE_DIR / 'content' / 'signup-form.json', signup_form)

    # General settings
    settings = {
        "site_title": "SwapBox",
        "tagline": "The easiest way to manage your cat's litter. Never scoop again with our weekly exchange service.",
        "phone": "(555) 123-4567",
        "email": "hello@swapbox.com",
        "facebook": "https://facebook.com/swapbox",
        "instagram": "https://instagram.com/swapbox",
        "twitter": "https://twitter.com/swapbox"
    }
    write_json(BASE_DIR / 'content' / '_data' / 'settings' / 'general.json', settings)

def create_data_symlinks():
    """Create symlinks so Jekyll can find the data files"""
    create_directory(BASE_DIR / '_data')
    create_directory(BASE_DIR / '_data' / 'settings')

    # Create symlink for hero data
    hero_src = BASE_DIR / 'content' / 'hero.json'
    hero_dest = BASE_DIR / '_data' / 'hero.json'
    if hero_src.exists() and not hero_dest.exists():
        try:
            os.symlink(hero_src, hero_dest)
            print(f"✓ Created symlink: {hero_dest}")
        except:
            # If symlink fails (Windows), copy the file instead
            import shutil
            shutil.copy(hero_src, hero_dest)
            print(f"✓ Copied file: {hero_dest}")

    # Create symlink for signup-form data
    signup_src = BASE_DIR / 'content' / 'signup-form.json'
    signup_dest = BASE_DIR / '_data' / 'signup-form.json'
    if signup_src.exists() and not signup_dest.exists():
        try:
            os.symlink(signup_src, signup_dest)
            print(f"✓ Created symlink: {signup_dest}")
        except:
            import shutil
            shutil.copy(signup_src, signup_dest)
            print(f"✓ Copied file: {signup_dest}")

    # Create symlink for settings
    settings_src = BASE_DIR / 'content' / '_data' / 'settings' / 'general.json'
    settings_dest = BASE_DIR / '_data' / 'settings' / 'general.json'
    if settings_src.exists() and not settings_dest.exists():
        try:
            os.symlink(settings_src, settings_dest)
            print(f"✓ Created symlink: {settings_dest}")
        except:
            import shutil
            shutil.copy(settings_src, settings_dest)
            print(f"✓ Copied file: {settings_dest}")

def create_readme():
    """Create an updated README"""
    readme = """# SwapBox Website

A Jekyll-powered website with Netlify CMS for easy content management.

## Quick Start

### 1. Install Jekyll

```bash
# Install Ruby (if not installed)
# On Mac:
brew install ruby

# On Ubuntu/Debian:
sudo apt-get install ruby-full

# Install Jekyll and Bundler
gem install jekyll bundler
```

### 2. Install Dependencies

```bash
bundle install
```

### 3. Run Locally

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` to see your site.

### 4. Access CMS Locally

While Jekyll is running, visit `http://localhost:4000/admin` to access the CMS.

## Deploying to GitHub Pages

### Push to GitHub

```bash
git add .
git commit -m "Complete Jekyll migration with CMS"
git push origin main
```

### Enable GitHub Pages

1. Go to your repository settings
2. Click "Pages" in the sidebar
3. Under "Source", select "main" branch
4. Click "Save"

Your site will be live at `https://litterswap.github.io/website/`

## Setting Up CMS for Your Client

### 1. Deploy to Netlify (Free)

1. Go to [netlify.com](https://netlify.com) and sign up
2. Click "Add new site" → "Import an existing project"
3. Connect to your GitHub repository
4. Deploy settings:
   - Build command: `jekyll build`
   - Publish directory: `_site`
5. Click "Deploy site"

### 2. Enable Netlify Identity

1. In your Netlify site dashboard, go to "Identity"
2. Click "Enable Identity"
3. Under "Registration preferences", select "Invite only"
4. Under "Services" → "Git Gateway", click "Enable Git Gateway"

### 3. Invite Your Client

1. In Netlify Identity, click "Invite users"
2. Enter your client's email
3. They'll receive an invitation to set up their account

### 4. Your Client Can Now Edit

They can visit `https://your-site.netlify.app/admin` and log in to edit all content!

## Content Structure

All content is stored in `/content/` as JSON files:

- `/content/_steps/` - How It Works steps
- `/content/_features/` - SwapBox features
- `/content/_pricing/` - Pricing plans
- `/content/_benefits/` - Why Choose Us benefits
- `/content/_faq/` - FAQ items
- `/content/_testimonials/` - Customer testimonials
- `/content/hero.json` - Hero section content
- `/content/signup-form.json` - Sign up form settings
- `/content/service-areas.json` - Service zip codes
- `/content/_data/settings/general.json` - Site-wide settings

## Customization

### Update Styles

Edit `assets/css/style.css`

### Update JavaScript

Edit `assets/js/main.js`

### Update Layout

Edit `_layouts/default.html`

### Update CMS Configuration

Edit `admin/config.yml`

## Troubleshooting

### Jekyll won't build

```bash
bundle update
bundle exec jekyll build --verbose
```

### CSS/JS not loading

Check that paths in `_layouts/default.html` use `relative_url` filter:

```liquid
{{ '/assets/css/style.css' | relative_url }}
```

### CMS not loading content

1. Check that files exist in `/content/` directories
2. Verify `admin/config.yml` paths match actual file locations
3. Clear browser cache and reload

## Support

For issues or questions:
- Check the [Jekyll docs](https://jekyllrb.com/docs/)
- Check the [Netlify CMS docs](https://decapcms.org/docs/)
- Review `admin/config.yml` for CMS configuration

---

Made with ❤️ for cat lovers
"""
    write_file(BASE_DIR / 'README-MIGRATION.md', readme)

def main():
    """Main migration function"""
    print("\n🚀 Starting Jekyll Migration for SwapBox Website\n")
    print("=" * 60)

    print("\n📝 Creating Jekyll Configuration...")
    create_config_yml()
    create_gemfile()

    print("\n🎨 Creating Layouts...")
    create_layouts()

    print("\n💅 Creating CSS and JavaScript...")
    create_css()
    create_js()

    print("\n📦 Creating Sample Content...")
    create_sample_content()

    print("\n🔗 Creating Data Symlinks...")
    create_data_symlinks()

    print("\n📚 Creating README...")
    create_readme()

    print("\n" + "=" * 60)
    print("✅ Migration Complete!")
    print("\n🎉 Next Steps:")
    print("   1. Run: bundle install")
    print("   2. Run: bundle exec jekyll serve")
    print("   3. Visit: http://localhost:4000")
    print("   4. Access CMS: http://localhost:4000/admin")
    print("\n📖 See README-MIGRATION.md for detailed instructions")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
