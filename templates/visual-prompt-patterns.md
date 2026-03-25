# 🗺️ Visual Prompt Patterns
*Transform mind map structures into text-based prompts*

## Core Concept
Visual information structures (mind maps, diagrams, flowcharts) can be translated into text prompts that preserve spatial relationships and hierarchical organization, improving both human comprehension and LLM processing.

## Pattern Library

### 1. Radial Structure (Mind Map Style)
```markdown
🎯 CENTER: [Main Objective]
├── 🔵 BRANCH_1: [Primary Aspect]
│   ├── Detail: [Specific requirement]
│   ├── Detail: [Constraint]
│   └── Detail: [Resource]
├── 🟢 BRANCH_2: [Secondary Aspect]
│   ├── Detail: [Implementation]
│   └── Detail: [Validation]
├── 🟡 BRANCH_3: [Support Aspect]
│   └── Detail: [Documentation]
└── 🔴 BRANCH_4: [Risk Management]
    ├── Detail: [Mitigation]
    └── Detail: [Contingency]
```

### 2. Hierarchical Tree
```markdown
ROOT: [System Name]
├── LAYER_1: Infrastructure
│   ├── Component: Database
│   │   ├── Type: PostgreSQL
│   │   └── Scale: 100GB
│   └── Component: Cache
│       ├── Type: Redis
│       └── TTL: 3600s
├── LAYER_2: Application
│   ├── Service: API
│   └── Service: Worker
└── LAYER_3: Interface
    ├── Web: React
    └── Mobile: React Native
```

### 3. Flow Diagram Translation
```markdown
START → [Initial State]
  ↓
DECISION: [Condition check]
  ├─YES→ ACTION: [Primary path]
  │       ↓
  │     PROCESS: [Transform data]
  │       ↓
  │     OUTPUT: [Result A]
  └─NO→  ACTION: [Alternative path]
          ↓
        OUTPUT: [Result B]
```

### 4. Matrix Structure
```markdown
┌──────────┬──────────┬──────────┐
│ DIMENSION│  OPTION A │  OPTION B │
├──────────┼──────────┼──────────┤
│ Speed    │  ⚡ Fast  │  🐢 Slow  │
│ Cost     │  💰 High  │  💵 Low   │
│ Quality  │  ⭐ Good  │  ⭐⭐ Best │
└──────────┴──────────┴──────────┘
```

### 5. Layered Context (Onion Model)
```markdown
CORE: [Essential requirement]
  LAYER_1: [Direct dependencies]
    LAYER_2: [Supporting context]
      LAYER_3: [Nice-to-have details]
        OUTER: [Optional enhancements]
```

### 6. Network Graph
```markdown
NODE[A]: Authentication
  ←→ NODE[B]: User Service
  ←→ NODE[C]: Permission Service
  
NODE[B]: User Service
  ←→ NODE[D]: Database
  ←→ NODE[E]: Cache
  
NODE[C]: Permission Service
  ←→ NODE[D]: Database
  ←→ NODE[F]: Audit Log
```

### 7. Quadrant Analysis
```markdown
        HIGH IMPACT ↑
            │
    Q1: 🔥  │  Q2: 💎
    URGENT  │  IMPORTANT
   ─────────┼─────────→
    Q3: 📋  │  Q4: 🗑️
    ROUTINE │  ELIMINATE
            │
        LOW IMPACT ↓
```

### 8. Nested Context Boxes
```markdown
╔════════════════════════════════╗
║ CONTEXT: Production Environment ║
║ ╔════════════════════════════╗ ║
║ ║ SYSTEM: E-commerce Platform ║ ║
║ ║ ╔════════════════════════╗ ║ ║
║ ║ ║ COMPONENT: Checkout     ║ ║ ║
║ ║ ║ • Payment processing    ║ ║ ║
║ ║ ║ • Inventory check       ║ ║ ║
║ ║ ╚════════════════════════╝ ║ ║
║ ╚════════════════════════════╝ ║
╚════════════════════════════════╝
```

## Usage Patterns

### Pattern Selection Guide

| Visual Structure | Best For | Example Use Case |
|-----------------|----------|------------------|
| Radial/Mind Map | Multi-faceted problems | System design, brainstorming |
| Hierarchical Tree | Component breakdown | Architecture, org structure |
| Flow Diagram | Process visualization | Workflows, algorithms |
| Matrix | Comparison/evaluation | Decision making, analysis |
| Layered/Onion | Priority levels | Requirements gathering |
| Network Graph | Relationships | Dependencies, integrations |
| Quadrant | Categorization | Task prioritization |
| Nested Boxes | Contextual scoping | System boundaries |

### Implementation Tips

1. **Color Coding with Emojis**
   - 🔵 Blue = Primary/Core
   - 🟢 Green = Secondary/Support
   - 🟡 Yellow = Caution/Consider
   - 🔴 Red = Risk/Constraint
   - ⚪ Gray = Optional/Future

2. **Depth Indicators**
   - Use indentation levels
   - Apply tree symbols (├── └──)
   - Number layers explicitly
   - Use size indicators (CAPS → normal → small)

3. **Relationship Markers**
   - `→` One-way dependency
   - `←→` Bidirectional relationship
   - `⇒` Transformation/Result
   - `↔` Interchangeable
   - `⊃` Contains/Includes

4. **Status Indicators**
   - ✅ Complete/Verified
   - ⚠️ Warning/Attention
   - 🚧 In Progress
   - ❌ Blocked/Failed
   - 💡 Idea/Suggestion

## Advanced Patterns

### Dynamic Expansion
```markdown
OVERVIEW: System Architecture
├── [+] Frontend (click to expand)
├── [-] Backend (expanded)
│   ├── API Gateway
│   ├── Microservices
│   └── Database Layer
└── [+] Infrastructure
```

### Weighted Relationships
```markdown
Component A ═══► Component B  (Strong dependency)
Component C ──► Component D   (Weak dependency)
Component E ···► Component F  (Optional link)
```

### Time-Based Progression
```markdown
T0: Initial State
 ↓ [2 hours]
T1: Data Collection
 ↓ [1 day]
T2: Processing
 ↓ [3 hours]
T3: Review
 ↓ [30 min]
T4: Deployment
```

## Integration with ADHD Framework

These visual patterns complement ADHD prompting by:
- **Reducing cognitive load** through spatial organization
- **Creating visual anchors** for quick scanning
- **Establishing clear hierarchies** for priority processing
- **Enabling progressive disclosure** through nested structures

## Examples

### Example 1: API Development Mind Map
```markdown
🎯 API: User Management
├── 🔵 ENDPOINTS
│   ├── GET /users → List all
│   ├── POST /users → Create new
│   └── PUT /users/:id → Update
├── 🟢 VALIDATION
│   ├── Email: RFC compliant
│   └── Password: 8+ chars
├── 🟡 SECURITY
│   ├── Auth: JWT tokens
│   └── Rate: 100 req/min
└── 🔴 ERRORS
    ├── 400: Bad request
    └── 401: Unauthorized
```

### Example 2: Decision Tree
```markdown
PROBLEM: Slow database queries
  ↓
CHECK: Query complexity?
  ├─COMPLEX→ ADD: Indexes
  │           ↓
  │         TEST: Performance
  │           ├─GOOD→ ✅ DONE
  │           └─BAD→ OPTIMIZE: Query
  └─SIMPLE→ CHECK: Data volume?
            ├─HIGH→ IMPLEMENT: Caching
            └─LOW→ INVESTIGATE: Network
```

## Best Practices

1. **Maintain Visual Consistency**
   - Use same symbols throughout
   - Keep indentation uniform
   - Apply color coding consistently

2. **Balance Detail and Overview**
   - Start with high-level structure
   - Add details progressively
   - Use expansion markers for deep content

3. **Optimize for Scanning**
   - Front-load important information
   - Use visual markers as anchors
   - Keep line lengths manageable

4. **Test Readability**
   - Ensure structure is clear in plain text
   - Verify hierarchy is obvious
   - Check that relationships are apparent

Remember: The goal is to translate visual thinking into text that preserves spatial relationships and enhances understanding for both humans and AI.
