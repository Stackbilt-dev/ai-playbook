# AI Reasoning Frameworks

This directory contains advanced structured reasoning frameworks for AI language models. Unlike standard prompts that focus on specific tasks, frameworks provide comprehensive methodologies for approaching complex problems, enhancing reasoning capabilities, and improving output quality across multiple domains.

## What Are AI Reasoning Frameworks?

AI reasoning frameworks are structured approaches that guide language models through specific cognitive processes. They provide:

1. **Structured Thinking**: Predefined pathways for processing information
2. **Multi-scale Analysis**: Approaches to break down complex problems
3. **Quality Assurance**: Built-in validation and verification steps
4. **Enhanced Reasoning**: Methods to improve logical consistency
5. **Domain Transferability**: Techniques that work across multiple fields

These frameworks are particularly valuable when working with complex problems that require structured reasoning, multi-step analysis, or specialized processing methodologies.

## When to Use Frameworks vs. Regular Prompts

| Use Frameworks When | Use Regular Prompts When |
|---------------------|--------------------------|
| Solving complex, multi-faceted problems | Completing specific, well-defined tasks |
| Requiring highly structured reasoning | Needing quick, straightforward responses |
| Working across multiple domains | Focusing on a single domain or task type |
| Needing consistent methodology | Preferring flexibility in approach |
| Building reasoning systems | Creating content or performing analysis |

## Framework Structure

Each framework in this library follows a standardized format:

1. **Theoretical Foundation**: The underlying principles and theories
2. **Processing Layers**: The specific cognitive layers or stages
3. **Implementation Guide**: How to apply the framework in practice
4. **Use Cases**: Examples of when the framework excels
5. **Limitations**: Understanding when the framework may not be optimal

## Available Frameworks

### Context Optimization Frameworks
Revolutionary approaches to prompt engineering:
- **[Context Engineering](./context-engineering/)** - Transform prompts into dynamic, efficient context fields
- **[ADHD Prompting](./adhd-prompting/)** - Context optimization through cognitive constraint patterns

### Decision-Making Frameworks
Frameworks optimized for structured decision processes:
- **[Enhanced Global Analysis Framework (EGAF)](./experimental/EGAF/)** _(experimental)_ - Context and constraints checklist; cross-context validity is not yet evaluated
- **[Enhanced Logic-Based Synergistic Framework (ELSF)](./experimental/elsf/)** _(experimental)_ - Claim and pattern separation; formal semantics are not yet specified

### Problem-Solving Frameworks
Frameworks focused on systematic problem decomposition and resolution:
- **[ECARLM](./experimental/ECARLM/)** _(experimental)_ - Iterative state-update concept; no implementation or benchmark is included
- **[METRICS+](./metricsplus/)** - Layered analytical framework with pattern recognition
- **[Fractal Framework](./fractal/)** - Multi-scale hierarchical analysis
- **[Reasoning v2](./reasoning/)** - Comprehensive reasoning methodology

### Multi-Actor Coordination
Pattern language for systems where agents, deterministic services, humans, policies, state machines, and external tools share an outcome:
- **[MCPA — Multi-Actor Coordination Pattern Architecture](./mcpa/)** - Coordination, durable lifecycle state, evidence, authority, commitment, and workflow evaluation

### Experimental Frameworks

Read the [experimental maturity index](./experimental/) before using ECARLM, EGAF, or ELSF. Experimental entries are research inputs rather than recommended defaults. Promotion requires bounded semantics, representative evaluation, observable failure behavior, and an explicit authority boundary.

The useful kernels are synthesized into an applied decision discipline in [*The Shape of Judgment*](../field-guides/the-shape-of-judgment/).

## Framework Comparison

| Framework | Key Strength | Best For | Complexity |
|-----------|--------------|----------|------------|
| Context Engineering | Token efficiency & emergence | All prompts - optimization layer | Low-Medium |
| ADHD Prompting | Clarity through constraint | Token optimization & consistency | Low |
| ECARLM _(experimental)_ | Iterative state updates | Testable reasoning research | High |
| EGAF _(experimental)_ | Context and constraints | Testable contextual analysis | Medium-High |
| ELSF _(experimental)_ | Claim and pattern separation | Testable claim audit | Medium |
| Fractal | Structured decomposition | Hierarchical problems | Medium-High |
| METRICS+ | Pattern recognition | Cross-domain insights | Medium |
| Reasoning v2 | Comprehensive reasoning | General problem solving | Medium |
| MCPA | Multi-actor governed workflows | Durable work with agents, services, humans, or effects | Medium-High |

## How to Use These Frameworks

1. **Selection**: Choose the appropriate framework based on your problem type
2. **Implementation**: Apply the framework's structure to your specific prompt
3. **Execution**: Guide the AI through the framework's reasoning processes
4. **Validation**: Use the framework's built-in validation methods
5. **Refinement**: Iterate based on results to improve outcomes

## Framework Selection Guide

To choose the right framework:

1. **Identify your problem type**: 
   - Is it analytical, creative, or decision-based?
   - Does it require multi-scale thinking?
   - Is formal logic central to the solution?

2. **Assess complexity**:
   - Simpler problems may not require full frameworks
   - Highly complex problems benefit from structured approaches

3. **Consider domain**:
   - Some frameworks excel in specific domains
   - Others are designed for cross-domain application

4. **Evaluate constraints**:
   - Time limitations may favor simpler frameworks
   - Quality requirements may necessitate more complex ones

## Creating New Frameworks

When developing new reasoning frameworks:

1. Follow the standardized format with YAML frontmatter
2. Clearly define the theoretical foundation
3. Provide explicit processing stages or layers
4. Include implementation examples
5. Document limitations and ideal use cases
6. Consider how the framework integrates with other approaches

## Best Practices

- **Framework Combination**: Sometimes combining elements from multiple frameworks produces better results
- **Simplification**: For less complex problems, consider simplified versions of these frameworks
- **Documentation**: When using a framework, document which aspects were most effective
- **Iteration**: Frameworks can be refined based on application results
- **Context Setting**: Always clearly communicate the framework to the AI model

These frameworks represent advanced approaches to enhancing AI reasoning capabilities. By understanding their strengths and appropriate applications, you can significantly improve problem-solving outcomes across a wide range of domains.
