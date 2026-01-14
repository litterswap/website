# Admin Setup with GitHub Authentication (Simpler!)

## ✅ Why GitHub Backend is Better

Since Netlify Identity is deprecated in favor of Auth0, we've switched to the **GitHub backend** which is:

- ✅ **Simpler** - No need for Identity or Auth0
- ✅ **Free** - No extra services required
- ✅ **Direct** - Saves directly to GitHub
- ✅ **Standard** - Your client logs in with GitHub (which they may already have)
- ✅ **Secure** - Uses Netlify's OAuth proxy

## 🚀 Quick Setup (5 minutes)

### Step 1: Enable Netlify OAuth for GitHub

1. **Go to Netlify Dashboard**
   - https://app.netlify.com
   - Select your DeLitterUp site

2. **Navigate to Site Settings**
   - Click "Site settings"
   - Scroll down to "Access control" section
   - Click "OAuth" (under Access control)

3. **Install GitHub Provider**
   - Click "Install provider" next to GitHub
   - Or if you see "Authentication providers", click that
   - Select "GitHub" from the list
   - Click "Install"

4. **Authorize with GitHub**
   - You'll be redirected to GitHub
   - Click "Authorize Netlify"
   - That's it! OAuth is now set up

### Step 2: Give Your Client Access

Your client will need a GitHub account to edit content. They have two options:

#### Option A: Client Already Has GitHub Account (Easiest)
- They just visit `yoursite.com/admin`
- Click "Login with GitHub"
- Authorize the app
- Done! They can edit content

#### Option B: Client Needs to Create GitHub Account (5 minutes)
1. Help them sign up at https://github.com/signup
2. Free account is fine
3. Add them as a collaborator to your repo:
   - Go to https://github.com/litterswap/website/settings/access
   - Click "Invite a collaborator"
   - Enter their GitHub username
   - They accept invitation
4. Now they can visit `yoursite.com/admin` and log in with GitHub

### Step 3: Test It!

1. **Visit your admin portal**
   ```
   https://your-site.netlify.app/admin
   ```

2. **Click "Login with GitHub"**
   - You'll be redirected to GitHub
   - Authorize the application
   - You'll be redirected back to the CMS

3. **You should see the CMS interface!**
   - Collections on the left (Pricing, FAQ, Testimonials, etc.)
   - Click any collection to edit
   - Make changes
   - Click "Save" - changes commit directly to GitHub!

## 🎯 How It Works

```
User visits /admin
     ↓
Clicks "Login with GitHub"
     ↓
Netlify OAuth proxy handles authentication
     ↓
GitHub authorizes the user
     ↓
User redirected back to CMS
     ↓
User can edit content
     ↓
Changes saved directly to GitHub
     ↓
Netlify auto-deploys updated site
```

## 🔐 Permissions & Security

### What GitHub Access Does the CMS Have?

- ✅ Read repository content
- ✅ Commit changes to the `main` branch
- ✅ Upload images to the repo
- ❌ Cannot delete the repository
- ❌ Cannot change repository settings
- ❌ Cannot access other repositories

### Who Can Edit Content?

**Only people who have:**
1. Access to the GitHub repository (as collaborators), OR
2. Are organization members (if repo is in an organization)

**Random visitors cannot edit** - they must authenticate via GitHub OAuth.

## 📋 User Permissions

### Repository Collaborator Levels

When inviting your client to the GitHub repo, choose:

- **Write access** (Recommended) ✅
  - Can edit content via CMS
  - Can commit changes
  - Can upload images
  - Perfect for content editors

- **Maintain access** (If you trust them more)
  - Everything "Write" can do
  - Plus: Can manage some repo settings
  - Usually not needed for content editing

- **Read access** ❌
  - Can only view content
  - Cannot edit via CMS
  - Don't use this for editors

## ⚙️ Configuration Details

The admin config now uses:

```yaml
backend:
  name: github
  repo: litterswap/website
  branch: main
  base_url: https://api.netlify.com
  auth_endpoint: auth
```

This tells the CMS:
- Use GitHub for authentication
- Connect to the `litterswap/website` repository
- Commit changes to the `main` branch
- Use Netlify's OAuth proxy for secure authentication

## 🎓 Training Your Client

### What They Need to Know:

1. **How to Log In**
   - Visit `yoursite.com/admin`
   - Click "Login with GitHub"
   - Enter GitHub credentials
   - Authorize the app (first time only)

2. **How to Edit Content**
   - Click a collection (e.g., "Pricing Plans")
   - Click an existing item to edit, or "New Pricing Plans" to add
   - Edit fields in the form
   - Click "Save"
   - Changes appear on the site in ~2 minutes

3. **How to Upload Images**
   - In any image field, click "Choose an image"
   - Upload from computer or drag & drop
   - Image is automatically saved to GitHub
   - Shows up on the site after deployment

4. **Important Notes**
   - Changes commit directly to GitHub (no "draft" mode with this setup)
   - Allow 1-2 minutes for Netlify to rebuild and deploy
   - They can see their changes at `yoursite.com` after deployment
   - If they make a mistake, you can revert via GitHub

## 🆚 Comparison: Git Gateway vs GitHub Backend

| Feature | Git Gateway (Old) | GitHub Backend (Current) |
|---------|------------------|------------------------|
| **Requires Netlify Identity** | Yes (deprecated) | No ✅ |
| **Requires Auth0 setup** | Yes (if using new auth) | No ✅ |
| **Authentication** | Email/password | GitHub account |
| **Setup complexity** | Medium | Simple ✅ |
| **Cost** | Free | Free |
| **Editorial workflow** | Yes (draft/review/publish) | No (direct commits) |
| **Who can edit** | Anyone invited | GitHub collaborators |
| **Best for** | Non-technical users without GitHub | Teams already using GitHub ✅ |

## 💡 Pros & Cons

### Pros ✅
- **Simpler setup** - No Identity, no Auth0
- **One less service** - Just GitHub + Netlify
- **Direct commits** - Changes go live faster
- **No user management** - GitHub handles it
- **Free forever** - No auth service costs

### Cons ⚠️
- Client needs GitHub account (easy to create)
- No draft/review/publish workflow (direct to main)
- Changes are immediately public after build
- Must be repository collaborator

## 🔧 Troubleshooting

### "Login with GitHub" button doesn't appear

**Check:**
1. Netlify OAuth is installed (Site Settings → Access Control → OAuth)
2. GitHub provider is enabled
3. Clear browser cache and reload /admin

### "Error: Cannot access repository"

**Check:**
1. Repository name in config.yml is correct: `litterswap/website`
2. User is a collaborator on the GitHub repo
3. Repository is not private (or user has access if it is)

### "Unauthorized" error when logging in

**Check:**
1. User has accepted repository collaborator invitation
2. Netlify OAuth is properly configured
3. Try logging out of GitHub and back in

### Changes not appearing on site

**Check:**
1. Wait 2-3 minutes for Netlify to rebuild
2. Check deploy status in Netlify dashboard
3. Hard refresh browser (Ctrl+Shift+R)
4. Verify commit was made to GitHub repo

### Client doesn't have GitHub account

**Options:**
1. Help them create free account (5 minutes at github.com/signup)
2. Consider using a shared account (not recommended for security)
3. Look into Auth0 setup (more complex, but supports email/password)

## 📖 Additional Resources

- **GitHub Signup**: https://github.com/signup
- **Decap CMS GitHub Backend**: https://decapcms.org/docs/github-backend/
- **Netlify OAuth**: https://docs.netlify.com/visitor-access/oauth-provider-tokens/

## ✅ Quick Checklist

Before your client can edit content:

- [ ] Netlify OAuth for GitHub is enabled
- [ ] Client has GitHub account
- [ ] Client is added as repository collaborator (Write access)
- [ ] Client has accepted collaborator invitation
- [ ] admin/config.yml has correct repo name
- [ ] Changes committed and pushed to GitHub
- [ ] Site successfully deployed on Netlify
- [ ] Client can visit /admin and see "Login with GitHub"

Once all boxes are checked, your client can edit content! 🎉

## 🎉 Benefits for Your Client

With this setup, your client can:
- ✅ Edit all website content without code
- ✅ Add/remove pricing plans
- ✅ Update FAQs
- ✅ Manage testimonials
- ✅ Upload images
- ✅ Change contact information
- ✅ Update service areas
- ✅ All from a user-friendly interface
- ✅ All changes tracked in Git history

**And they only need to remember:**
1. Go to `yoursite.com/admin`
2. Login with GitHub
3. Edit content
4. Click Save

That's it! 🚀
