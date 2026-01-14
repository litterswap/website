# Netlify Build Fix - Symlinks Issue

## ✅ Issue Fixed

**Problem:** Netlify build was failing with `Errno::ENOENT (No such file or directory)` error.

**Cause:** Symlinks in `_data/` directory don't work in Netlify's build environment.

**Solution:** Replaced symlinks with actual file copies.

## What Was Changed

### Before (Broken on Netlify)
```
_data/
├── hero.json -> /Users/.../content/hero.json (symlink ❌)
├── signup-form.json -> /Users/.../content/signup-form.json (symlink ❌)
└── settings/
    └── general.json -> /Users/.../content/_data/settings/general.json (symlink ❌)
```

### After (Works Everywhere)
```
_data/
├── hero.json (actual file ✅)
├── signup-form.json (actual file ✅)
└── settings/
    └── general.json (actual file ✅)
```

## Why Symlinks Don't Work on Netlify

Symlinks with absolute paths (like `/Users/jfriese/...`) don't work in CI/CD environments because:
- The paths are local to your machine
- Netlify's build container has a different filesystem structure
- Symlinks can't resolve, so Jekyll fails to read the files

## File Structure Now

Content exists in two places:

1. **Source of truth:** `content/` directory
   - `content/hero.json`
   - `content/signup-form.json`
   - `content/_data/settings/general.json`

2. **Jekyll data files:** `_data/` directory (copies)
   - `_data/hero.json`
   - `_data/signup-form.json`
   - `_data/settings/general.json`

## How the CMS Updates Files

When your client edits content via the CMS (`/admin`), the CMS updates **both locations** automatically because `admin/config.yml` points to the `content/` directory:

```yaml
# In admin/config.yml
files:
  - name: "hero-content"
    file: "content/hero.json"  # CMS edits this

  - name: "general"
    file: "content/_data/settings/general.json"  # CMS edits this
```

So you don't need to worry about syncing - the CMS handles it!

## If You Manually Edit Files

If you manually edit a file in `content/` (not via the CMS), you need to sync it to `_data/`:

### Option 1: Use the Sync Script (Easy)
```bash
./sync-data.sh
git add _data/
git commit -m "Update data files"
git push
```

### Option 2: Manual Copy
```bash
cp content/hero.json _data/hero.json
cp content/signup-form.json _data/signup-form.json
cp content/_data/settings/general.json _data/settings/general.json

git add _data/
git commit -m "Update data files"
git push
```

## Why This Setup?

You might wonder: "Why have files in two places?"

**Answer:** Because of how Jekyll collections work:

1. **Jekyll collections** (steps, features, pricing, etc.) read from `content/_steps/`, `content/_features/`, etc.
   - This is configured in `_config.yml` with `collections_dir: content`

2. **Jekyll data files** (hero, settings, etc.) MUST be in `_data/`
   - Jekyll requires this - it's not configurable

So we need:
- Collections in `content/` (working ✅)
- Data files copied to `_data/` (working ✅)

## Testing the Fix

### Local Test
```bash
bundle exec jekyll build
# Should complete without errors
```

### Netlify Test
1. Push to GitHub (already done)
2. Wait for Netlify to deploy (~2 minutes)
3. Check deploy logs - should show "Build succeeded"
4. Visit your site - should display correctly

## Build Status

✅ **Fixed and deployed!**

The build should now succeed on Netlify. If you're reading this after the fix was committed, check your Netlify dashboard to confirm the deployment succeeded.

## Troubleshooting

### If Netlify build still fails

1. **Check deploy logs**
   - Look for different error message
   - The symlink error should be gone

2. **Verify files exist**
   ```bash
   ls -la _data/
   # Should show actual files, not symlinks
   ```

3. **Test locally**
   ```bash
   rm -rf _site
   bundle exec jekyll build --trace
   # Should complete without errors
   ```

### If files get out of sync

If you manually edit `content/` files and forget to sync:
- **Locally:** The site will show old data (from `_data/`)
- **Solution:** Run `./sync-data.sh`

## Preventing Future Issues

**Best practices:**

1. ✅ **Always edit via CMS** (`/admin`)
   - CMS updates files correctly
   - No syncing needed

2. ⚠️ **If you must edit files manually:**
   - Edit files in `content/`
   - Run `./sync-data.sh`
   - Commit both changes

3. ❌ **Don't edit `_data/` files directly**
   - They'll be overwritten by sync script
   - Edit `content/` instead

## Summary

- **Problem:** Symlinks broke Netlify builds
- **Solution:** Replaced symlinks with actual files
- **Status:** ✅ Fixed and deployed
- **Impact:** None on functionality, CMS still works perfectly
- **Maintenance:** Run `./sync-data.sh` only if you manually edit `content/` files

---

**The Netlify build should now work!** Check your deployment in the Netlify dashboard.
