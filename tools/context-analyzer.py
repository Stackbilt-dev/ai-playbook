#!/usr/bin/env python3
"""
Context Analyzer - Analyze prompts for context engineering optimization opportunities
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple
import yaml

class ContextAnalyzer:
    """Analyze prompts for context engineering optimization opportunities."""
    
    def __init__(self, prompt_dir: str = "."):
        self.prompt_dir = Path(prompt_dir)
        self.results = []
        
    def analyze_file(self, filepath: Path) -> Dict:
        """Analyze a single prompt file for optimization opportunities."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract frontmatter and content
        frontmatter, prompt_content = self.extract_sections(content)
        
        # Calculate metrics
        metrics = {
            'filepath': str(filepath.relative_to(self.prompt_dir)),
            'title': frontmatter.get('title', 'Unknown'),
            'category': frontmatter.get('category', 'Unknown'),
            'total_tokens': self.estimate_tokens(content),
            'prompt_tokens': self.estimate_tokens(prompt_content),
            'redundancy_score': self.calculate_redundancy(prompt_content),
            'structure_score': self.analyze_structure(prompt_content),
            'optimization_potential': 'Unknown',
            'suggested_patterns': []
        }
        
        # Analyze optimization potential
        metrics['optimization_potential'] = self.assess_optimization_potential(metrics)
        metrics['suggested_patterns'] = self.suggest_patterns(prompt_content, frontmatter)
        
        return metrics
    
    def extract_sections(self, content: str) -> Tuple[Dict, str]:
        """Extract frontmatter and main content from file."""
        frontmatter = {}
        prompt_content = content
        
        # Extract YAML frontmatter
        if content.startswith('---\n'):
            parts = content.split('---\n', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                except:
                    pass
                prompt_content = parts[2]
                
        return frontmatter, prompt_content
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate token count (rough approximation)."""
        # Approximate: 1 token ≈ 4 characters or 0.75 words
        words = len(text.split())
        chars = len(text)
        return int(max(chars / 4, words * 0.75))
    
    def calculate_redundancy(self, text: str) -> float:
        """Calculate redundancy score (0-1, higher = more redundant)."""
        lines = text.lower().split('\n')
        unique_lines = set(lines)
        
        # Check for repeated phrases
        phrases = re.findall(r'\b\w+\s+\w+\s+\w+\b', text.lower())
        unique_phrases = set(phrases)
        
        if not phrases or not lines:
            return 0.0
            
        line_redundancy = 1 - (len(unique_lines) / len(lines))
        phrase_redundancy = 1 - (len(unique_phrases) / len(phrases))
        
        return (line_redundancy + phrase_redundancy) / 2
    
    def analyze_structure(self, text: str) -> Dict:
        """Analyze the structure of the prompt."""
        structure = {
            'has_role': bool(re.search(r'\b(you are|role:|acting as)\b', text, re.I)),
            'has_task': bool(re.search(r'\b(task:|objective:|goal:|should)\b', text, re.I)),
            'has_instructions': bool(re.search(r'\b(instructions:|steps:|follow|must)\b', text, re.I)),
            'has_examples': bool(re.search(r'\b(example:|for instance|such as|e\.g\.)\b', text, re.I)),
            'has_constraints': bool(re.search(r'\b(constraint:|limit:|must not|avoid)\b', text, re.I)),
            'list_count': len(re.findall(r'^\s*[-*•]\s+', text, re.MULTILINE)),
            'numbered_lists': len(re.findall(r'^\s*\d+\.\s+', text, re.MULTILINE))
        }
        return structure
    
    def assess_optimization_potential(self, metrics: Dict) -> str:
        """Assess the optimization potential based on metrics."""
        tokens = metrics['prompt_tokens']
        redundancy = metrics['redundancy_score']
        structure = metrics['structure_score']
        
        # High potential: Long prompts with high redundancy
        if tokens > 300 and redundancy > 0.3:
            return "High"
        # Medium potential: Moderate length with some redundancy or many lists
        elif tokens > 150 and (redundancy > 0.2 or structure.get('list_count', 0) > 5):
            return "Medium"
        # Low potential: Already concise or well-structured
        elif tokens < 100 or redundancy < 0.1:
            return "Low"
        else:
            return "Medium"
    
    def suggest_patterns(self, content: str, frontmatter: Dict) -> List[str]:
        """Suggest context engineering patterns based on content analysis."""
        suggestions = []
        
        # Check for different prompt types and suggest patterns
        if 'vibecoding' in frontmatter.get('tags', []):
            suggestions.append("Field-based: Convert philosophical descriptions to field dynamics")
            
        if re.search(r'step.by.step|procedure|workflow', content, re.I):
            suggestions.append("Control-flow: Implement explicit control flow pattern")
            
        if re.search(r'examples?|for instance|such as', content, re.I):
            suggestions.append("Few-shot: Extract examples into few-shot format")
            
        if len(content) > 1000:
            suggestions.append("Progressive: Use progressive context enhancement")
            
        if re.search(r'you are an? \w+ expert', content, re.I):
            suggestions.append("Minimal-role: Compress role to essential attributes")
            
        if re.search(r'(analyze|evaluate|assess|review)', content, re.I):
            suggestions.append("Token-budget: Implement token budgeting for analysis")
            
        return suggestions
    
    def analyze_directory(self, directory: Path = None) -> List[Dict]:
        """Analyze all prompt files in directory."""
        if directory is None:
            directory = self.prompt_dir
            
        results = []
        for filepath in directory.rglob("*.md"):
            # Skip README files and non-prompt files
            if filepath.name.lower() == 'readme.md':
                continue
            if 'frameworks' in str(filepath) or 'tools' in str(filepath):
                continue
                
            try:
                result = self.analyze_file(filepath)
                results.append(result)
            except Exception as e:
                print(f"Error analyzing {filepath}: {e}")
                
        return results
    
    def generate_report(self, results: List[Dict]) -> str:
        """Generate optimization report."""
        report = ["# Context Engineering Analysis Report\n"]
        report.append(f"Analyzed {len(results)} prompts\n")
        
        # Summary statistics
        total_tokens = sum(r['total_tokens'] for r in results)
        high_potential = [r for r in results if r['optimization_potential'] == 'High']
        medium_potential = [r for r in results if r['optimization_potential'] == 'Medium']
        
        report.append("## Summary Statistics\n")
        report.append(f"- Total tokens across all prompts: {total_tokens:,}")
        report.append(f"- Average tokens per prompt: {total_tokens // len(results):,}")
        report.append(f"- High optimization potential: {len(high_potential)} prompts")
        report.append(f"- Medium optimization potential: {len(medium_potential)} prompts")
        report.append(f"- Estimated token savings (50% reduction): {total_tokens // 2:,}\n")
        
        # High potential prompts
        if high_potential:
            report.append("## High Optimization Potential\n")
            for prompt in sorted(high_potential, key=lambda x: x['prompt_tokens'], reverse=True)[:10]:
                report.append(f"### {prompt['title']}")
                report.append(f"- **File**: {prompt['filepath']}")
                report.append(f"- **Tokens**: {prompt['prompt_tokens']:,}")
                report.append(f"- **Redundancy**: {prompt['redundancy_score']:.2%}")
                report.append(f"- **Suggested Patterns**: {', '.join(prompt['suggested_patterns'])}")
                report.append("")
        
        # Pattern frequency
        all_patterns = []
        for r in results:
            all_patterns.extend(r['suggested_patterns'])
        
        if all_patterns:
            report.append("## Recommended Patterns\n")
            pattern_counts = {}
            for pattern in all_patterns:
                pattern_type = pattern.split(':')[0]
                pattern_counts[pattern_type] = pattern_counts.get(pattern_type, 0) + 1
            
            for pattern, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True):
                report.append(f"- **{pattern}**: {count} prompts")
        
        return '\n'.join(report)
    
    def export_json(self, results: List[Dict], output_file: str):
        """Export results as JSON for further processing."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'analysis_date': str(Path.cwd()),
                'total_prompts': len(results),
                'results': results
            }, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description='Analyze prompts for context engineering optimization')
    parser.add_argument('path', nargs='?', default='.', help='Path to analyze (default: current directory)')
    parser.add_argument('-o', '--output', help='Output report file (default: print to stdout)')
    parser.add_argument('-j', '--json', help='Export results as JSON')
    parser.add_argument('-c', '--category', help='Analyze only specific category')
    
    args = parser.parse_args()
    
    analyzer = ContextAnalyzer(args.path)
    
    # Analyze prompts
    if args.category:
        results = analyzer.analyze_directory(Path(args.path) / args.category)
    else:
        results = analyzer.analyze_directory()
    
    # Generate report
    report = analyzer.generate_report(results)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)
    
    # Export JSON if requested
    if args.json:
        analyzer.export_json(results, args.json)
        print(f"JSON data exported to {args.json}")


if __name__ == "__main__":
    main()