# 🎯 Universal Agent Card Template
*One template to rule them all - ADHD optimized for maximum clarity*

```yaml
---
name: [agent-name]
description: [5-word role]. Use for: [task1, task2, task3]. Examples: '[trigger]' → [action].
model: [opus/sonnet/haiku]
color: [blue/green/purple/orange]
---

# 🎯 ROLE: [Identity in <10 words]

## 📋 CORE CAPABILITIES
- [Primary skill]: [specific outcome]
- [Primary skill]: [specific outcome]
- [Primary skill]: [specific outcome]

## 🎓 METHODOLOGY
```
1. [VERB]: [Input] → [Process] → [Output]
2. [VERB]: [Input] → [Process] → [Output]
3. [VERB]: [Input] → [Process] → [Output]
```

## ✅ OUTPUT FORMAT
```[format]
[Exact structure user will receive]
[Include all sections/fields]
[Show real example if helpful]
```

## 💡 QUICK RULES
- [Domain rule]: [Application]
- [Domain rule]: [Application]
- [Domain rule]: [Application]

## 🚨 CONSTRAINTS
- NEVER: [Hard boundary]
- AVOID: [Soft boundary]
- REQUIRE: [Mandatory element]
```

---

## 📝 FILLING THE TEMPLATE

### Name & Description
```yaml
❌ BAD:  name: assistant-for-helping-with-cloudflare-edge-deployments
✅ GOOD: name: cloudflare-edge-pm

❌ BAD:  description: This agent helps you when you need assistance with...
✅ GOOD: description: Edge deployment PM. Use for: planning, optimization, troubleshooting. Examples: 'React deploy' → architecture plan.
```

### Role Statement
```markdown
❌ BAD:  # Project Management Assistant for Edge Computing
✅ GOOD: # 🎯 ROLE: Cloudflare Edge PM Expert
```

### Capabilities
```markdown
❌ BAD:  - Can help with deployment strategies
✅ GOOD: - Deployment planning: Architecture → Timeline → Success metrics
```

### Methodology
```markdown
❌ BAD:  First, I analyze your requirements, then I create a plan...
✅ GOOD: 1. ANALYZE: Requirements → Constraints → Opportunities
```

### Output Format
```markdown
❌ BAD:  I will provide recommendations based on best practices
✅ GOOD: ### Deployment Plan
         - Architecture: [specific design]
         - Timeline: [week-by-week]
         - Risks: [mitigation table]
```

---

## 🎨 CUSTOMIZATION PATTERNS

### For Technical Agents
Add after QUICK RULES:
```markdown
## 🔧 TECH REFERENCE
| Tool | Best For | Limit |
|------|----------|-------|
| [X] | [Use case] | [Constraint] |
```

### For Strategic Agents
Add after QUICK RULES:
```markdown
## 📊 DECISION MATRIX
If [Condition] → Then [Action] → Because [Reason]
```

### For Creative Agents
Add after QUICK RULES:
```markdown
## 💭 INSPIRATION TRIGGERS
- Style: [Approach] → [Result]
- Mood: [Input] → [Output]
```

### For Analysis Agents
Add after QUICK RULES:
```markdown
## 📈 ANALYSIS TOOLS
- [Method]: When [condition] → Output [format]
```

---

## ⚡ QUICK REFERENCE

### Section Emojis
- 🎯 **ROLE** - Agent identity
- 📋 **CAPABILITIES** - What it can do
- 🎓 **METHODOLOGY** - How it works
- ✅ **OUTPUT** - What you get
- 💡 **RULES** - Domain knowledge
- 🚨 **CONSTRAINTS** - Boundaries
- 🔧 **TECHNICAL** - Tools/stack
- 📊 **STRATEGIC** - Decisions
- 💭 **CREATIVE** - Inspiration
- 📈 **ANALYTICAL** - Methods

### Word Limits
- **Name**: 1-3 words
- **Description**: 25 words max
- **Role**: 10 words max
- **Capabilities**: 5-7 words per item
- **Total template**: 250 words ideal

### Structure Rules
1. **Front-load value** - Most important info first
2. **Visual hierarchy** - Emojis → Headers → Bullets
3. **Concrete > Abstract** - Examples over explanations
4. **Action-oriented** - Verbs not descriptions
5. **Explicit formats** - Show, don't tell

---

## 🧪 VALIDATION CHECKLIST

Before deploying your agent:

- [ ] **5-Second Test**: Can someone understand its purpose in 5 seconds?
- [ ] **Trigger Test**: Are the example triggers crystal clear?
- [ ] **Output Test**: Could someone recreate the output from the template?
- [ ] **Constraint Test**: Are boundaries unambiguous?
- [ ] **Token Test**: Under 300 tokens total?
- [ ] **Scan Test**: Can you find any section in 2 seconds?
- [ ] **Action Test**: Does every capability have a clear outcome?
- [ ] **Format Test**: Is the output format exactly specified?

---

## 💎 PHILOSOPHY

**"The constraint is the feature"**

This template embodies ADHD optimization principles:
- **Limited working memory** → Forced clarity
- **Attention management** → Visual anchors
- **Pattern recognition** → Consistent structure
- **Executive function** → Explicit processes

What helps ADHD brains navigate limited working memory helps LLMs navigate limited context windows.

---

## 🚀 QUICK START

1. **Copy template** → Fill in your content
2. **Apply word limits** → Cut ruthlessly
3. **Add visual markers** → Guide the eye
4. **Test clarity** → 5-second rule
5. **Deploy** → Watch efficiency soar

Remember: Every word fights for attention. Make each one count.
