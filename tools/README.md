# AI Playbook Tools

Utilities for searching, indexing, and optimizing the playbook content.

## Quick Start

From the repository root:

```bash
# Search for prompts
python tools/search-prompts.py "code review"
python tools/search-prompts.py -t optimization debugging
python tools/search-prompts.py -r "I need to analyze data"

# Rebuild search index after changes
python tools/index-prompts.py
```

## Tools Overview

### 🚀 `adhd-optimizer/`
Transforms any prompt into a context-optimized version using ADHD principles:

- **40-60% token reduction** while maintaining information fidelity
- **Multiple interfaces**: Web UI, Python CLI, batch script
- **Auto-detects style**: technical, debug, learning, creative
- **Provides metrics**: token counts, clarity scores, structure analysis
- **Identifies implicit needs** in prompts

Quick usage:
```bash
# Command line
python tools/adhd-optimizer/optimize.py "Your long prompt here"

# Interactive mode
python tools/adhd-optimizer/optimize.py -i

# Web interface
open tools/adhd-optimizer/optimizer.html
```

### 🔍 `search-prompts.py`
The main search engine with multiple search modes:

- **Keyword search**: `./search "your query"`
- **Tag search**: `./search -t tag1 tag2`
- **Category filter**: `./search -c "tasks/coding"`
- **Archetype search**: `./search -a "Clarity Architect"`
- **Similarity**: `./search -s "article writer"`
- **Recommendations**: `./search -r "analyze customer feedback"`

### 🗂️ `index-prompts.py`
Creates and updates the searchable index of all prompts:

- Extracts metadata from YAML frontmatter
- Builds searchable descriptions
- Tracks tags, categories, and archetypes
- Outputs to `prompt-index.json`

### 📊 `context-analyzer.py`
Analyzes prompts for context engineering optimization opportunities:

- Calculates token usage and redundancy
- Identifies optimization patterns
- Suggests context engineering techniques
- Generates optimization reports

Usage:
```bash
# Analyze all prompts
python3 tools/context-analyzer.py

# Analyze specific category
python3 tools/context-analyzer.py -c tasks/writing

# Export detailed JSON report
python3 tools/context-analyzer.py -j analysis.json

# Save report to file
python3 tools/context-analyzer.py -o optimization-report.md
```

### 📊 Generated Files

- **`prompt-index.json`**: Searchable metadata for all prompts
- **`prompt-dashboard.md`**: Quick reference guide

## Search Examples

```bash
# Find code-related prompts
./search "code"
./search -t coding optimization

# Get writing help
./search "article"
./search -c "tasks/writing"

# Explore vibecoding
./search --list-archetypes
./search -a "Truth Builder"

# Find similar prompts
./search -s "data analysis"

# Get task recommendations
./search -r "I need to debug Python code"

# Detailed results with descriptions
./search -v "machine learning"
```

## Advanced Usage

### Combining Searches
Use the search results to build prompt combinations:

1. Find base prompt: `./search "code review"`
2. Add framework: `./search "METRICS"`
3. Enhance with archetype: `./search -a "Truth Builder"`

### Maintenance
- Run `./update-index` after adding/modifying prompts
- Check `prompt-index.json` for indexing issues
- Use `-v` flag to verify descriptions are being extracted correctly

## Search Modes Explained

| Mode | Flag | Purpose | Example |
|------|------|---------|---------|
| Keyword | (default) | Full-text search | `./search "optimization"` |
| Tags | `-t` | Match specific tags | `./search -t debugging performance` |
| Category | `-c` | Filter by directory | `./search -c "frameworks"` |
| Archetype | `-a` | Vibecoding search | `./search -a "Clarity"` |
| Similar | `-s` | Find related prompts | `./search -s "article writer"` |
| Recommend | `-r` | Task-based suggestions | `./search -r "analyze logs"` |

## Integration with Git

Consider adding these to your git hooks:

```bash
# .git/hooks/post-merge
#!/bin/bash
./update-index

# .git/hooks/post-checkout
#!/bin/bash
./update-index
```

This ensures the search index stays current with repository changes.