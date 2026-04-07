# Claude Code Integration

Drop-in skills and CLAUDE.md configurations built on the AI Playbook frameworks. Copy what you need, customize to taste.

## Skills

Skills are markdown files with YAML frontmatter that Claude Code loads as slash commands. Place them in your project's `.claude/skills/<name>/SKILL.md` (recommended) or `.claude/commands/<name>.md` (legacy).

| Skill | Framework | What it does |
|-------|-----------|-------------|
| [clarity-architect.md](skills/clarity-architect.md) | Vibecoding | Structural simplicity — fortress-like clarity |
| [direct-mirror.md](skills/direct-mirror.md) | Vibecoding | Immediate insight — cut through confusion |
| [flow-director.md](skills/flow-director.md) | Vibecoding | Dynamic harmony — structured improvisation |
| [truth-builder.md](skills/truth-builder.md) | Vibecoding | Foundational rigor — first-principles analysis |
| [pattern-synthesizer.md](skills/pattern-synthesizer.md) | Vibecoding | Holistic integration — systems thinking |
| [wisdom-guide.md](skills/wisdom-guide.md) | Vibecoding | Ethical integration — stakeholder harmony |
| [creative-organizer.md](skills/creative-organizer.md) | Vibecoding | Aesthetic function — beautiful structure |
| [purpose-seeker.md](skills/purpose-seeker.md) | Vibecoding | Authentic discovery — find the real "why" |
| [adhd-optimize.md](skills/adhd-optimize.md) | ADHD Prompting | Rewrites any prompt for 40-60% token reduction |
| [context-audit.md](skills/context-audit.md) | Context Engineering | Audits conversation context efficiency |
| [fractal-decompose.md](skills/fractal-decompose.md) | Fractal | Macro/meso/micro problem decomposition |

## Example CLAUDE.md Configurations

Pre-built CLAUDE.md files that wire up the frameworks as default behavior:

| Config | Best for |
|--------|----------|
| [claude-md-adhd.md](examples/claude-md-adhd.md) | Any project (universal upgrade) |
| [claude-md-fullstack.md](examples/claude-md-fullstack.md) | Full-stack web development |
| [claude-md-research.md](examples/claude-md-research.md) | Research and analysis projects |

## Quick Setup

```bash
# Install a skill (recommended — skill directory format)
mkdir -p .claude/skills/adhd-optimize
cp ai-playbook/claude-code/skills/adhd-optimize.md .claude/skills/adhd-optimize/SKILL.md

# Or use the legacy commands directory
cp ai-playbook/claude-code/skills/adhd-optimize.md .claude/commands/adhd-optimize.md

# Now use it in Claude Code:
# /adhd-optimize "Your verbose prompt here"

# Or grab a full CLAUDE.md config
cp ai-playbook/claude-code/examples/claude-md-adhd.md CLAUDE.md
```

## How Skills Map to Frameworks

```
Vibecoding Archetypes ──► Persona skills (who the AI becomes)
ADHD Prompting ─────────► Optimization skills (how prompts are structured)
Context Engineering ────► Audit skills (measuring context efficiency)
Fractal Framework ──────► Decomposition skills (breaking down problems)
METRICS+ ───────────────► Analysis skills (layered evaluation)
```

## Creating Your Own

Any framework or archetype from this playbook can become a Claude Code skill:

1. Pick a framework from `frameworks/` or archetype from `tasks/vibecoding/`
2. Extract the system prompt or core methodology
3. Wrap it in a skill file with `$ARGUMENTS` for user input
4. Drop it in `.claude/commands/`

See [CONTRIBUTING.md](../CONTRIBUTING.md) for formatting guidelines.
