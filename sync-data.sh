#!/bin/bash
# Sync data files from content/ to _data/
# Run this if you manually edit files in content/ and need to update _data/
# (The CMS will update both automatically via admin/config.yml)

echo "Syncing data files from content/ to _data/..."

cp content/hero.json _data/hero.json
cp content/signup-form.json _data/signup-form.json
cp content/_data/settings/general.json _data/settings/general.json

echo "✅ Data files synced successfully!"
echo ""
echo "Files updated:"
echo "  - _data/hero.json"
echo "  - _data/signup-form.json"
echo "  - _data/settings/general.json"
echo ""
echo "Don't forget to commit these changes:"
echo "  git add _data/"
echo "  git commit -m 'Update data files'"
echo "  git push"
