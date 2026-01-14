# Netlify Setup Guide - Fix Admin Portal

## Issues Fixed

✅ **Fixed folder paths in admin/config.yml** (was missing underscores)
✅ **Created netlify.toml** for proper Jekyll builds
✅ **Disabled local_backend** for production use

## 🚨 Critical: Enable Netlify Identity

The admin portal shows nothing because **Netlify Identity is not enabled yet**. This is REQUIRED for the CMS to work.

## Step-by-Step Setup

### 1. Enable Netlify Identity

1. **Go to your Netlify site dashboard**
   - URL: https://app.netlify.com
   - Select your SwapBox site

2. **Enable Identity**
   - Click "Identity" in the top navigation
   - Click the big "Enable Identity" button
   - Wait for it to activate (~10 seconds)

3. **Configure Registration**
   - Under "Identity" → "Settings and usage"
   - Find "Registration preferences"
   - Select **"Invite only"** (prevents random people from editing your site!)
   - Click "Save"

### 2. Enable Git Gateway

This allows the CMS to save changes back to GitHub:

1. **In the Identity section**
   - Scroll down to "Services"
   - Find "Git Gateway"
   - Click "Enable Git Gateway"
   - Confirm the authorization

### 3. Update Site URL in Config

1. **Find your Netlify site URL**
   - It will be something like: `https://swapbox-xyz123.netlify.app`
   - Or your custom domain if you set one up

2. **You're done!** The config files are already set up correctly.

### 4. Invite Your Client

1. **In Netlify Identity section**
   - Click "Invite users"
   - Enter your client's email address
   - Click "Send"

2. **They will receive an email**
   - Click the invitation link
   - Set their password
   - Done! They can now log in

### 5. Test the Admin Portal

1. **Visit your site's admin page**
   ```
   https://your-site.netlify.app/admin
   ```

2. **Log in**
   - Use the email you invited
   - Use the password you set

3. **You should now see the CMS interface!**
   - Collections on the left (Pricing, FAQ, etc.)
   - Content management in the center
   - Edit, add, delete content
   - Click "Publish" to save changes

## Troubleshooting

### Admin page still blank after enabling Identity

1. **Clear your browser cache**
   - Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
   - Or open in incognito/private window

2. **Check browser console for errors**
   - Press F12 to open developer tools
   - Check the "Console" tab
   - Look for error messages

3. **Verify Git Gateway is enabled**
   - Go back to Netlify Identity settings
   - Confirm Git Gateway shows as "Enabled"

### "Failed to load config" error

This means admin/config.yml has an error:

1. **Check YAML syntax**
   - Visit: https://www.yamllint.com
   - Paste your admin/config.yml content
   - Fix any syntax errors

2. **Verify folder paths exist**
   - All paths in config.yml should point to actual folders
   - Check that `content/_steps`, `content/_pricing`, etc. exist

### Site not building on Netlify

1. **Check build logs**
   - Go to "Deploys" tab in Netlify
   - Click on the latest deploy
   - Read the build log for errors

2. **Common issues:**
   - Ruby version mismatch (netlify.toml specifies 3.2.0)
   - Missing gems (should be fixed with netlify.toml)
   - Jekyll build errors (check _config.yml syntax)

### Jekyll showing raw Liquid tags

This means Jekyll isn't building. Check:

1. **Build command is correct**
   - Should be: `bundle install && bundle exec jekyll build`
   - Verify in Netlify site settings → Build & deploy

2. **Publish directory is correct**
   - Should be: `_site`
   - Verify in Netlify site settings

3. **netlify.toml is committed**
   - Run: `git status`
   - If not committed: `git add netlify.toml && git commit -m "Add Netlify config" && git push`

## What Each File Does

### `admin/config.yml`
- Configures what your client can edit
- Defines content collections (Pricing, FAQ, etc.)
- Specifies field types (text, number, image, etc.)
- Uses `git-gateway` backend (requires Netlify Identity)

### `netlify.toml`
- Tells Netlify how to build your Jekyll site
- Sets Ruby version (3.2.0)
- Configures build command
- Sets publish directory (_site)

### `admin/index.html`
- Loads the Decap CMS (formerly Netlify CMS) interface
- Provides the visual editor your client will use

## Comparison: GitHub Pages vs Netlify

| Feature | GitHub Pages | Netlify |
|---------|-------------|---------|
| **Static Hosting** | ✅ Free | ✅ Free |
| **Custom Domain** | ✅ Free | ✅ Free |
| **HTTPS/SSL** | ✅ Automatic | ✅ Automatic |
| **Jekyll Build** | ✅ Automatic | ✅ Automatic |
| **CMS Admin Portal** | ❌ Not available | ✅ **Yes! (with Identity)** |
| **Client Can Edit** | ❌ No | ✅ **Yes!** |
| **Git Gateway** | ❌ No | ✅ Yes |
| **Form Handling** | ❌ No | ✅ Yes (100/month free) |

**Recommendation:** Use **Netlify** for your production site so your client can edit content.

## Current Status After Fixes

✅ **Folder paths corrected** - CMS will now find content files
✅ **netlify.toml created** - Jekyll will build properly
✅ **local_backend disabled** - Won't interfere with production
✅ **Bundler updated** - Compatible with Ruby 3.4

**Next step:** Enable Netlify Identity (steps above) and the admin portal will work!

## Quick Checklist

Before the admin portal will work, you need:

- [ ] Netlify Identity enabled
- [ ] Git Gateway enabled
- [ ] At least one user invited
- [ ] User has accepted invitation and set password
- [ ] Git push the latest changes (with fixed admin/config.yml)
- [ ] Site has successfully built on Netlify
- [ ] Visit /admin and log in

Once all checkboxes are complete, the CMS will work perfectly!

## Need Help?

**Build failing?**
- Check deploy logs in Netlify dashboard
- Look for Ruby or Jekyll errors
- Verify netlify.toml is committed

**Admin portal blank?**
- Confirm Identity is enabled
- Confirm Git Gateway is enabled
- Clear browser cache
- Check browser console for errors

**Can't log in?**
- Make sure you accepted the invitation email
- Check spam folder for invitation
- Try "Forgot password" to reset

---

**Once Netlify Identity is enabled, your client will be able to:**
- Edit all content via visual interface at /admin
- Add/edit/delete pricing plans, FAQs, testimonials
- Upload images
- Change contact information
- Publish changes instantly
- Preview before publishing
- All without touching code!
