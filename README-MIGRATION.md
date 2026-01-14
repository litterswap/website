# SwapBox Website

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
