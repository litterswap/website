#!/usr/bin/env python3
"""
Convert JSON collection files to YAML with front matter for Jekyll
"""

import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

def convert_json_to_yaml(json_file_path):
    """Convert a JSON file to YAML format with front matter"""
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Create YAML front matter
    yaml_content = "---\n"
    for key, value in data.items():
        if isinstance(value, list):
            yaml_content += f"{key}:\n"
            for item in value:
                yaml_content += f"  - {json.dumps(item)}\n"
        elif isinstance(value, str):
            # Escape quotes in strings
            value_escaped = value.replace('"', '\\"')
            yaml_content += f'{key}: "{value_escaped}"\n'
        elif isinstance(value, bool):
            yaml_content += f"{key}: {str(value).lower()}\n"
        else:
            yaml_content += f"{key}: {value}\n"
    yaml_content += "---\n"

    # Write back to file (change extension to .md)
    md_file_path = json_file_path.replace('.json', '.md')
    with open(md_file_path, 'w') as f:
        f.write(yaml_content)

    print(f"✓ Converted {json_file_path} → {md_file_path}")

    # Remove old JSON file
    os.remove(json_file_path)
    print(f"  Removed {json_file_path}")

def convert_directory(dir_path):
    """Convert all JSON files in a directory"""
    json_files = list(Path(dir_path).glob('*.json'))
    if json_files:
        print(f"\n📁 Converting {dir_path}...")
        for json_file in json_files:
            convert_json_to_yaml(str(json_file))

def main():
    print("🔄 Converting JSON collection files to YAML format...\n")

    # Collections to convert
    collections = [
        'content/_steps',
        'content/_features',
        'content/_pricing',
        'content/_benefits',
        'content/_faq',
        'content/_testimonials'
    ]

    for collection_dir in collections:
        full_path = BASE_DIR / collection_dir
        if full_path.exists():
            convert_directory(full_path)
        else:
            print(f"⚠️  Directory not found: {collection_dir}")

    print("\n✅ Conversion complete!")
    print("\nNext steps:")
    print("  1. Review the converted .md files")
    print("  2. Update admin/config.yml to use .md extension")
    print("  3. Commit and push changes")

if __name__ == "__main__":
    main()
