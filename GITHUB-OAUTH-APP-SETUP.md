# GitHub OAuth App Setup - Fix Redirect URI Error

## Error You're Seeing

**"The redirect_uri is not associated with this application"**

This means GitHub doesn't have an OAuth application registered for your CMS.

## ✅ Solution: Create GitHub OAuth App

### Step 1: Create the OAuth App

1. **Go to GitHub Developer Settings**
   - Visit: https://github.com/settings/developers
   - Click "OAuth Apps" in the left sidebar
   - Click **"New OAuth App"** button

2. **Fill in Application Details:**

   **Application name:**
   ```
   SwapBox CMS
   ```

   **Homepage URL:**
   ```
   https://delitterup.netlify.app
   ```

   **Application description:** (optional)
   ```
   Content management system for SwapBox website
   ```

   **Authorization callback URL:** (IMPORTANT - must be exact!)
   ```
   https://api.netlify.com/auth/done
   ```

3. **Click "Register application"**

### Step 2: Get Your Credentials

After creating the app, you'll see:

1. **Client ID** - Copy this (it's visible)
2. **Client secrets** section - Click "Generate a new client secret"
3. **Copy the secret** - You'll only see it once! Save it securely.

**Keep these safe - you'll need them in Step 3!**

### Step 3: Add Credentials to Netlify

1. **Go to Netlify Dashboard**
   - https://app.netlify.com
   - Select your "delitterup" site

2. **Navigate to Site Settings**
   - Click "Site settings"
   - Scroll to "Access control" or find "OAuth"

3. **Configure GitHub OAuth Provider**

   **Look for one of these:**
   - "OAuth" section with "Configure" button next to GitHub
   - "Authentication providers" with GitHub listed
   - "Install provider" → After installing, a settings/configure option

4. **Enter Your Credentials:**
   - **Key/Client ID:** Paste your GitHub OAuth App Client ID
   - **Secret:** Paste your GitHub OAuth App Client Secret
   - Click "Save" or "Install"

### Step 4: Update CMS Configuration

Your `admin/config.yml` should use this configuration:

```yaml
backend:
  name: github
  repo: litterswap/website
  branch: main
  base_url: https://api.netlify.com
  auth_endpoint: auth
```

Let me update this file for you...

### Step 5: Test the Login

1. Wait for Netlify to deploy (~2 min)
2. Visit: https://delitterup.netlify.app/admin
3. Click "Login with GitHub"
4. Should now redirect properly to GitHub authorization
5. Click "Authorize"
6. Redirected back to CMS - should work!

## Expected OAuth Flow (Correct)

```
1. Click "Login with GitHub"
   ↓
2. Redirect to: api.netlify.com/auth?provider=github...
   ↓
3. Netlify proxies to: github.com/login/oauth/authorize?client_id=YOUR_ID
   ↓
4. You see: "Authorize SwapBox CMS"
   ↓
5. Click "Authorize"
   ↓
6. GitHub redirects to: api.netlify.com/auth/done
   ↓
7. Netlify redirects to: delitterup.netlify.app/admin
   ↓
8. CMS loads with your authentication ✅
```

## Alternative: Use Netlify's OAuth Provider (Simpler)

If you don't want to create your own GitHub OAuth App, Netlify can do it for you:

### Option: Let Netlify Handle OAuth

1. **In Netlify Site Settings:**
   - Go to "Access control" → "OAuth"
   - Click "Install provider"
   - Select "GitHub"
   - **Authorize NETLIFY (not your app)**

2. **Netlify will create the OAuth app for you**
   - Client ID managed by Netlify
   - No need to create app manually

3. **Your config should be:**
   ```yaml
   backend:
     name: github
     repo: litterswap/website
     branch: main
   ```
   (No base_url or auth_endpoint needed!)

**Try this first!** It's simpler if it works.

## Troubleshooting

### OAuth App Settings Double-Check

Make sure these are EXACT:

**Homepage URL:**
- ✅ `https://delitterup.netlify.app`
- ❌ `http://delitterup.netlify.app` (no http)
- ❌ `https://delitterup.netlify.app/` (no trailing slash)

**Callback URL:**
- ✅ `https://api.netlify.com/auth/done`
- ❌ `https://delitterup.netlify.app/admin/` (wrong)

### If Still Getting Redirect URI Error

**Check:**
1. Client ID/Secret entered correctly in Netlify (no spaces)
2. OAuth app is owned by YOUR GitHub account (or org with access)
3. Callback URL in GitHub app matches exactly: `https://api.netlify.com/auth/done`
4. Waited 2-3 minutes after saving settings

### Wrong Callback URL?

If you used a different callback URL when creating the OAuth app:

1. Go back to https://github.com/settings/developers
2. Click your "SwapBox CMS" app
3. Change "Authorization callback URL" to: `https://api.netlify.com/auth/done`
4. Click "Update application"
5. Test again

## Quick Fix Commands

After creating OAuth app and adding to Netlify, update config:

```bash
# I'll do this for you in the next step
```

## Summary: What You Need to Do

1. ✅ **Create GitHub OAuth App** (https://github.com/settings/developers)
   - Callback URL: `https://api.netlify.com/auth/done`

2. ✅ **Copy Client ID and Secret**

3. ✅ **Add to Netlify** (Site Settings → OAuth)

4. ✅ **Wait for next deploy**

5. ✅ **Test login** - Should work!

---

**Need help?** Let me know which step you're stuck on!
