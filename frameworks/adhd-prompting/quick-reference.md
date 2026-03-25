# ADHD Prompting: Quick Reference Card

## The 10-Second Template
```
🎯 TASK: [what you want]
📋 CONTEXT: [key facts]
✅ OUTPUT: [expected result]
```

## Essential Emojis
- 🎯 **TASK/GOAL** - Main objective
- 📋 **CONTEXT** - Background info
- ✅ **OUTPUT/SUCCESS** - Expected result
- ⚠️ **CONSTRAINTS** - Limitations
- 🚫 **AVOID** - What not to do
- 🔧 **TOOLS/STACK** - Technologies
- 💡 **APPROACH** - How to solve
- 🐛 **BUG/ISSUE** - Problem description
- ⏱️ **TIME** - Deadline/duration
- 📊 **DATA** - Input/metrics

## Power Patterns

### Pattern 1: Front-Load
```
❌ "I've been working on..."
✅ "TASK: Fix auth bug"
```

### Pattern 2: Bullet Lists
```
❌ Long paragraph explaining needs
✅ NEED:
   - Feature X
   - Performance Y
   - Security Z
```

### Pattern 3: Explicit State
```
❌ "Using the setup from before..."
✅ "CURRENT: DB connected (Postgres 15)"
```

### Pattern 4: Progressive Detail
```
MAIN: Deploy app
├── Stack: Node + React
├── Target: Cloudflare
└── <details>Config...</details>
```

## Format Transformations

| Traditional | ADHD-Optimized |
|-------------|----------------|
| "Create a function that..." | `FUNC: name \| IN: type \| OUT: type` |
| "I need help with..." | `🎯 TASK:` |
| "It should include..." | `✅ REQUIREMENTS:` |
| "Make sure not to..." | `🚫 AVOID:` |
| "Using X technology..." | `🔧 STACK: X` |

## Copy-Paste Templates

### Debug Template
```
🐛 BUG: 
📍 WHERE: 
🔍 TRIED: 
💭 THEORY: 
❓ NEED: 
```

### Build Template
```
🎯 BUILD: 
🔧 STACK: 
📋 FEATURES:
- 
- 
⚠️ CONSTRAINTS: 
✅ SUCCESS WHEN: 
```

### Learn Template
```
📚 LEARN: 
🎓 LEVEL: 
🎯 GOAL: 
⏱️ TIME: 
💡 STYLE: [examples/theory]
```

## Why It Works
1. **Less tokens** → Cheaper API calls
2. **Clear structure** → Consistent outputs  
3. **Visual anchors** → Easy scanning
4. **No ambiguity** → Fewer errors
5. **Explicit needs** → Better results

## Remember
> "The constraint is the feature" - What helps ADHD brains navigate limited working memory helps LLMs navigate limited context windows.