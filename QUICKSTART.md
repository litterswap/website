# DeLitterUp Website - Quick Start Guide

## ✅ Migration Complete!

Your DeLitterUp website has been successfully converted to Jekyll with Netlify CMS integration.

## 🚀 Running Locally

### Option 1: Using the Helper Script (Easiest)

```bash
./serve.sh
```

Then visit:
- **Website**: http://localhost:4000
- **CMS Admin**: http://localhost:4000/admin

### Option 2: Manual Commands

```bash
export GEM_HOME="$HOME/.gem"
export PATH="$HOME/.gem/bin:$PATH"
bundle exec jekyll serve --livereload
```

## 📁 Project Structure

```
website/
├── _config.yml           # Jekyll configuration
├── _layouts/             # Page layouts
│   └── default.html      # Main layout template
├── _data/                # Data files (symlinked from content/)
├── index.html            # Homepage (with Jekyll/Liquid tags)
├── content/              # All editable content (JSON files)
│   ├── _steps/           # "How It Works" steps
│   ├── _features/        # DeLitterUp features
│   ├── _pricing/         # Pricing plans
│   ├── _benefits/        # "Why Choose Us" benefits
│   ├── _faq/             # FAQ items
│   ├── _testimonials/    # Customer testimonials
│   ├── hero.json         # Hero section content
│   ├── signup-form.json  # Sign up form settings
│   ├── service-areas.json # Service zip codes
│   └── _data/settings/   # Site-wide settings
├── assets/
│   ├── css/style.css     # All website styles
│   └── js/main.js        # All JavaScript
├── admin/
│   ├── index.html        # CMS interface
│   └── config.yml        # CMS configuration
└── serve.sh              # Helper script to run locally

```

## 📝 Editing Content

### For You (Developer)

Edit JSON files in the `content/` directory:

```bash
# Edit hero section
vi content/hero.json

# Add a new FAQ
vi content/_faq/faq-9.json

# Update pricing
vi content/_pricing/single-cat.json
```

After editing, rebuild the site:
```bash
export GEM_HOME="$HOME/.gem" && export PATH="$HOME/.gem/bin:$PATH"
bundle exec jekyll build
```

### For Your Client (Non-Technical)

They'll use the CMS at `/admin`:

1. Visit http://localhost:4000/admin (locally) or https://yoursite.com/admin (production)
2. Log in with their Netlify Identity credentials
3. Click any section (Pricing, FAQ, Testimonials, etc.)
4. Edit, add, or delete items
5. Click "Publish" - changes go live automatically!

## 🌐 Deploying to Production

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Complete Jekyll migration with CMS"
git push origin main
```

### Step 2: Deploy to Netlify (Recommended for CMS)

**Why Netlify?** While your site currently works on GitHub Pages, Netlify provides:
- The authentication system for your CMS (Netlify Identity)
- Git Gateway for your client to save changes
- Form handling
- Continuous deployment
- Free SSL
- **Free plan available!**

**Setup Steps:**

1. **Sign up at Netlify**
   - Go to https://netlify.com
   - Sign up with your GitHub account

2. **Create New Site**
   - Click "Add new site" → "Import an existing project"
   - Choose GitHub and select your repository
   - Build settings:
     - Build command: `jekyll build`
     - Publish directory: `_site`
   - Click "Deploy site"

3. **Enable Netlify Identity** (Required for CMS)
   - In your site dashboard, go to "Identity"
   - Click "Enable Identity"
   - Under "Registration preferences", select "Invite only"
   - Click "Settings and usage"
   - Scroll to "Git Gateway" and click "Enable Git Gateway"

4. **Invite Your Client**
   - In Identity section, click "Invite users"
   - Enter your client's email address
   - They'll receive an invitation to create their account

5. **Update Your Site URL**
   - Edit `_config.yml` and update the `url` field:
     ```yaml
     url: "https://your-site-name.netlify.app"
     ```
   - Commit and push:
     ```bash
     git add _config.yml
     git commit -m "Update site URL"
     git push origin main
     ```

6. **Test the CMS**
   - Visit https://your-site-name.netlify.app/admin
   - Log in with the invited user credentials
   - Try editing some content
   - Click "Publish" - changes should appear on the live site!

### Alternative: Keep GitHub Pages (Limited CMS)

If you want to stay on GitHub Pages:

1. **Enable GitHub Pages**
   - Repository Settings → Pages
   - Source: main branch
   - Save

2. **CMS Limitations on GitHub Pages**
   - Your client will need a GitHub account
   - They'll need to commit directly to GitHub
   - No visual CMS interface without Netlify
   - **Recommendation**: Use Netlify for the best client experience

## 🎨 Customization

### Update Styles

Edit `assets/css/style.css`:

```css
:root {
    --primary: #10B981;  /* Change primary color */
    --secondary: #3B82F6; /* Change secondary color */
}
```

### Update Scripts

Edit `assets/js/main.js`

### Update Layout

Edit `_layouts/default.html`

### Update CMS Fields

Edit `admin/config.yml` to add/remove fields your client can edit.

## 🔧 Common Tasks

### Add a New Pricing Plan

1. Create a new file: `content/_pricing/new-plan.json`
2. Copy structure from existing plan:
   ```json
   {
     "name": "Enterprise",
     "price": 99,
     "period": "per week",
     "featured": false,
     "features": [
       "Feature 1",
       "Feature 2"
     ],
     "order": 4
   }
   ```
3. Rebuild site: `bundle exec jekyll build`

### Add Service Zip Codes

Edit `content/service-areas.json`:

```json
{
  "zip_codes": [
    {"zip": "94102"},
    {"zip": "94103"},
    {"zip": "10001"}
  ]
}
```

### Change Contact Information

Edit `content/_data/settings/general.json`:

```json
{
  "site_title": "DeLitterUp",
  "phone": "(555) 123-4567",
  "email": "hello@delitterup.com"
}
```

## 🐛 Troubleshooting

### "Command not found: bundle"

Run:
```bash
gem install bundler
```

### "Permission denied" errors

Use the GEM_HOME method:
```bash
export GEM_HOME="$HOME/.gem"
export PATH="$HOME/.gem/bin:$PATH"
```

Or add these lines to your `~/.bashrc` or `~/.zshrc` file.

### Site not updating after changes

1. Stop the server (Ctrl+C)
2. Delete `_site` folder: `rm -rf _site`
3. Rebuild: `bundle exec jekyll build`
4. Start server again: `./serve.sh`

### CMS not loading locally

1. Make sure Jekyll server is running
2. Visit http://localhost:4000/admin (not https)
3. For local testing, the CMS uses `local_backend: true` in `admin/config.yml`

### CSS/JS not loading

Check that `_config.yml` has the correct `baseurl`:
- For Netlify: `baseurl: ""`
- For GitHub Pages: `baseurl: "/repository-name"`

## 📚 Next Steps

1. ✅ Test the site locally: `./serve.sh`
2. ✅ Review all content in the CMS: http://localhost:4000/admin
3. ✅ Push to GitHub: `git push origin main`
4. ✅ Deploy to Netlify (recommended)
5. ✅ Invite your client to the CMS
6. ✅ Add real images to `/images/` directory
7. ✅ Update service zip codes
8. ✅ Connect a custom domain (optional)

## 🎉 Success!

Your website is now:
- ✅ Powered by Jekyll (fast, secure, version-controlled)
- ✅ Editable via CMS (your client can make changes)
- ✅ Fully responsive (works on all devices)
- ✅ SEO-ready (meta tags, sitemap, RSS feed)
- ✅ Production-ready (deploy anywhere)

## 📖 Resources

- **Jekyll Documentation**: https://jekyllrb.com/docs/
- **Netlify CMS Documentation**: https://decapcms.org/docs/
- **Netlify Deployment**: https://docs.netlify.com/

---

Need help? Check `README-MIGRATION.md` for detailed information.
