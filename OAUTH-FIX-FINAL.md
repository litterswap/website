# OAuth "Page Not Found" - Complete Fix Guide

## Current Problem

Clicking "Login with GitHub" redirects to an endpoint that returns 404:
- `https://delitterup.netlify.app/.netlify/functions/auth` → Not Found

## Root Cause

The OAuth endpoint doesn't exist, which means either:
1. GitHub OAuth provider is not properly installed in Netlify, OR
2. The configuration needs a different approach

## 🎯 Solution: Verify and Fix OAuth Setup

### Step 1: Check Current OAuth Status in Netlify

1. **Go to Netlify Dashboard**
   - https://app.netlify.com
   - Select your "delitterup" site

2. **Navigate to Site Settings**
   - Click "Site settings" in top navigation

3. **Find OAuth Section**
   - Look for "Access control" in the left sidebar
   - OR search for "OAuth" in the settings search

4. **Check What You See:**

**Scenario A: OAuth Section Shows GitHub as "Installed"**
- You should see "GitHub" listed
- Status should be "Active" or with a green checkmark
- If you see this, OAuth IS installed → proceed to Solution A below

**Scenario B: No OAuth Providers Listed or "Not Installed"**
- OAuth section is empty or shows "Install provider" button
- GitHub is not listed
- If you see this → proceed to Solution B below

---

## Solution A: OAuth IS Installed, Need to Fix Configuration

If OAuth shows as installed but still 404, the endpoint path might be different.

### Try These Configurations (One at a Time)

**Option 1: Remove base_url and auth_endpoint entirely**

Edit `admin/config.yml`:

```yaml
backend:
  name: github
  repo: litterswap/website
  branch: main
  # Remove base_url and auth_endpoint lines completely
```

**Why:** Netlify might automatically inject the OAuth endpoint when it detects the GitHub backend.

**Option 2: Use Netlify's auth gateway**

```yaml
backend:
  name: github
  repo: litterswap/website
  branch: main
  base_url: https://api.netlify.com
  auth_endpoint: auth
```

**Why:** This uses Netlify's centralized OAuth service (if enabled).

**Option 3: Check if endpoint exists at different path**

Visit these URLs in your browser to see which works:
- `https://delitterup.netlify.app/.netlify/git/github/auth`
- `https://delitterup.netlify.app/api/auth`
- `https://delitterup.netlify.app/.netlify/identity/authorize`

If one of these loads (doesn't 404), use that path in your config.

---

## Solution B: OAuth NOT Properly Installed

If OAuth doesn't show as installed, you need to install it properly.

### Install GitHub OAuth Provider (Step by Step)

1. **In Netlify Site Settings**
   - Look for "Access control" or "Security" section
   - Find "OAuth" or "Authentication providers"

2. **Click Install Provider**
   - Should see a list of providers (GitHub, GitLab, Bitbucket)
   - Select "GitHub"

3. **Authorize Netlify**
   - You'll be redirected to GitHub
   - Click "Authorize Netlify" or "Install"
   - Confirm any permissions requested

4. **Verify Installation**
   - Should redirect back to Netlify
   - GitHub should now show as "Installed" or "Active"
   - You might see a client ID or configuration details

5. **Wait 2-3 Minutes**
   - Netlify needs time to provision the OAuth endpoint
   - Don't test immediately after installing

### If You Can't Find OAuth Settings

**Netlify might have changed the UI. Try these locations:**

1. **Site Configuration → Access Control → OAuth**
2. **Site Settings → Security → OAuth providers**
3. **Site Settings → Build & deploy → Environment → OAuth**
4. **Identity tab → Services → Git Gateway**

---

## Alternative Solution: Use GitHub App Instead

If Netlify OAuth continues to have issues, you can use GitHub's OAuth directly.

### Setup GitHub OAuth App

1. **Create GitHub OAuth App**
   - Go to https://github.com/settings/developers
   - Click "OAuth Apps" → "New OAuth App"

2. **Fill in Details:**
   - Application name: `SwapBox CMS`
   - Homepage URL: `https://delitterup.netlify.app`
   - Authorization callback URL: `https://delitterup.netlify.app/admin/`

3. **Create App and Get Credentials**
   - Click "Register application"
   - Copy the "Client ID"
   - Click "Generate a new client secret"
   - Copy the "Client Secret" (save it securely!)

4. **Update admin/config.yml:**

```yaml
backend:
  name: github
  repo: litterswap/website
  branch: main
  # Remove base_url and auth_endpoint
```

5. **Add Environment Variables in Netlify:**
   - Go to Site settings → Environment variables
   - Add: `GITHUB_OAUTH_CLIENT_ID` = your Client ID
   - Add: `GITHUB_OAUTH_CLIENT_SECRET` = your Client Secret

**Problem:** This approach requires serverless functions, which adds complexity.

---

## Recommended Quick Fix: Try Simplest Config First

**1. Update admin/config.yml to simplest possible:**

```yaml
backend:
  name: github
  repo: litterswap/website
  branch: main
```

**2. Make sure OAuth is installed in Netlify**

**3. Clear browser cache and test**

**4. If still 404, check browser console for exact error**

---

## Debugging Checklist

Work through these to identify the issue:

### Check 1: Verify OAuth Installation
- [ ] Logged into Netlify dashboard
- [ ] Found OAuth/Authentication section
- [ ] GitHub shows as "Installed" or "Active"
- [ ] Waited 2-3 minutes after installing

### Check 2: Test Endpoint Exists
Visit in browser:
- [ ] `https://delitterup.netlify.app/.netlify/functions/auth`
- [ ] `https://delitterup.netlify.app/.netlify/git/github/auth`

One should load (not 404). If both 404:
→ OAuth endpoint doesn't exist → OAuth not properly installed

### Check 3: Check Netlify Deploy Logs
- [ ] Go to Deploys tab in Netlify
- [ ] Click latest deploy
- [ ] Check build logs for OAuth-related messages
- [ ] Look for "OAuth provider enabled" or similar

### Check 4: Browser Console Errors
When clicking "Login with GitHub":
- [ ] Open Dev Tools (F12) → Console tab
- [ ] Look for errors about OAuth or authentication
- [ ] Note the exact URL it's trying to reach

---

## What You Should See (Working OAuth)

**Correct flow:**
1. Click "Login with GitHub" button
2. Brief redirect/loading
3. Taken to GitHub authorization page
4. See: "Authorize SwapBox CMS" or similar
5. Click "Authorize"
6. Redirected back to admin page
7. CMS loads with collections visible

**If you see 404 at any point:**
→ OAuth endpoint doesn't exist
→ Need to properly install OAuth in Netlify

---

## Emergency Fallback: Manual Editing

If you absolutely can't get OAuth working and need your client to edit content NOW:

**They can edit files directly on GitHub:**

1. Go to https://github.com/litterswap/website
2. Navigate to `_pricing/single-cat.md` (for example)
3. Click the pencil icon (Edit)
4. Make changes
5. Click "Commit changes"
6. Wait for Netlify to redeploy

**Not ideal, but works until OAuth is fixed.**

---

## Next Steps

**1. Check OAuth Status in Netlify** (do this first!)
   - Is it installed? Active?
   - Screenshot it if unsure

**2. Try Simplest Config**
   - Remove base_url and auth_endpoint
   - Commit, push, deploy
   - Test again

**3. Share Details**
   - What do you see in Netlify OAuth settings?
   - What exact error in browser console?
   - Which endpoint URLs return 404?

With those details, I can provide exact fix!

---

## TL;DR Quick Fixes to Try

**Try in this order:**

1. **Verify OAuth installed** in Netlify Site Settings → Access Control → OAuth
2. **Remove** `base_url` and `auth_endpoint` from admin/config.yml (use simplest config)
3. **Clear browser cache** and test
4. **Wait 2-3 minutes** after any Netlify changes
5. **Check browser console** for exact error/URL

If still stuck, tell me:
- What Netlify OAuth section shows
- Browser console errors
- Which URLs return 404
