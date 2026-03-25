# ADHD Prompt Optimizer - Interactive Script

This script provides an interactive way to optimize prompts using ADHD principles. It can be used as a standalone tool or integrated into other systems.

## Core Optimization Engine

```python
import re
from typing import Dict, List, Tuple, Optional
import json

class ADHDPromptOptimizer:
    """
    Transforms any prompt into an ADHD-optimized version for better LLM performance
    and context efficiency.
    """
    
    def __init__(self):
        self.emoji_map = {
            'task': '🎯',
            'context': '📋',
            'requirements': '✅',
            'constraints': '⚠️',
            'avoid': '🚫',
            'tools': '🔧',
            'input': '📥',
            'output': '📤',
            'bug': '🐛',
            'location': '📍',
            'tried': '🔍',
            'hypothesis': '💭',
            'need': '❓',
            'learn': '📚',
            'level': '🎓',
            'goal': '🎯',
            'time': '⏱️',
            'style': '💡',
            'data': '📊',
            'create': '✍️',
            'audience': '🎪',
            'build': '🏗️',
            'feature': '⭐'
        }
        
        # Common patterns for extraction
        self.patterns = {
            'task_indicators': [
                'i need', 'i want', 'help me', 'create', 'build', 'make',
                'design', 'implement', 'fix', 'solve', 'explain', 'write'
            ],
            'context_indicators': [
                'i have', "i'm using", 'working with', 'based on', 'currently',
                'background', 'experience with', 'familiar with'
            ],
            'requirement_indicators': [
                'should', 'must', 'need to', 'has to', 'require', 'want it to',
                'make sure', 'important that', 'essential'
            ],
            'constraint_indicators': [
                'limit', 'maximum', 'minimum', 'budget', 'deadline', 'only',
                'cannot', "don't", 'avoid', 'without', 'except'
            ]
        }
        
        self.filler_words = [
            'basically', 'actually', 'really', 'very', 'quite', 'somewhat',
            'perhaps', 'maybe', 'probably', 'definitely', 'certainly',
            'i think', 'i believe', 'i feel', 'in my opinion', 'it seems'
        ]
    
    def analyze_prompt(self, prompt: str) -> Dict[str, any]:
        """Analyze prompt to extract key components."""
        prompt_lower = prompt.lower()
        
        analysis = {
            'original': prompt,
            'word_count': len(prompt.split()),
            'char_count': len(prompt),
            'components': {
                'task': self._extract_task(prompt),
                'context': self._extract_context(prompt),
                'requirements': self._extract_requirements(prompt),
                'constraints': self._extract_constraints(prompt),
                'implicit_needs': self._identify_implicit_needs(prompt)
            },
            'complexity': self._assess_complexity(prompt),
            'optimization_potential': self._calculate_optimization_potential(prompt)
        }
        
        return analysis
    
    def optimize(self, prompt: str, style: str = 'auto') -> Dict[str, any]:
        """
        Optimize a prompt using ADHD principles.
        
        Args:
            prompt: Original prompt text
            style: Optimization style ('technical', 'creative', 'learning', 'debug', 'auto')
        
        Returns:
            Dictionary with optimized prompt and metrics
        """
        analysis = self.analyze_prompt(prompt)
        
        if style == 'auto':
            style = self._detect_style(prompt)
        
        optimized = self._apply_optimization(analysis, style)
        
        # Calculate metrics
        original_tokens = self._estimate_tokens(prompt)
        optimized_tokens = self._estimate_tokens(optimized)
        
        return {
            'original': prompt,
            'optimized': optimized,
            'style': style,
            'metrics': {
                'original_tokens': original_tokens,
                'optimized_tokens': optimized_tokens,
                'token_reduction': f"{((original_tokens - optimized_tokens) / original_tokens * 100):.1f}%",
                'clarity_score': self._calculate_clarity_score(optimized),
                'structure_score': self._calculate_structure_score(optimized)
            },
            'analysis': analysis,
            'explanation': self._generate_explanation(analysis, style)
        }
    
    def _extract_task(self, prompt: str) -> Optional[str]:
        """Extract the main task from the prompt."""
        prompt_lower = prompt.lower()
        
        for indicator in self.patterns['task_indicators']:
            if indicator in prompt_lower:
                # Find the sentence containing the indicator
                sentences = prompt.split('.')
                for sentence in sentences:
                    if indicator in sentence.lower():
                        # Clean and extract the core ask
                        task = sentence.strip()
                        task = re.sub(r'^.*?' + indicator + r'\s*', '', task, flags=re.IGNORECASE)
                        return task.strip()
        
        # Fallback: assume first sentence is the task
        first_sentence = prompt.split('.')[0]
        return first_sentence.strip()
    
    def _extract_context(self, prompt: str) -> List[str]:
        """Extract context elements from the prompt."""
        context_items = []
        prompt_lower = prompt.lower()
        
        for indicator in self.patterns['context_indicators']:
            if indicator in prompt_lower:
                # Extract the phrase following the indicator
                pattern = rf'{indicator}\s+([^,.;]+)'
                matches = re.findall(pattern, prompt_lower)
                context_items.extend(matches)
        
        # Remove duplicates and clean
        context_items = list(set(item.strip() for item in context_items))
        return context_items[:5]  # Limit to 5 most relevant
    
    def _extract_requirements(self, prompt: str) -> List[str]:
        """Extract requirements from the prompt."""
        requirements = []
        prompt_lower = prompt.lower()
        
        for indicator in self.patterns['requirement_indicators']:
            if indicator in prompt_lower:
                pattern = rf'{indicator}\s+([^,.;]+)'
                matches = re.findall(pattern, prompt_lower)
                requirements.extend(matches)
        
        # Clean and deduplicate
        requirements = list(set(req.strip() for req in requirements))
        return requirements
    
    def _extract_constraints(self, prompt: str) -> List[str]:
        """Extract constraints from the prompt."""
        constraints = []
        prompt_lower = prompt.lower()
        
        for indicator in self.patterns['constraint_indicators']:
            if indicator in prompt_lower:
                pattern = rf'{indicator}\s+([^,.;]+)'
                matches = re.findall(pattern, prompt_lower)
                constraints.extend(matches)
        
        return list(set(constraint.strip() for constraint in constraints))
    
    def _identify_implicit_needs(self, prompt: str) -> List[str]:
        """Identify needs that are implied but not explicitly stated."""
        implicit = []
        prompt_lower = prompt.lower()
        
        # Check for common implicit needs
        if 'api' in prompt_lower and 'document' not in prompt_lower:
            implicit.append('API documentation')
        
        if 'build' in prompt_lower and 'test' not in prompt_lower:
            implicit.append('Testing approach')
        
        if 'performance' in prompt_lower and 'metric' not in prompt_lower:
            implicit.append('Performance metrics')
        
        if 'secure' in prompt_lower or 'security' in prompt_lower:
            if 'auth' not in prompt_lower:
                implicit.append('Authentication method')
        
        return implicit
    
    def _detect_style(self, prompt: str) -> str:
        """Auto-detect the prompt style based on content."""
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['bug', 'error', 'fix', 'debug', 'issue']):
            return 'debug'
        elif any(word in prompt_lower for word in ['learn', 'explain', 'understand', 'tutorial']):
            return 'learning'
        elif any(word in prompt_lower for word in ['write', 'create content', 'story', 'article']):
            return 'creative'
        elif any(word in prompt_lower for word in ['api', 'function', 'code', 'implement']):
            return 'technical'
        else:
            return 'general'
    
    def _apply_optimization(self, analysis: Dict, style: str) -> str:
        """Apply ADHD optimization based on style."""
        components = analysis['components']
        
        # Style-specific templates
        templates = {
            'technical': self._optimize_technical,
            'debug': self._optimize_debug,
            'learning': self._optimize_learning,
            'creative': self._optimize_creative,
            'general': self._optimize_general
        }
        
        optimizer = templates.get(style, self._optimize_general)
        return optimizer(components)
    
    def _optimize_technical(self, components: Dict) -> str:
        """Optimize technical/coding prompts."""
        lines = []
        
        if components['task']:
            lines.append(f"{self.emoji_map['build']} BUILD: {components['task']}")
        
        if components['context']:
            lines.append(f"{self.emoji_map['tools']} STACK: {', '.join(components['context'])}")
        
        if components['requirements']:
            lines.append(f"{self.emoji_map['requirements']} REQUIREMENTS:")
            for req in components['requirements'][:5]:
                lines.append(f"- {req}")
        
        if components['constraints']:
            lines.append(f"{self.emoji_map['constraints']} CONSTRAINTS:")
            for constraint in components['constraints'][:3]:
                lines.append(f"- {constraint}")
        
        if components['implicit_needs']:
            lines.append(f"{self.emoji_map['output']} INCLUDE:")
            for need in components['implicit_needs']:
                lines.append(f"- {need}")
        
        return '\n'.join(lines)
    
    def _optimize_debug(self, components: Dict) -> str:
        """Optimize debugging prompts."""
        lines = []
        
        lines.append(f"{self.emoji_map['bug']} ISSUE: {components['task']}")
        
        if components['context']:
            lines.append(f"{self.emoji_map['location']} CONTEXT: {', '.join(components['context'])}")
        
        if components['requirements']:
            lines.append(f"{self.emoji_map['tried']} ATTEMPTED:")
            for req in components['requirements'][:3]:
                lines.append(f"- {req}")
        
        lines.append(f"{self.emoji_map['need']} NEED: Specific fix")
        
        return '\n'.join(lines)
    
    def _optimize_learning(self, components: Dict) -> str:
        """Optimize learning prompts."""
        lines = []
        
        lines.append(f"{self.emoji_map['learn']} LEARN: {components['task']}")
        
        if components['context']:
            lines.append(f"{self.emoji_map['level']} BACKGROUND: {', '.join(components['context'])}")
        
        lines.append(f"{self.emoji_map['goal']} TARGET: Practical understanding")
        lines.append(f"{self.emoji_map['style']} FORMAT: Examples > theory")
        
        return '\n'.join(lines)
    
    def _optimize_creative(self, components: Dict) -> str:
        """Optimize creative prompts."""
        lines = []
        
        lines.append(f"{self.emoji_map['create']} CREATE: {components['task']}")
        
        if components['context']:
            lines.append(f"{self.emoji_map['context']} CONTEXT: {', '.join(components['context'])}")
        
        if components['requirements']:
            lines.append(f"{self.emoji_map['style']} STYLE: {', '.join(components['requirements'][:2])}")
        
        if components['constraints']:
            lines.append(f"{self.emoji_map['avoid']} AVOID: {', '.join(components['constraints'][:2])}")
        
        return '\n'.join(lines)
    
    def _optimize_general(self, components: Dict) -> str:
        """General optimization for any prompt."""
        lines = []
        
        if components['task']:
            lines.append(f"{self.emoji_map['task']} TASK: {components['task']}")
        
        if components['context']:
            lines.append(f"{self.emoji_map['context']} CONTEXT:")
            for ctx in components['context'][:3]:
                lines.append(f"- {ctx}")
        
        if components['requirements']:
            lines.append(f"{self.emoji_map['requirements']} REQUIREMENTS:")
            for req in components['requirements'][:4]:
                lines.append(f"- {req}")
        
        if components['constraints']:
            lines.append(f"{self.emoji_map['constraints']} CONSTRAINTS: {', '.join(components['constraints'][:2])}")
        
        lines.append(f"{self.emoji_map['output']} OUTPUT: Clear solution")
        
        return '\n'.join(lines)
    
    def _estimate_tokens(self, text: str) -> int:
        """Estimate token count (rough approximation)."""
        # Rough estimate: ~4 characters per token
        return len(text) // 4
    
    def _calculate_clarity_score(self, text: str) -> float:
        """Calculate clarity score (0-100)."""
        score = 100.0
        
        # Penalize for lack of structure
        if not any(emoji in text for emoji in self.emoji_map.values()):
            score -= 20
        
        # Reward for bullet points
        if '- ' in text:
            score += 10
        
        # Reward for clear sections
        if '\n' in text:
            score += 5
        
        # Penalize for filler words
        text_lower = text.lower()
        filler_count = sum(1 for word in self.filler_words if word in text_lower)
        score -= (filler_count * 5)
        
        return max(0, min(100, score))
    
    def _calculate_structure_score(self, text: str) -> float:
        """Calculate structure score (0-100)."""
        score = 0
        
        # Points for each structural element
        if any(emoji in text for emoji in self.emoji_map.values()):
            score += 30
        
        if '- ' in text:  # Bullet points
            score += 20
        
        if text.count('\n') > 2:  # Multiple sections
            score += 20
        
        if ':' in text:  # Clear labeling
            score += 15
        
        if any(word.isupper() for word in text.split()):  # Keywords
            score += 15
        
        return min(100, score)
    
    def _assess_complexity(self, prompt: str) -> str:
        """Assess prompt complexity."""
        word_count = len(prompt.split())
        component_count = sum(1 for v in self.analyze_prompt(prompt)['components'].values() if v)
        
        if word_count > 100 or component_count > 4:
            return 'high'
        elif word_count > 50 or component_count > 2:
            return 'medium'
        else:
            return 'low'
    
    def _calculate_optimization_potential(self, prompt: str) -> str:
        """Calculate how much the prompt can be optimized."""
        prompt_lower = prompt.lower()
        
        # Count optimization opportunities
        opportunities = 0
        
        # Filler words
        opportunities += sum(1 for word in self.filler_words if word in prompt_lower)
        
        # Lack of structure
        if '\n' not in prompt:
            opportunities += 3
        
        # Buried main ask
        if not any(prompt_lower.startswith(ind) for ind in self.patterns['task_indicators']):
            opportunities += 2
        
        # Long sentences
        sentences = prompt.split('.')
        opportunities += sum(1 for s in sentences if len(s.split()) > 20)
        
        if opportunities > 8:
            return 'high'
        elif opportunities > 4:
            return 'medium'
        else:
            return 'low'
    
    def _generate_explanation(self, analysis: Dict, style: str) -> str:
        """Generate explanation of optimizations made."""
        explanations = []
        
        explanations.append(f"Detected style: {style}")
        explanations.append(f"Complexity: {analysis['complexity']}")
        explanations.append(f"Optimization potential: {analysis['optimization_potential']}")
        
        if analysis['components']['implicit_needs']:
            explanations.append(f"Identified implicit needs: {', '.join(analysis['components']['implicit_needs'])}")
        
        return ' | '.join(explanations)


# Interactive CLI usage
def interactive_optimize():
    """Run interactive optimization session."""
    optimizer = ADHDPromptOptimizer()
    
    print("🚀 ADHD Prompt Optimizer")
    print("=" * 50)
    print("Enter your prompt (press Enter twice to optimize):")
    print()
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    prompt = '\n'.join(lines)
    
    if not prompt.strip():
        print("No prompt entered!")
        return
    
    print("\n" + "=" * 50)
    print("Analyzing and optimizing...")
    print()
    
    result = optimizer.optimize(prompt)
    
    print("📊 ANALYSIS")
    print("-" * 30)
    print(f"Original tokens: ~{result['metrics']['original_tokens']}")
    print(f"Optimized tokens: ~{result['metrics']['optimized_tokens']}")
    print(f"Reduction: {result['metrics']['token_reduction']}")
    print(f"Clarity score: {result['metrics']['clarity_score']:.0f}/100")
    print(f"Structure score: {result['metrics']['structure_score']:.0f}/100")
    print()
    
    print("✨ OPTIMIZED PROMPT")
    print("-" * 30)
    print(result['optimized'])
    print()
    
    print("💡 EXPLANATION")
    print("-" * 30)
    print(result['explanation'])


# Example usage as a library
if __name__ == "__main__":
    # Example 1: Direct optimization
    optimizer = ADHDPromptOptimizer()
    
    test_prompt = """
    I'm working on a React application and I've noticed that when I render large lists 
    of items, the performance becomes really sluggish. I've tried using key props and 
    I'm already using functional components, but it's still slow. The list has about 
    1000 items and each item has several child components. I need to figure out how to 
    optimize this. Can you help me understand the best practices for handling large 
    lists in React?
    """
    
    result = optimizer.optimize(test_prompt)
    print(json.dumps(result, indent=2))
```

## Usage Examples

### As a Python Library
```python
from adhd_optimizer import ADHDPromptOptimizer

optimizer = ADHDPromptOptimizer()
result = optimizer.optimize("Your long prompt here...")
print(result['optimized'])
```

### As a Command Line Tool
```bash
python adhd_optimizer.py
# Enter your prompt and press Enter twice
```

### Integration with Other Tools
```python
# Function to optimize any prompt
def optimize_prompt(prompt: str) -> str:
    optimizer = ADHDPromptOptimizer()
    result = optimizer.optimize(prompt)
    return result['optimized']

# Use in your workflow
original = "I need help creating a REST API..."
optimized = optimize_prompt(original)
```

## API Reference

### ADHDPromptOptimizer Methods

#### `optimize(prompt: str, style: str = 'auto') -> Dict`
Main optimization method. Returns dictionary with:
- `original`: Original prompt
- `optimized`: Optimized version
- `metrics`: Token counts and scores
- `analysis`: Detailed component breakdown
- `explanation`: What was optimized and why

#### `analyze_prompt(prompt: str) -> Dict`
Analyzes prompt structure without optimizing. Useful for understanding prompt composition.

### Styles
- `'auto'`: Automatically detect style
- `'technical'`: Code/API/implementation prompts
- `'debug'`: Error fixing and troubleshooting
- `'learning'`: Educational and explanatory
- `'creative'`: Content creation and writing
- `'general'`: Default optimization

## Extending the Optimizer

Add custom patterns:
```python
optimizer = ADHDPromptOptimizer()
optimizer.patterns['custom_indicators'] = ['specific', 'domain', 'terms']
optimizer.emoji_map['custom'] = '🎨'
```

This tool is designed to be both powerful and extensible, helping you masterfully navigate context limits while maintaining clarity.