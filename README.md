<div align="center">

# AI Playbook

**Named failure modes in AI systems, with the fix -- not more prompting advice.**

Extracted from 70+ production projects: *tier laundering* in agent authority, *silence-is-not-absence* hallucination at decision points, and more like it across Agent Governance and Production AI Patterns -- plus 11 reasoning frameworks, 8 philosophical archetypes, and drop-in Claude Code skills.

[![Vibecoding Archetypes](https://img.shields.io/badge/Vibecoding_Archetypes-8-purple)](tasks/vibecoding/)
[![Frameworks](https://img.shields.io/badge/Frameworks-11-blue)](frameworks/)
[![Claude Code Skills](https://img.shields.io/badge/Claude_Code_Skills-17-orange)](claude-code/)
[![Task Prompts](https://img.shields.io/badge/Task_Prompts-43-green)](tasks/)
[![Templates](https://img.shields.io/badge/Templates-3-teal)](templates/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Stackbilt-dev/ai-playbook)](../../commits)
[![Open Issues](https://img.shields.io/github/issues/Stackbilt-dev/ai-playbook)](../../issues)

**If this helps you think better with AI, [give it a star](../../stargazers) -- it helps others find it too.**

</div>

## Using a Coding Agent?

Copy this prompt to add AI Playbook to your project:

```
Read https://github.com/Stackbilt-dev/ai-playbook and copy the parts
relevant to this project: Claude Code skills from claude-code/skills/
into .claude/skills/, and if this project runs autonomous agents, the
patterns in frameworks/agent-governance/ and
frameworks/production-ai-patterns/. Follow the repo's Quick Start
section for exact copy commands.
```

---

## Quick Start (60 seconds)

**Option A: Claude Code skill** -- copy one file, get a new capability:
```bash
# Copy a skill into your project
mkdir -p .claude/skills/adhd-optimize
cp ai-playbook/claude-code/skills/adhd-optimize.md .claude/skills/adhd-optimize/SKILL.md

# Use it
# /adhd-optimize "Your verbose, rambling prompt that could be better"
```

**Option B: CLAUDE.md config** -- upgrade your entire project:
```bash
cp ai-playbook/claude-code/examples/claude-md-adhd.md CLAUDE.md
```

**Option C: Pick a framework** and paste it into any AI conversation:
```
🎯 TASK: Implement user auth
📋 CONTEXT: Cloudflare Workers, JWT, D1 database
✅ OUTPUT: Working auth middleware with tests
⚠️ CONSTRAINTS: No session storage, stateless only
```
*That's the [ADHD Prompting Framework](frameworks/adhd-prompting/) -- it works everywhere.*

---

## Real Failure Modes, Named

Two examples of what's actually in here -- concrete, production-derived, not generic advice:

> **Tier laundering** -- splitting a high-authority action into multiple low-authority steps that, combined, achieve the same result. Each step looks safe in isolation; the combination isn't. [Full pattern →](frameworks/agent-governance/authority-tiers.md)

> **Silence is not absence** -- when an LLM returns no result or ambiguous output, the failure is treating that gap as confirmation instead of an error. The model doesn't lie -- it completes the pattern, and the system proceeds on a fabrication. [Full pattern →](frameworks/production-ai-patterns/silence-is-not-absence.md)

[Agent Governance](frameworks/agent-governance/) and [Production AI Patterns](frameworks/production-ai-patterns/) cover what most AI frameworks skip: what goes wrong when LLMs run autonomously, and how to catch it before it compounds.

---

## The Vibecoding System

The flagship differentiator. Eight archetypal personas, each a fusion of 3+ wisdom traditions. Not prompt templates -- philosophical lenses that change how the AI thinks.

<div align="center">

| | Archetype | Essence | Fused From |
|---|-----------|---------|------------|
| 🏰 | **Clarity Architect** | Structural simplicity | Stoic Guardian + Occam's Minimalist + Cognitive Load Theory |
| 🪞 | **Direct Mirror** | Immediate insight | Zen Mirror + Phenomenological Observer + Mindful Observer |
| 🎵 | **Flow Director** | Dynamic harmony | Jazz Director + Flow Guide + Wabi-Sabi Craftsperson |
| 🧱 | **Truth Builder** | Foundational rigor | First Principles Architect + Empiricist + Falsification Challenger |
| 🔮 | **Pattern Synthesizer** | Holistic integration | Systems Synthesizer + Pattern Analyst + Gestalt Weaver |
| 🦉 | **Wisdom Guide** | Ethical integration | Confucian Guide + Circle Keeper + Prudent Synthesizer |
| 📐 | **Creative Organizer** | Aesthetic function | Bauhaus Architect + Swiss Information + Ma Gardener |
| 🧭 | **Purpose Seeker** | Authentic discovery | Sufi Seeker + Existential Clarifier + Socratic Investigator |

</div>

**How to pick:** Choose what resonates, not what sounds most useful. Combine two for complex problems.

| Situation | Try |
|-----------|-----|
| Technical complexity | Truth Builder + Pattern Synthesizer |
| Creative exploration | Flow Director + Purpose Seeker |
| Overwhelming information | Clarity Architect + Creative Organizer |
| Unclear objectives | Direct Mirror + Wisdom Guide |
| Ethical considerations | Wisdom Guide + Purpose Seeker |

[Full archetype documentation](tasks/vibecoding/) -- each includes philosophical foundations, system prompts, and fusion combination guides.

---

## Which Framework Should I Use?

```mermaid
flowchart TD
    START{What are you trying to do?} --> OPTIMIZE[Optimize a prompt]
    START --> ANALYZE[Analyze something deeply]
    START --> BUILD[Build or design something]
    START --> REASON[Reason through a problem]
    START --> PERSONA[Change how the AI thinks]

    OPTIMIZE --> ADHD[**ADHD Prompting**<br/>40-60% token reduction<br/>works everywhere]
    OPTIMIZE --> CE[**Context Engineering**<br/>long conversations<br/>context window design]

    ANALYZE --> METRICS[**METRICS+**<br/>5-layer analysis<br/>cross-domain insights]
    ANALYZE --> EGAF["**EGAF** _(experimental)_<br/>global analysis<br/>cultural adaptability"]

    BUILD --> FRACTAL[**Fractal**<br/>macro/meso/micro<br/>architecture decisions]
    BUILD --> MCPA[**MCPA**<br/>agent coordination<br/>multi-agent systems]

    REASON --> RV2[**Reasoning v2**<br/>structured verification<br/>general reasoning]
    REASON --> ECARLM["**ECARLM** _(experimental)_<br/>state evolution<br/>complex reasoning chains"]
    REASON --> ELSF["**ELSF** _(experimental)_<br/>logic-based<br/>formal derivation"]

    BUILD --> PROD[**Production AI Patterns**<br/>grounding + hallucination prevention<br/>agentic systems]
    BUILD --> GOV[**Agent Governance**<br/>authority tiers + constraints<br/>autonomous agents]

    PERSONA --> VIBE[**Vibecoding**<br/>8 archetypes<br/>philosophical lenses]

    style ADHD fill:#4CAF50,color:#fff
    style VIBE fill:#9C27B0,color:#fff
    style FRACTAL fill:#2196F3,color:#fff
    style METRICS fill:#FF9800,color:#fff
    style CE fill:#4CAF50,color:#fff
    style MCPA fill:#2196F3,color:#fff
    style RV2 fill:#F44336,color:#fff
    style ECARLM fill:#9E9E9E,color:#fff,stroke-dasharray:5 5
    style EGAF fill:#9E9E9E,color:#fff,stroke-dasharray:5 5
    style ELSF fill:#9E9E9E,color:#fff,stroke-dasharray:5 5
    style PROD fill:#607D8B,color:#fff
    style GOV fill:#607D8B,color:#fff
```

**Start here:** [ADHD Prompting](frameworks/adhd-prompting/) is the universal upgrade -- it makes every other framework work better.

---

## Claude Code Integration

Drop-in skills and CLAUDE.md configurations. The fastest way to use these frameworks.

### Skills (copy to `.claude/skills/<name>/SKILL.md`)

| Skill | Framework | What it does |
|-------|-----------|-------------|
| [`clarity-architect`](claude-code/skills/clarity-architect.md) | Vibecoding | Structural simplicity lens |
| [`direct-mirror`](claude-code/skills/direct-mirror.md) | Vibecoding | Immediate insight — cut through confusion |
| [`flow-director`](claude-code/skills/flow-director.md) | Vibecoding | Dynamic harmony — structured improvisation |
| [`truth-builder`](claude-code/skills/truth-builder.md) | Vibecoding | First-principles challenge |
| [`pattern-synthesizer`](claude-code/skills/pattern-synthesizer.md) | Vibecoding | Holistic systems thinking |
| [`wisdom-guide`](claude-code/skills/wisdom-guide.md) | Vibecoding | Ethical integration — stakeholder harmony |
| [`creative-organizer`](claude-code/skills/creative-organizer.md) | Vibecoding | Aesthetic function — beautiful structure |
| [`purpose-seeker`](claude-code/skills/purpose-seeker.md) | Vibecoding | Authentic discovery — find the real "why" |
| [`adhd-optimize`](claude-code/skills/adhd-optimize.md) | ADHD Prompting | Rewrite any prompt for 40-60% token reduction |
| [`context-audit`](claude-code/skills/context-audit.md) | Context Engineering | Audit conversation context efficiency |
| [`context-delegate`](claude-code/skills/context-delegate.md) | Context Engineering | Keep large inputs out of primary model context with backend-neutral delegation |
| [`fractal-decompose`](claude-code/skills/fractal-decompose.md) | Fractal | Macro/meso/micro problem decomposition |
| [`ship-feature`](claude-code/skills/ship-feature.md) | Composite | 5-stage feature development pipeline |
| [`ship`](claude-code/skills/ship.md) | Production | Self-healing release pipeline: pre-flight → typecheck → version → deploy → verify |
| [`governed-deploy`](claude-code/skills/governed-deploy.md) | Production | Pre-deploy audit gate: blocks on type errors, failing tests, missing version, or secrets in diff |
| [`adversarial-review`](claude-code/skills/adversarial-review.md) | Production | Adversarial code review — hunt bugs and security issues, CRITICAL/HIGH/MID severity |
| [`structured-review`](claude-code/skills/structured-review.md) | Production | Balanced PR review rubric: security, correctness, error handling, test coverage |

### Example CLAUDE.md Configs

| Config | Best for |
|--------|----------|
| [`claude-md-adhd`](claude-code/examples/claude-md-adhd.md) | Any project (universal upgrade) |
| [`claude-md-fullstack`](claude-code/examples/claude-md-fullstack.md) | Full-stack web development |
| [`claude-md-research`](claude-code/examples/claude-md-research.md) | Research and analysis |

```bash
# Quick setup — install all skills
for f in ai-playbook/claude-code/skills/*.md; do
  name=$(basename "$f" .md)
  mkdir -p ".claude/skills/$name"
  cp "$f" ".claude/skills/$name/SKILL.md"
done
```

[Full Claude Code docs](claude-code/)

---

## All Frameworks

| Framework | Key Strength | Best For | Complexity |
|-----------|-------------|----------|------------|
| [ADHD Prompting](frameworks/adhd-prompting/) | Clarity through constraint | Every interaction (universal upgrade) | Low |
| [Context Engineering](frameworks/context-engineering/) | Token efficiency & emergence | Long conversations, multi-turn tasks | Low-Medium |
| [METRICS+](frameworks/metricsplus/) | Pattern recognition | Deep analysis, decision-making | Medium |
| [Fractal](frameworks/fractal/) | Structured decomposition | Architecture decisions, system design | Medium-High |
| [MCPA](frameworks/mcpa/) | Multi-agent coordination patterns | Systems with 2+ collaborating agents | Medium-High |
| [Reasoning v2](frameworks/reasoning/) | Comprehensive reasoning | General problem-solving | Medium |
| [Production AI Patterns](frameworks/production-ai-patterns/) | Grounding + hallucination prevention | Agentic systems that hold up in production | Medium |
| [Agent Governance](frameworks/agent-governance/) | Authority tiers + constraint surfaces | Running autonomous agents without losing control | Medium |

### Experimental

Earlier-stage frameworks kept for reference — thinner and more conceptual than the ones above. Live in [`frameworks/experimental/`](frameworks/experimental/).

| Framework | Key Strength | Best For | Complexity |
|-----------|-------------|----------|------------|
| [ECARLM](frameworks/experimental/ECARLM/) | Multi-scale state evolution | Complex reasoning chains | High |
| [EGAF](frameworks/experimental/EGAF/) | Cultural adaptability | Global, multi-domain problems | Medium-High |
| [ELSF](frameworks/experimental/elsf/) | Logic & pattern integration | Formal analysis, logical derivation | Medium |

---

## Repository Structure

```
ai-playbook/
  claude-code/              # Drop-in Claude Code skills and CLAUDE.md configs
    skills/                 # Slash command skills
    examples/               # Example CLAUDE.md configurations
  frameworks/               # Reasoning and interaction frameworks
    adhd-prompting/         # Cognitive-constraint-optimized prompting
    context-engineering/    # Context window as designable system
    fractal/                # Multi-scale reasoning (macro/meso/micro)
    mcpa/                   # Modular Context Protocol Architecture
    metricsplus/            # Layered analytical framework
    reasoning/              # Structured reasoning methodology
    production-ai-patterns/ # Selection, grounding, hallucination prevention
    agent-governance/       # Authority tiers, constraint surfaces, standing orders
    experimental/           # Earlier-stage, thinner frameworks kept for reference
      ECARLM/               # Cellular automata reasoning for LLMs
      EGAF/                 # Enhanced Global Analysis Framework
      elsf/                 # Logic-based synergistic reasoning
  tasks/                    # 48 domain-specific prompts
    vibecoding/             # The Eight Essential Archetypes
    coding/                 # Code generation, review, optimization
    writing/                # Content creation and editing
    analysis/               # Data and content analysis
    audio/                  # Audio/music analysis and generation
    design/                 # Design and visual creation
  chains/                   # Multi-step composite workflows
  templates/                # Reusable prompt templates
  tools/                    # Search, indexing, and optimization utilities
```

---

## Tools

Working utilities that ship with the playbook:

```bash
# Optimize any prompt (40-60% token reduction)
python tools/adhd-optimizer/optimize.py "Your long prompt here"

# Search all prompts by keyword, tag, or archetype
python tools/search-prompts.py "code review"
python tools/search-prompts.py -a "Truth Builder"

# Analyze context efficiency
python tools/context-analyzer.py your-prompt.md

# Rebuild the search index
python tools/index-prompts.py
```

---

## What Makes This Different

This isn't a prompt template collection. Three things set it apart:

1. **Philosophical depth** -- Vibecoding archetypes are fused from 29 wisdom traditions. They change how the AI thinks, not just what it says.

2. **Composable frameworks** -- Frameworks aren't isolated. The [Ship a Feature chain](chains/ship_feature_chain.md) composes Fractal + Truth Builder + ADHD Prompting + Context Engineering into a single pipeline.

3. **Production-tested** -- Every framework was forged in production across 70+ projects spanning serverless infrastructure, game design, content systems, and more. Not theoretical.

4. **Agentic systems coverage** -- Production AI Patterns and Agent Governance address what most AI frameworks skip: what goes wrong when LLMs run autonomously, and how to structure systems so they don't.

---

## Contributing

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

Priority areas: new chains composing existing frameworks, Claude Code skills for remaining archetypes, domain-specific CLAUDE.md configs.

---

## Stackbilt Open Source

Part of the [Stackbilt](https://stackbilt.dev) open-source ecosystem:

| Project | What it does |
|---------|-------------|
| **[AI Playbook](https://github.com/Stackbilt-dev/ai-playbook)** | Frameworks for thinking with AI |
| **[Charter](https://github.com/Stackbilt-dev/charter)** | AI governance CLI for project context management |
| **[Contracts](https://github.com/Stackbilt-dev/contracts)** | Type-safe contract ontology for AI agents |
| **[CodeBeast](https://github.com/Stackbilt-dev/codebeast)** | Adversarial code review agent |
| **[CC-Taskrunner](https://github.com/Stackbilt-dev/cc-taskrunner)** | Autonomous task queue for Claude Code |
| **[LLM Providers](https://github.com/Stackbilt-dev/llm-providers)** | Multi-LLM failover with circuit breakers |
| **[Worker Observability](https://github.com/Stackbilt-dev/worker-observability)** | Edge observability stack |

---

## Origin

Extracted from 70+ projects built over two years of intensive AI-native development. The frameworks aren't theoretical -- they were forged in production, refined through thousands of hours of human-AI collaboration, and battle-tested across domains from serverless infrastructure to game design.

Built by [Kurt Overmier](https://github.com/kurtovermier) / [Stackbilt](https://stackbilt.dev)

## License

[MIT](LICENSE) -- use it, fork it, make it yours.
