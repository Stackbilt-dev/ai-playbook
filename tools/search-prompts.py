#!/usr/bin/env python3
"""
Prompt Library Search Tool
Smart search functionality for finding the right prompt quickly
"""

import json
import sys
from pathlib import Path
from difflib import SequenceMatcher
import argparse
from typing import List, Dict, Any

class PromptSearcher:
    def __init__(self, index_path: str):
        """Initialize searcher with prompt index"""
        with open(index_path, 'r', encoding='utf-8') as f:
            self.index = json.load(f)
        self.prompts = self.index['prompts']
    
    def search_by_tags(self, tags: List[str]) -> List[Dict[str, Any]]:
        """Find prompts that match any of the given tags"""
        results = []
        for prompt in self.prompts:
            if any(tag.lower() in [t.lower() for t in prompt['tags']] for tag in tags):
                results.append(prompt)
        return results
    
    def search_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Find all prompts in a specific category"""
        category_lower = category.lower()
        return [p for p in self.prompts if category_lower in p['category'].lower()]
    
    def search_by_keyword(self, keyword: str) -> List[Dict[str, Any]]:
        """Full-text search across titles, descriptions, and tags"""
        keyword_lower = keyword.lower()
        results = []
        
        for prompt in self.prompts:
            # Check title
            if keyword_lower in prompt['title'].lower():
                prompt['_match_score'] = 1.0
                results.append(prompt)
                continue
            
            # Check tags
            if any(keyword_lower in tag.lower() for tag in prompt['tags']):
                prompt['_match_score'] = 0.8
                results.append(prompt)
                continue
            
            # Check description
            if keyword_lower in prompt['description'].lower():
                prompt['_match_score'] = 0.6
                results.append(prompt)
                continue
            
            # Check archetype fields for vibecoding
            if 'archetype' in prompt:
                if (keyword_lower in prompt.get('archetype', '').lower() or
                    keyword_lower in prompt.get('core_principle', '').lower()):
                    prompt['_match_score'] = 0.7
                    results.append(prompt)
        
        # Sort by match score
        results.sort(key=lambda x: x.get('_match_score', 0), reverse=True)
        return results
    
    def search_by_archetype(self, archetype: str) -> List[Dict[str, Any]]:
        """Find vibecoding prompts by archetype"""
        archetype_lower = archetype.lower()
        return [p for p in self.prompts 
                if 'archetype' in p and archetype_lower in p['archetype'].lower()]
    
    def find_similar(self, title: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Find prompts similar to the given title"""
        results = []
        
        for prompt in self.prompts:
            # Calculate similarity score
            similarity = SequenceMatcher(None, title.lower(), prompt['title'].lower()).ratio()
            
            # Also check tag overlap
            if prompt['tags']:
                tag_text = ' '.join(prompt['tags'])
                tag_similarity = SequenceMatcher(None, title.lower(), tag_text.lower()).ratio()
                similarity = max(similarity, tag_similarity * 0.8)
            
            if similarity > 0.3:  # Threshold for relevance
                prompt['_similarity'] = similarity
                results.append(prompt)
        
        # Sort by similarity and return top results
        results.sort(key=lambda x: x['_similarity'], reverse=True)
        return results[:limit]
    
    def recommend_for_task(self, task_description: str) -> List[Dict[str, Any]]:
        """Recommend prompts based on task description"""
        # Keywords that suggest different prompt types
        keywords = {
            'review': ['code review', 'review', 'optimization'],
            'write': ['writing', 'content', 'article', 'creative'],
            'analyze': ['analysis', 'data', 'parsing', 'categorization'],
            'design': ['design', 'logo', 'visual', 'creative'],
            'debug': ['debugging', 'error', 'fix', 'troubleshoot'],
            'refactor': ['refactoring', 'cleanup', 'optimization'],
            'test': ['testing', 'validation', 'quality'],
            'document': ['documentation', 'docs', 'explain']
        }
        
        recommendations = []
        task_lower = task_description.lower()
        
        # Check for keyword matches
        for key, tags in keywords.items():
            if key in task_lower:
                recommendations.extend(self.search_by_tags(tags))
        
        # Also do a general keyword search
        words = task_description.split()
        for word in words:
            if len(word) > 3:  # Skip short words
                recommendations.extend(self.search_by_keyword(word))
        
        # Remove duplicates while preserving order
        seen = set()
        unique_recommendations = []
        for prompt in recommendations:
            if prompt['path'] not in seen:
                seen.add(prompt['path'])
                unique_recommendations.append(prompt)
        
        return unique_recommendations[:10]  # Top 10 recommendations

def format_prompt_result(prompt: Dict[str, Any], verbose: bool = False) -> str:
    """Format a prompt result for display"""
    output = f"\n📄 {prompt['title']}"
    output += f"\n   Path: {prompt['path']}"
    output += f"\n   Category: {prompt['category']}"
    
    if prompt['tags']:
        output += f"\n   Tags: {', '.join(prompt['tags'])}"
    
    if 'archetype' in prompt:
        output += f"\n   🎭 Archetype: {prompt['archetype']}"
    
    if verbose and prompt['description']:
        output += f"\n   Description: {prompt['description']}"
    
    return output

def main():
    parser = argparse.ArgumentParser(description='Search the prompt library')
    parser.add_argument('query', nargs='*', help='Search query')
    parser.add_argument('-t', '--tags', nargs='+', help='Search by tags')
    parser.add_argument('-c', '--category', help='Filter by category')
    parser.add_argument('-k', '--keyword', help='Keyword search')
    parser.add_argument('-a', '--archetype', help='Search by vibecoding archetype')
    parser.add_argument('-s', '--similar', help='Find similar prompts to this title')
    parser.add_argument('-r', '--recommend', action='store_true', 
                       help='Get recommendations based on query')
    parser.add_argument('-v', '--verbose', action='store_true', 
                       help='Show detailed descriptions')
    parser.add_argument('--list-categories', action='store_true', 
                       help='List all categories')
    parser.add_argument('--list-tags', action='store_true', 
                       help='List all tags')
    parser.add_argument('--list-archetypes', action='store_true', 
                       help='List all vibecoding archetypes')
    
    args = parser.parse_args()
    
    # Find index file
    script_dir = Path(__file__).parent
    index_path = script_dir.parent / 'prompt-index.json'
    
    if not index_path.exists():
        print("Error: prompt-index.json not found. Run index-prompts.py first.")
        sys.exit(1)
    
    searcher = PromptSearcher(str(index_path))
    
    # Handle list operations
    if args.list_categories:
        print("\n📁 Categories:")
        for cat, count in sorted(searcher.index['metadata']['categories'].items()):
            print(f"   {cat}: {count} prompts")
        return
    
    if args.list_tags:
        print("\n🏷️  Tags (sorted by frequency):")
        sorted_tags = sorted(searcher.index['metadata']['tags'].items(), 
                           key=lambda x: x[1], reverse=True)
        for tag, count in sorted_tags[:20]:  # Top 20 tags
            print(f"   {tag}: {count} prompts")
        return
    
    if args.list_archetypes:
        print("\n🎭 Vibecoding Archetypes:")
        for archetype in searcher.index['metadata']['archetypes']:
            print(f"   - {archetype}")
        return
    
    # Perform search
    results = []
    
    if args.tags:
        results = searcher.search_by_tags(args.tags)
        print(f"\n🔍 Searching for tags: {', '.join(args.tags)}")
    elif args.category:
        results = searcher.search_by_category(args.category)
        print(f"\n🔍 Searching in category: {args.category}")
    elif args.keyword:
        results = searcher.search_by_keyword(args.keyword)
        print(f"\n🔍 Searching for keyword: {args.keyword}")
    elif args.archetype:
        results = searcher.search_by_archetype(args.archetype)
        print(f"\n🔍 Searching for archetype: {args.archetype}")
    elif args.similar:
        results = searcher.find_similar(args.similar)
        print(f"\n🔍 Finding prompts similar to: {args.similar}")
    elif args.recommend and args.query:
        query_text = ' '.join(args.query)
        results = searcher.recommend_for_task(query_text)
        print(f"\n🎯 Recommendations for: {query_text}")
    elif args.query:
        # Default to keyword search
        query_text = ' '.join(args.query)
        results = searcher.search_by_keyword(query_text)
        print(f"\n🔍 Searching for: {query_text}")
    else:
        parser.print_help()
        return
    
    # Display results
    if results:
        print(f"\nFound {len(results)} results:")
        for prompt in results:
            print(format_prompt_result(prompt, args.verbose))
    else:
        print("\nNo results found.")
    
    print("\n💡 Tip: Use -v for detailed descriptions, or -r for task recommendations")

if __name__ == '__main__':
    main()