# 🐱 SwapBox - Cat Litter Exchange Service Website

A modern, professional website for SwapBox - a weekly cat litter exchange service. Built with vanilla HTML, CSS, and JavaScript, optimized for GitHub Pages deployment.

## 🌟 Features

- **Fully Responsive Design** - Works perfectly on mobile, tablet, and desktop
- **Modern UI/UX** - Clean, professional design with smooth animations
- **Interactive Elements** - FAQ accordion, zip code checker, smooth scrolling
- **SEO Optimized** - Proper meta tags and semantic HTML
- **No Dependencies** - Pure HTML/CSS/JS, no frameworks required
- **GitHub Pages Ready** - Optimized for instant deployment

## 🚀 Quick Start - Deploy to GitHub Pages

### Option 1: Simple Deployment

1. **Create a new repository on GitHub**
   - Go to https://github.com/new
   - Name it `swapbox-website` (or any name you prefer)
   - Make it public
   - Don't initialize with README (we have one)

2. **Upload the files**
   - Click "uploading an existing file"
   - Drag and drop `index.html` and this `README.md`
   - Commit changes

3. **Enable GitHub Pages**
   - Go to repository Settings
   - Scroll to "Pages" section
   - Under "Source", select "main" branch
   - Click Save

4. **Your site is live!**
   - URL will be: `https://yourusername.github.io/swapbox-website`
   - May take 1-2 minutes to deploy

### Option 2: Using Git Command Line

```bash
# Clone or create new repository
git clone https://github.com/yourusername/swapbox-website.git
cd swapbox-website

# Add the files
cp /path/to/index.html .
cp /path/to/README.md .

# Commit and push
git add .
git commit -m "Initial commit - SwapBox website"
git push origin main

# Enable GitHub Pages in repository settings
```

## 📁 File Structure

```
swapbox-website/
├── index.html          # Main website file (all-in-one)
├── README.md          # This file
└── (optional folders)
    ├── images/        # Add your SwapBox images here
    ├── assets/        # Additional assets
    └── CNAME          # For custom domain
```

## 🎨 Customization Guide

### 1. Colors

Find and replace these CSS variables in the `<style>` section:

```css
:root {
    --primary: #2E7D32;        /* Main green */
    --primary-light: #4CAF50;  /* Light green */
    --secondary: #00ACC1;      /* Blue accent */
    --accent: #FF6F00;         /* Orange accent */
}
```

### 2. Add Your Logo

Replace the emoji logo in the header:

```html
<!-- Find this line -->
<div class="logo">🐱 SwapBox</div>

<!-- Replace with -->
<div class="logo">
    <img src="images/logo.png" alt="SwapBox" style="height: 40px;">
</div>
```

### 3. Add Real Images

Create an `images` folder and add SwapBox photos:

```html
<!-- In the hero section, add -->
<div class="hero-image">
    <img src="images/swapbox-hero.jpg" alt="SwapBox System">
</div>
```

### 4. Update Service Areas

In the JavaScript section, update the zip codes:

```javascript
// Find this line
const serviceZips = ['94102', '94103', '94104', '10001', '10002', '90001', '90002'];

// Replace with your actual service zip codes
const serviceZips = ['12345', '12346', '12347', /* ... */];
```

### 5. Connect Real Forms

Replace the form handler with your backend:

```javascript
function handleSignup(event) {
    event.preventDefault();
    
    // Get form data
    const formData = new FormData(event.target);
    
    // Send to your backend
    fetch('https://your-api.com/signup', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => {
        alert('Signup successful!');
        // Redirect to thank you page
    });
}
```

### 6. Add Analytics

Add before closing `</head>` tag:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🔧 Advanced Configuration

### Custom Domain

1. Buy a domain (e.g., `swapbox.com`)
2. Create a `CNAME` file in repository root:
   ```
   swapbox.com
   ```
3. Add DNS records at your domain registrar:
   - Type: `A` → Value: `185.199.108.153`
   - Type: `A` → Value: `185.199.109.153`
   - Type: `A` → Value: `185.199.110.153`
   - Type: `A` → Value: `185.199.111.153`
   - Type: `CNAME` → Name: `www` → Value: `yourusername.github.io`

4. In GitHub Pages settings, add your custom domain

### Add Contact Form Integration

**Using Formspree (Free):**

```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
    <!-- Your form fields -->
</form>
```

**Using EmailJS (Free):**

1. Sign up at emailjs.com
2. Add before closing `</body>`:

```html
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
<script>
    emailjs.init("YOUR_PUBLIC_KEY");
    
    function handleSignup(event) {
        event.preventDefault();
        emailjs.sendForm('service_id', 'template_id', event.target)
            .then(() => alert('Signup successful!'));
    }
</script>
```

### Enable HTTPS

GitHub Pages automatically provides HTTPS. To enforce it:
1. Go to repository Settings
2. Scroll to GitHub Pages
3. Check "Enforce HTTPS"

## 📱 Testing

### Local Testing

Simply double-click `index.html` or:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx http-server

# Then visit http://localhost:8000
```

### Mobile Testing

- Use Chrome DevTools (F12 → Toggle device toolbar)
- Test on actual devices
- Use https://www.browserstack.com for cross-browser testing

## 🎯 SEO Optimization

### Add Favicon

Create a `favicon.ico` and add to `<head>`:

```html
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
```

### Improve Meta Tags

```html
<meta name="description" content="SwapBox - Weekly cat litter exchange service. Never scoop again! Fresh litter delivered, used boxes picked up.">
<meta name="keywords" content="cat litter, litter box service, pet care, cat care">
<meta property="og:title" content="SwapBox - Never Scoop Cat Litter Again">
<meta property="og:description" content="Weekly cat litter exchange service. Fresh litter delivered to your door.">
<meta property="og:image" content="https://yoursite.com/images/og-image.jpg">
<meta property="og:url" content="https://yoursite.com">
<meta name="twitter:card" content="summary_large_image">
```

### Create sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://yoursite.com/</loc>
    <lastmod>2026-01-14</lastmod>
    <priority>1.0</priority>
  </url>
</urlset>
```

### Add robots.txt

```
User-agent: *
Allow: /
Sitemap: https://yoursite.com/sitemap.xml
```

## 🔌 Integration Ideas

### Payment Processing

- **Stripe**: Best for subscriptions - https://stripe.com
- **PayPal**: Alternative option - https://paypal.com
- **Square**: Good for service businesses - https://squareup.com

### Email Marketing

- **Mailchimp**: Free tier available
- **ConvertKit**: Great for creators
- **SendGrid**: Good for transactional emails

### Customer Management

- **Airtable**: Simple database/CRM
- **Google Sheets**: Free and easy
- **HubSpot**: Full CRM solution

### Scheduling/Logistics

- **Calendly**: Appointment scheduling
- **Route4Me**: Route optimization
- **Google Calendar API**: Custom scheduling

## 📊 Analytics & Tracking

Add these tools to track performance:

1. **Google Analytics** - User behavior
2. **Hotjar** - Heatmaps and recordings
3. **Facebook Pixel** - Ad tracking
4. **Google Search Console** - SEO insights

## 🐛 Troubleshooting

### Site Not Showing Up

- Wait 2-5 minutes after enabling Pages
- Check GitHub Pages settings
- Ensure `index.html` is in root directory
- Check repository is public

### Styles Not Loading

- Clear browser cache
- Check browser console for errors
- Ensure all code is in single `index.html`

### Mobile Menu Not Working

- Check JavaScript is enabled
- Test in different browsers
- Check console for errors

## 📝 Content Updates

### Update Pricing

Find the pricing section and modify:

```html
<div class="plan-price">$29</div>
```

### Update Testimonials

Add/edit testimonials in the testimonials section:

```html
<div class="testimonial fade-in">
    <div class="stars">★★★★★</div>
    <p class="testimonial-text">"Your review here..."</p>
    <div class="testimonial-author">
        <div class="author-avatar">AB</div>
        <div class="author-info">
            <h4>Author Name</h4>
            <p>Cat parent of X</p>
        </div>
    </div>
</div>
```

### Update FAQ

Add new questions:

```html
<div class="faq-item" onclick="toggleFAQ(this)">
    <div class="faq-question">
        <span>Your question here?</span>
        <span class="faq-toggle">▼</span>
    </div>
    <div class="faq-answer">
        <p>Your answer here.</p>
    </div>
</div>
```

## 🚀 Performance Optimization

### Image Optimization

1. Use WebP format for images
2. Compress images (use TinyPNG.com)
3. Add lazy loading:

```html
<img src="image.jpg" loading="lazy" alt="Description">
```

### Minify Code

For production, minify HTML/CSS/JS:
- https://www.minifier.org/
- Or use build tools (optional)

## 📞 Support & Resources

- **GitHub Pages Docs**: https://docs.github.com/pages
- **HTML/CSS Reference**: https://developer.mozilla.org/
- **Web Design Inspiration**: https://dribbble.com
- **Free Images**: https://unsplash.com

## 📄 License

This template is free to use for your SwapBox business. No attribution required.

## 🤝 Contributing

To improve this template:
1. Fork the repository
2. Make your changes
3. Submit a pull request

## 📧 Questions?

If you need help with deployment or customization, feel free to open an issue on GitHub.

---

**Built with ❤️ for SwapBox**

Ready to launch your cat litter revolution! 🚀🐱
