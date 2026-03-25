# Contributing to AI Playbook

Thanks for your interest in contributing. This playbook grows through real-world usage, so practical contributions are especially valued.

## How to contribute

### Adding a new prompt

1. Create a markdown file in the appropriate `tasks/` subdirectory
2. Use the YAML frontmatter format (see [README](README.md#file-format))
3. Include a `## Context` section explaining when to use it
4. Name files with lowercase and hyphens: `my-new-prompt.md`

### Adding a framework

1. Create a directory under `frameworks/`
2. Include a `README.md` with overview, core concepts, and usage examples
3. Keep frameworks self-contained -- they should work independently

### Improving existing content

- Fix typos, clarify explanations, add examples
- Update outdated references
- Add real-world usage notes from your own experience

## Guidelines

- **Practical over theoretical** -- show how things work, not just what they are
- **Concise over comprehensive** -- shorter docs get read more
- **Examples over descriptions** -- a good example beats a paragraph of explanation
- **Test your prompts** -- verify they work with at least one major LLM before submitting

## Process

1. Fork the repo
2. Create a branch (`add-my-framework` or `fix-typo-in-adhd-docs`)
3. Make your changes
4. Submit a PR with a clear description of what you added/changed and why

## Code of conduct

Be respectful, be constructive, be practical. We're all here to make AI interaction better.
