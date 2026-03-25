#!/usr/bin/env python3
"""
Prompt Library Indexer
Extracts metadata from all markdown files to create a searchable index
"""

import os
import json
import yaml
import re
from pathlib import Path
from datetime import datetime

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return {}
    return {}

def extract_description(content):
    """Extract first paragraph after Context section or first non-header paragraph"""
    # Remove frontmatter
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    
    # Try to find Context section
    context_match = re.search(r'## Context\s*\n\n?(.+?)(?:\n\n|\n#)', content, re.DOTALL)
    if context_match:
        return context_match.group(1).strip()
    
    # Otherwise, get first paragraph that's not a header
    paragraphs = content.split('\n\n')
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('#') and len(para) > 20:
            return para[:200] + '...' if len(para) > 200 else para
    
    return ""

def index_prompt_library(root_dir):
    """Create index of all prompts in the library"""
    index = {
        'metadata': {
            'created': datetime.now().isoformat(),
            'total_prompts': 0,
            'categories': {},
            'tags': {},
            'archetypes': []
        },
        'prompts': []
    }
    
    root_path = Path(root_dir)
    
    # Walk through all markdown files
    for filepath in root_path.rglob('*.md'):
        # Skip README files and non-prompt files
        if filepath.name.lower() in ['readme.md', 'claude.md']:
            continue
            
        relative_path = filepath.relative_to(root_path)
        
        # Read file content
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            continue
        
        # Extract metadata
        frontmatter = extract_frontmatter(content)
        if not frontmatter:
            continue
            
        # Build prompt entry
        prompt_entry = {
            'title': frontmatter.get('title', filepath.stem.replace('-', ' ').title()),
            'path': str(relative_path),
            'category': frontmatter.get('category', str(relative_path.parent)),
            'tags': frontmatter.get('tags', []),
            'description': extract_description(content),
            'created': frontmatter.get('created', ''),
            'updated': frontmatter.get('updated', ''),
            'version': frontmatter.get('version', 1.0),
            'author': frontmatter.get('author', '')
        }
        
        # Add vibecoding specific fields
        if 'archetype' in frontmatter:
            prompt_entry['archetype'] = frontmatter['archetype']
            prompt_entry['philosophical_fusion'] = frontmatter.get('philosophical_fusion', '')
            prompt_entry['core_principle'] = frontmatter.get('core_principle', '')
            if frontmatter['archetype'] not in index['metadata']['archetypes']:
                index['metadata']['archetypes'].append(frontmatter['archetype'])
        
        # Update index
        index['prompts'].append(prompt_entry)
        index['metadata']['total_prompts'] += 1
        
        # Track categories
        category = prompt_entry['category']
        if category not in index['metadata']['categories']:
            index['metadata']['categories'][category] = 0
        index['metadata']['categories'][category] += 1
        
        # Track tags
        for tag in prompt_entry['tags']:
            if tag not in index['metadata']['tags']:
                index['metadata']['tags'][tag] = 0
            index['metadata']['tags'][tag] += 1
    
    # Sort prompts by category and title
    index['prompts'].sort(key=lambda x: (x['category'], x['title']))
    
    return index

def save_index(index, output_path):
    """Save index to JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"Index saved to {output_path}")
    print(f"Total prompts indexed: {index['metadata']['total_prompts']}")
    print(f"Categories: {len(index['metadata']['categories'])}")
    print(f"Unique tags: {len(index['metadata']['tags'])}")

if __name__ == '__main__':
    # Get the repository root (parent of tools directory)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    # Create index
    print("Indexing prompt library...")
    index = index_prompt_library(repo_root)
    
    # Save index
    output_path = repo_root / 'prompt-index.json'
    save_index(index, output_path)