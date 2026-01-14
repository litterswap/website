#!/bin/bash
# SwapBox Website - Development Server
# Run this script to start the Jekyll development server

export GEM_HOME="$HOME/.gem"
export PATH="$HOME/.gem/bin:$PATH"

echo "🚀 Starting SwapBox website..."
echo "📍 Visit: http://localhost:4000"
echo "🎨 CMS Admin: http://localhost:4000/admin"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

bundle exec jekyll serve --livereload
