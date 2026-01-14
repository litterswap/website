# Admin Page Blank - Troubleshooting Guide

## Issue: Admin page loads but shows empty/blank page

**URL:** https://delitterup.netlify.app/admin/#/
**Status:** Page loads (not 404) but CMS interface doesn't appear

## Most Common Cause: GitHub OAuth Not Enabled

The Decap CMS **requires** GitHub OAuth to be enabled in Netlify. Without it, the page will load but stay completely blank.

### ✅ Solution: Enable GitHub OAuth in Netlify

**Step-by-Step:**

1. **Go to Netlify Dashboard**
   - Visit: https://app.netlify.com
   - Select your "delitterup" site

2. **Navigate to OAuth Settings**
   - Click "Site settings" (in top nav)
   - Scroll down to find "Access control" section
   - Click "OAuth" (or "Authentication providers")

3. **Install GitHub Provider**
   - Look for "Install provider" button or "Install authentication providers"
   - Click it
   - Select "GitHub" from the list
   - Click "Install" or "Add provider"

4. **Authorize Netlify**
   - You'll be redirected to GitHub
   - Click "Authorize Netlify"
   - You'll be redirected back to Netlify
   - OAuth should now show as "Installed" or "Active"

5. **Test the Admin Page**
   - Visit: https://delitterup.netlify.app/admin
   - You should now see **"Login with GitHub"** button
   - Page should NO LONGER be blank!

### Expected Results

**Before OAuth enabled:**
- Blank white page
- No interface visible
- Console may show auth errors

**After OAuth enabled:**
- "Login with GitHub" button appears
- CMS branding/interface visible
- Can click to authenticate

## Other Possible Causes

### 1. JavaScript Console Errors

**How to check:**
1. Press F12 (or Cmd+Option+I on Mac)
2. Click "Console" tab
3. Refresh the admin page
4. Look for red error messages

**Common errors:**

**Error: "Failed to load config.yml"**
- Solution: Check that `admin/config.yml` exists in your repo
- Verify it's not excluded from build
- Check YAML syntax is valid

**Error: "Error loading the CMS configuration"**
- Solution: YAML syntax error in config.yml
- Use https://www.yamllint.com to validate

**Error: "repo not found" or "API rate limit"**
- Solution: Check repo name in config.yml matches: `litterswap/website`
- Verify repository exists and is accessible

**Error: "Cannot read property ... of undefined"**
- Solution: OAuth is not enabled (go back to step above)

### 2. CDN Loading Issue

**Check if Decap CMS JavaScript loaded:**

In browser console, type:
```javascript
typeof CMS
```

**If it returns "undefined":**
- Decap CMS JavaScript didn't load from CDN
- Check your internet connection
- Try hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

**If it returns "object":**
- CMS loaded successfully
- Issue is likely OAuth or config

### 3. Browser Cache

**Solution:**
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Or try in incognito/private browsing window
3. Or clear browser cache completely

### 4. Ad Blocker or Extension

Some browser extensions can interfere with the CMS.

**Solution:**
1. Disable ad blockers temporarily
2. Try in incognito mode (extensions usually disabled)
3. If it works in incognito, re-enable extensions one by one to find culprit

## Diagnostic Checklist

Work through this checklist:

- [ ] GitHub OAuth is enabled in Netlify
- [ ] Visiting /admin shows "Login with GitHub" button (not blank)
- [ ] No errors in browser console (F12 → Console)
- [ ] `admin/config.yml` exists in repository
- [ ] `admin/index.html` exists in repository
- [ ] Repo name in config matches: `litterswap/website`
- [ ] Branch name in config matches: `main`
- [ ] Tried hard refresh (Ctrl+Shift+R)
- [ ] Tried in incognito mode
- [ ] No ad blockers interfering

## Step-by-Step Debug Process

### 1. Open Browser Console (F12)

**Look for these specific errors:**

```
Error: Failed to load config
Error: API rate limit exceeded
Error: Not Found (repository)
Error: [object Object] (OAuth issue)
```

**Paste the full error here to diagnose**

### 2. Check Network Tab

1. Open Developer Tools (F12)
2. Click "Network" tab
3. Refresh page
4. Look for failed requests (red lines)

**Check these files loaded successfully:**
- `decap-cms.js` (should be 200 OK)
- `config.yml` (should be 200 OK)

If `config.yml` shows 404:
- It's not being built/published
- Check `_config.yml` doesn't exclude `admin/`

### 3. Test Config Syntax

Visit: https://www.yamllint.com

Paste your `admin/config.yml` content and validate.

**To get your config:**
```bash
cat admin/config.yml
```

Or view on GitHub:
https://github.com/litterswap/website/blob/main/admin/config.yml

### 4. Verify Files Deployed

Check if admin files are actually on Netlify:

Visit these URLs (replace with your domain):
- https://delitterup.netlify.app/admin/index.html (should load)
- https://delitterup.netlify.app/admin/config.yml (should download)

If either 404s:
- Files didn't get deployed
- Check `_config.yml` exclude list
- Trigger a new deploy

## What You Should See (Normal Behavior)

### Before Login
1. Visit `/admin`
2. See "Login with GitHub" button
3. CMS interface frame visible

### After Clicking Login
1. Redirected to GitHub
2. Authorize application
3. Redirected back to CMS
4. See collections in sidebar (Pricing, FAQ, etc.)

## Common Mistake: Wrong OAuth Setup

**Correct OAuth setup:**
- Service: GitHub
- Provider installed in: Netlify site settings
- Not: GitHub OAuth App (don't create one manually)
- Not: GitHub Personal Access Token

**Use Netlify's built-in OAuth provider** - it handles everything automatically.

## Still Blank After OAuth?

If you've enabled OAuth and it's still blank:

1. **Wait 2 minutes** after enabling OAuth (Netlify needs to propagate)

2. **Hard refresh** the page:
   - Ctrl+Shift+R (Windows/Linux)
   - Cmd+Shift+R (Mac)

3. **Check browser console** - paste any errors you see

4. **Try different browser** - to rule out browser-specific issues

5. **Verify OAuth is active**:
   - Go back to Netlify site settings
   - Check OAuth section shows "GitHub" as installed/active
   - If it shows "Not installed", install it again

## Success Indicators

You'll know it's working when you see:

✅ Page is **not blank** anymore
✅ "Login with GitHub" button appears
✅ Decap CMS logo/branding visible
✅ Can click login button and get redirected to GitHub
✅ After auth, see CMS interface with collections sidebar

## Need More Help?

If still having issues after trying everything above:

1. **Share browser console errors** - Screenshot or copy/paste
2. **Confirm OAuth is enabled** - Screenshot of Netlify OAuth settings
3. **Test these URLs**:
   - https://delitterup.netlify.app/admin/index.html
   - https://delitterup.netlify.app/admin/config.yml

---

**TL;DR: Enable GitHub OAuth in Netlify Site Settings → OAuth → Install GitHub Provider**

That's the #1 cause of blank admin pages!
