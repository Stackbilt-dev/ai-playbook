# 📝 Prompt Templates

## Overview

This directory contains reusable, optimized templates for creating various types of prompts and AI interactions. Unlike task-specific prompts, these templates provide structured frameworks that can be adapted to multiple use cases.

## Philosophy

**"The constraint is the feature"** - All templates follow ADHD optimization principles, treating cognitive and token constraints as design advantages rather than limitations.

## Available Templates

### 🎯 Universal Agent Card (`universal-agent-card.md`)

**Purpose**: Standardized template for creating AI agent personas and capabilities

**Key Features**:
- ADHD-optimized with strict word limits
- 5-second comprehension test
- Token optimization (<300 tokens)
- Visual hierarchy using emojis
- Built-in validation checklist

**When to Use**:
- Designing new AI agents or assistants
- Standardizing agent documentation
- Creating consistent agent libraries
- Rapid prototyping of agent capabilities

**Example Output**:
```yaml
name: code-reviewer
description: Code quality guardian. Use for: reviews, refactoring, standards. 
            Examples: 'check PR' → detailed analysis.
```

---

### 🗺️ Visual Prompt Patterns (`visual-prompt-patterns.md`)

**Purpose**: Transform visual thinking structures (mind maps, diagrams) into text-based prompts

**Patterns Included**:
1. Radial/Mind Map structures
2. Hierarchical trees
3. Flow diagrams
4. Matrix structures
5. Layered context (onion model)
6. Network graphs
7. Quadrant analysis
8. Nested context boxes

**When to Use**:
- Complex system design requiring spatial organization
- Multi-faceted problems needing visual hierarchy
- Converting whiteboard sessions to prompts
- Preserving relationships between concepts

**Example Pattern**:
```markdown
🎯 CENTER: API Design
├── 🔵 ENDPOINTS: CRUD operations
├── 🟢 VALIDATION: Input checking
├── 🟡 SECURITY: Auth & rate limiting
└── 🔴 ERRORS: Handling strategies
```

---

### 🎙️ ElevenLabs Conversational AI (`elevenlabs-conversational-ai.md`)

**Purpose**: Design natural, human-like conversational AI agents for voice interactions

**Key Features**:
- Emotional state detection patterns
- Natural language phrase banks
- Progressive information gathering
- TTS (Text-to-Speech) optimization
- LLM selection matrix
- Pre-deployment testing checklist

**When to Use**:
- Building voice-enabled AI assistants
- Customer service chatbots
- Interactive voice response (IVR) systems
- Any conversational AI requiring natural dialogue

**Core Principle**: "Conversation over script" - Agents should feel like talking to a knowledgeable colleague, not navigating a phone tree.

---

## Template Selection Guide

| Need | Recommended Template | Why |
|------|---------------------|-----|
| Create an AI assistant | Universal Agent Card | Structured, comprehensive agent design |
| Design complex system | Visual Prompt Patterns | Preserves spatial relationships |
| Build voice interface | ElevenLabs Conversational | Natural dialogue optimization |
| Optimize token usage | Universal Agent Card | Built-in token constraints |
| Convert diagrams to text | Visual Prompt Patterns | Multiple pattern options |
| Handle emotional users | ElevenLabs Conversational | Emotion detection built-in |

## How to Use Templates

### 1. Choose Your Template
Review the available templates and select based on your specific need.

### 2. Copy the Structure
Each template provides copy-paste ready structures. Start with the base template.

### 3. Fill in Your Content
Follow the guidelines and examples provided. Pay attention to:
- Word limits (where specified)
- Required vs optional sections
- Format specifications

### 4. Validate
Use built-in checklists to ensure quality:
- 5-second comprehension test
- Token count verification
- Completeness check

### 5. Iterate
Templates are starting points. Customize based on:
- Specific domain requirements
- User feedback
- Performance metrics

## Best Practices

### DO:
- ✅ Start with templates for consistency
- ✅ Respect word/token limits
- ✅ Use visual anchors (emojis) consistently
- ✅ Test with real scenarios
- ✅ Combine templates when needed

### DON'T:
- ❌ Override core structure without reason
- ❌ Ignore validation checklists
- ❌ Add complexity unnecessarily
- ❌ Mix incompatible patterns
- ❌ Forget the 5-second rule

## Creating New Templates

When adding new templates to this directory:

1. **Follow the Format**:
   ```markdown
   # 🎯 Template Name
   *One-line description*
   
   ## Purpose
   ## Key Features
   ## When to Use
   ## Template Structure
   ## Examples
   ## Best Practices
   ```

2. **Include Metadata**:
   - YAML frontmatter
   - Version number
   - Creation date
   - Tags

3. **Provide Examples**:
   - Good vs bad comparisons
   - Real-world applications
   - Common variations

4. **Add Validation**:
   - Checklists
   - Success criteria
   - Common pitfalls

## Integration with Frameworks

Templates work best when combined with frameworks:

| Template | Pairs Well With | Result |
|----------|----------------|--------|
| Universal Agent Card | Vibecoding Archetypes | Philosophically-grounded agents |
| Visual Patterns | ADHD Framework | Maximum clarity and scanning |
| ElevenLabs | Context Engineering | Token-optimized conversations |

## Token Optimization Tips

All templates emphasize token efficiency:

1. **Front-load critical info** - Most important first
2. **Use structure over prose** - Lists beat paragraphs
3. **Employ visual markers** - Emojis = instant recognition
4. **Progressive disclosure** - Details only when needed
5. **Explicit > Implicit** - State everything clearly

## Community Contributions

We welcome new templates! Consider submitting templates for:
- Specific industries (healthcare, finance, education)
- Specialized tasks (data analysis, creative writing)
- New AI platforms (OpenAI, Anthropic, Google)
- Novel interaction patterns

## Resources

- [ADHD Prompting Framework](../frameworks/adhd-prompting/)
- [Context Engineering](../frameworks/context-engineering/)
- [Vibecoding System](../tasks/vibecoding/)
- [Search Tools](../tools/)

---

Remember: **Great templates make complex simple and simple powerful.**
