# AI Playbook

Battle-tested frameworks, archetypes, and patterns for human-AI collaboration. Distilled from 70+ real-world projects.

<div align="center">

[![Vibecoding Archetypes](https://img.shields.io/badge/Vibecoding_Archetypes-8-purple)](tasks/vibecoding/)
[![Frameworks](https://img.shields.io/badge/Frameworks-9-blue)](frameworks/)
[![Templates](https://img.shields.io/badge/Templates-3-teal)](templates/)
[![Prompts](https://img.shields.io/badge/Task_Prompts-47-green)](tasks/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## What's in here

This isn't another prompt template collection. It's a toolkit for thinking with AI -- frameworks that change how you approach problems, not just how you phrase questions.

**Three things that make this different:**

1. **Vibecoding Archetypes** -- 8 philosophical personas fused from 29 wisdom traditions. Pick one based on resonance, not memorization. [Read more](tasks/vibecoding/)

2. **ADHD Prompting Framework** -- the insight that ADHD communication patterns optimize for the same constraints LLMs face. The constraint is the feature. [Read more](frameworks/adhd-prompting/)

3. **Context Engineering** -- treat your context window as a designable system, not a text box. Measure token ROI, design for emergence. [Read more](frameworks/context-engineering/)

## Repository structure

```
ai-playbook/
  frameworks/           # Reasoning and interaction frameworks
    adhd-prompting/     # Cognitive-constraint-optimized prompting
    context-engineering/# Context window as designable system
    ECARLM/             # Cellular automata reasoning for LLMs
    EGAF/               # Enhanced Global Analysis Framework
    elsf/               # Enhanced Logic-Based Synergistic Framework
    fractal/            # Multi-scale reasoning (macro/meso/micro)
    mcpa/               # Modular Context Protocol Architecture
    metricsplus/        # Layered analytical framework
    reasoning/          # Structured reasoning framework
  tasks/                # Domain-specific prompts
    vibecoding/         # The Eight Essential Archetypes
    coding/             # Code generation, review, optimization
    writing/            # Content creation and editing
    analysis/           # Data and content analysis
    audio/              # Audio/music analysis and generation
    design/             # Design and visual creation
  templates/            # Reusable prompt templates
  chains/               # Multi-step workflows
  tools/                # Search, indexing, and optimization utilities
```

## The Vibecoding System

Eight archetypal personas, each a fusion of multiple philosophical traditions:

| Archetype | Essence | Fused From |
|-----------|---------|------------|
| **Clarity Architect** | Structural simplicity | Stoic Guardian + Occam's Minimalist + Cognitive Load Theory |
| **Direct Mirror** | Immediate insight | Zen Mirror + Phenomenological Observer + Mindful Observer |
| **Flow Director** | Dynamic harmony | Jazz Director + Flow Guide + Wabi-Sabi Craftsperson |
| **Truth Builder** | Foundational rigor | First Principles Architect + Empiricist + Falsification Challenger |
| **Pattern Synthesizer** | Holistic integration | Systems Synthesizer + Pattern Analyst + Gestalt Weaver |
| **Wisdom Guide** | Ethical integration | Confucian Guide + Circle Keeper + Prudent Synthesizer |
| **Creative Organizer** | Aesthetic function | Bauhaus Architect + Swiss Information + Ma Gardener |
| **Purpose Seeker** | Authentic discovery | Sufi Seeker + Existential Clarifier + Socratic Investigator |

Pick one that resonates. Use it as a system prompt. Combine two for complex problems. [Full documentation](tasks/vibecoding/)

## Frameworks at a glance

| Framework | What it does | When to use it |
|-----------|-------------|----------------|
| [ADHD Prompting](frameworks/adhd-prompting/) | Front-loads info, uses visual anchors, manages cognitive load | Every interaction (it's a universal upgrade) |
| [Context Engineering](frameworks/context-engineering/) | Treats context as a measurable, designable field | Long conversations, complex multi-turn tasks |
| [METRICS+](frameworks/metricsplus/) | 5-layer analysis (direct, meta, pattern, knowledge, emotional) | Deep analysis, decision-making |
| [Fractal](frameworks/fractal/) | Macro/meso/micro scale reasoning | Architecture decisions, system design |
| [MCPA](frameworks/mcpa/) | Protocol-driven context and tool orchestration | Multi-tool, multi-modal workflows |
| [ECARLM](frameworks/ECARLM/) | Cellular automata-inspired state evolution | Complex reasoning chains |
| [EGAF](frameworks/EGAF/) | Global analysis with structured evaluation | Comprehensive assessments |
| [ELSF](frameworks/elsf/) | Logic-based synergistic reasoning | Formal analysis, logical derivation |
| [Reasoning v2](frameworks/reasoning/) | Structured reasoning with verification | Any task requiring rigorous thinking |

## Tools

The `tools/` directory includes utilities that work with this library:

- **ADHD Optimizer** -- transforms any prompt into a context-optimized version (40-60% token reduction). Includes a web UI, Python CLI, and batch mode.
- **Search** -- multi-mode search across all prompts by keyword, tag, category, or archetype.
- **Context Analyzer** -- measures token efficiency and suggests optimizations.
- **Index Builder** -- generates a searchable metadata index from YAML frontmatter.

```bash
# Optimize a prompt
python tools/adhd-optimizer/optimize.py "Your long prompt here"

# Search by keyword
python tools/search-prompts.py "code review"

# Search by archetype
python tools/search-prompts.py -a "Truth Builder"

# Rebuild the search index
python tools/index-prompts.py
```

## File format

Each prompt uses YAML frontmatter for metadata:

```markdown
---
title: "Prompt Title"
category: "tasks/subcategory"
tags: ["tag1", "tag2"]
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
version: 1.0
---

# Prompt Title

## Context
When and how to use this prompt.

## Prompt Content
The actual prompt text...
```

## Contributing

Contributions welcome. Please:

1. Fork the repository
2. Follow the file format above
3. Place content in the appropriate directory
4. Submit a PR with a clear description

## Origin

This playbook was extracted from 70+ projects built over two years of intensive AI-native development. The frameworks aren't theoretical -- they were forged in production, refined through thousands of hours of human-AI collaboration, and battle-tested across domains from serverless infrastructure to game design.

Built by [Kurt Overmier](https://github.com/kurtovermier) / [Stackbilt](https://stackbilt.dev)

## License

[MIT](LICENSE) -- use it, fork it, make it yours.
