#!/usr/bin/env python3
"""
ADHD Prompt Optimizer - Command Line Interface

Usage:
    python optimize.py "Your prompt here"
    python optimize.py -f prompt.txt
    python optimize.py -i  # Interactive mode
    
Options:
    -s, --style     Optimization style (auto, technical, debug, learning, creative)
    -o, --output    Output file path
    -j, --json      Output as JSON
    -m, --metrics   Show detailed metrics
    -q, --quiet     Only output optimized prompt
"""

import sys
import argparse
import json
from pathlib import Path

# Import the optimizer (assuming optimizer.py is in the same directory)
try:
    from optimizer import ADHDPromptOptimizer
except ImportError:
    print("Error: optimizer.py not found in current directory")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='ADHD Prompt Optimizer - Transform prompts for better AI performance',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  optimize.py "Create a Python function that sorts a list"
  optimize.py -f long_prompt.txt -o optimized.txt
  optimize.py -i -s technical
  optimize.py "Debug my code" -j -m > result.json
        """
    )
    
    parser.add_argument('prompt', nargs='?', help='Prompt text to optimize')
    parser.add_argument('-f', '--file', help='Read prompt from file')
    parser.add_argument('-i', '--interactive', action='store_true', 
                      help='Interactive mode')
    parser.add_argument('-s', '--style', 
                      choices=['auto', 'technical', 'debug', 'learning', 'creative', 'general'],
                      default='auto', help='Optimization style (default: auto)')
    parser.add_argument('-o', '--output', help='Save optimized prompt to file')
    parser.add_argument('-j', '--json', action='store_true', 
                      help='Output as JSON')
    parser.add_argument('-m', '--metrics', action='store_true', 
                      help='Show detailed metrics')
    parser.add_argument('-q', '--quiet', action='store_true', 
                      help='Only output optimized prompt')
    parser.add_argument('--no-color', action='store_true', 
                      help='Disable colored output')
    
    args = parser.parse_args()
    
    # Color codes for terminal output
    if not args.no_color and sys.stdout.isatty():
        COLORS = {
            'GREEN': '\033[92m',
            'BLUE': '\033[94m',
            'YELLOW': '\033[93m',
            'RED': '\033[91m',
            'BOLD': '\033[1m',
            'RESET': '\033[0m'
        }
    else:
        COLORS = {k: '' for k in ['GREEN', 'BLUE', 'YELLOW', 'RED', 'BOLD', 'RESET']}
    
    # Get prompt text
    prompt_text = None
    
    if args.interactive:
        print(f"{COLORS['BOLD']}🚀 ADHD Prompt Optimizer - Interactive Mode{COLORS['RESET']}")
        print("=" * 50)
        print("Enter your prompt (press Ctrl+D or Ctrl+Z when done):\n")
        try:
            prompt_text = sys.stdin.read().strip()
        except KeyboardInterrupt:
            print("\nCancelled.")
            sys.exit(0)
    elif args.file:
        try:
            prompt_text = Path(args.file).read_text().strip()
        except Exception as e:
            print(f"{COLORS['RED']}Error reading file: {e}{COLORS['RESET']}")
            sys.exit(1)
    elif args.prompt:
        prompt_text = args.prompt
    else:
        parser.print_help()
        sys.exit(0)
    
    if not prompt_text:
        print(f"{COLORS['RED']}Error: No prompt text provided{COLORS['RESET']}")
        sys.exit(1)
    
    # Initialize optimizer
    optimizer = ADHDPromptOptimizer()
    
    # Optimize the prompt
    try:
        result = optimizer.optimize(prompt_text, style=args.style)
    except Exception as e:
        print(f"{COLORS['RED']}Error optimizing prompt: {e}{COLORS['RESET']}")
        sys.exit(1)
    
    # Output results
    if args.quiet:
        print(result['optimized'])
    elif args.json:
        print(json.dumps(result, indent=2))
    else:
        # Pretty print results
        if not args.metrics:
            print(f"\n{COLORS['GREEN']}{COLORS['BOLD']}✨ OPTIMIZED PROMPT{COLORS['RESET']}")
            print("-" * 50)
            print(result['optimized'])
        else:
            print(f"\n{COLORS['BLUE']}{COLORS['BOLD']}📊 ANALYSIS{COLORS['RESET']}")
            print("-" * 50)
            print(f"Style detected: {COLORS['YELLOW']}{result['style']}{COLORS['RESET']}")
            print(f"Original tokens: ~{result['metrics']['original_tokens']}")
            print(f"Optimized tokens: ~{result['metrics']['optimized_tokens']}")
            print(f"Reduction: {COLORS['GREEN']}{result['metrics']['token_reduction']}{COLORS['RESET']}")
            print(f"Clarity score: {result['metrics']['clarity_score']:.0f}/100")
            print(f"Structure score: {result['metrics']['structure_score']:.0f}/100")
            
            if result['analysis']['components']['implicit_needs']:
                print(f"\n{COLORS['YELLOW']}💡 Implicit needs identified:{COLORS['RESET']}")
                for need in result['analysis']['components']['implicit_needs']:
                    print(f"  - {need}")
            
            print(f"\n{COLORS['GREEN']}{COLORS['BOLD']}✨ OPTIMIZED PROMPT{COLORS['RESET']}")
            print("-" * 50)
            print(result['optimized'])
            
            print(f"\n{COLORS['BLUE']}💭 Optimization notes:{COLORS['RESET']}")
            print(result['explanation'])
    
    # Save to file if requested
    if args.output:
        try:
            output_content = json.dumps(result, indent=2) if args.json else result['optimized']
            Path(args.output).write_text(output_content)
            print(f"\n{COLORS['GREEN']}✅ Saved to {args.output}{COLORS['RESET']}")
        except Exception as e:
            print(f"\n{COLORS['RED']}Error saving file: {e}{COLORS['RESET']}")
            sys.exit(1)


if __name__ == "__main__":
    main()