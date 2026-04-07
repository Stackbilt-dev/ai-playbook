"""
Shared fixtures and helpers for ai-playbook tests.

The ADHDPromptOptimizer lives inside a markdown file (optimizer.py is actually
markdown with fenced Python code blocks), so we extract and exec the class at
import time rather than doing a normal Python import.
"""

import re
import sys
import json
import types
import tempfile
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Extract ADHDPromptOptimizer from the markdown-formatted optimizer.py
# ---------------------------------------------------------------------------
TOOLS_DIR = Path(__file__).resolve().parent.parent / "tools"

def _load_adhd_optimizer_class():
    """Extract Python from the fenced code block in optimizer.py and return the class."""
    optimizer_md = TOOLS_DIR / "adhd-optimizer" / "optimizer.py"
    content = optimizer_md.read_text(encoding="utf-8")

    # Pull the first ```python ... ``` block
    match = re.search(r"```python\n(.*?)```", content, re.DOTALL)
    if not match:
        raise RuntimeError("Could not extract Python code from optimizer.py")

    code = match.group(1)
    namespace = {}
    exec(compile(code, str(optimizer_md), "exec"), namespace)
    return namespace["ADHDPromptOptimizer"]


# Make the class available as a module-level import for test files
ADHDPromptOptimizer = _load_adhd_optimizer_class()


# ---------------------------------------------------------------------------
# Ensure tools/ is importable so search-prompts.py and context-analyzer.py work
# ---------------------------------------------------------------------------
sys.path.insert(0, str(TOOLS_DIR))


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def optimizer():
    """Return a fresh ADHDPromptOptimizer instance."""
    return ADHDPromptOptimizer()


@pytest.fixture
def sample_index(tmp_path):
    """Create a minimal prompt-index.json and return its path."""
    index = {
        "metadata": {
            "created": "2026-01-01T00:00:00",
            "total_prompts": 3,
            "categories": {"coding": 2, "writing": 1},
            "tags": {"python": 2, "creative": 1, "api": 1},
            "archetypes": ["The Architect"],
        },
        "prompts": [
            {
                "title": "Python API Builder",
                "path": "coding/python-api.md",
                "category": "coding",
                "tags": ["python", "api"],
                "description": "Build REST APIs with Python and FastAPI.",
                "archetype": "The Architect",
                "core_principle": "Structure first",
            },
            {
                "title": "Python Test Writer",
                "path": "coding/python-tests.md",
                "category": "coding",
                "tags": ["python", "testing"],
                "description": "Generate pytest test suites from source code.",
            },
            {
                "title": "Blog Post Generator",
                "path": "writing/blog-post.md",
                "category": "writing",
                "tags": ["creative", "content"],
                "description": "Create engaging blog posts on technical topics.",
            },
        ],
    }
    index_path = tmp_path / "prompt-index.json"
    index_path.write_text(json.dumps(index, indent=2), encoding="utf-8")
    return str(index_path)


@pytest.fixture
def sample_prompt_file(tmp_path):
    """Create a sample markdown prompt file with YAML frontmatter."""
    content = """\
---
title: Sample Prompt
category: coding
tags:
  - python
  - testing
---

## Context

You are a senior Python developer reviewing code for quality.

## Task

Review the provided code and suggest improvements.

## Instructions

1. Check for PEP 8 compliance
2. Look for potential bugs
3. Suggest performance improvements

## Example

For instance, consider this function:

```python
def add(a, b):
    return a + b
```

## Constraints

- Must not exceed 500 tokens
- Avoid unnecessary verbosity
"""
    filepath = tmp_path / "sample-prompt.md"
    filepath.write_text(content, encoding="utf-8")
    return filepath
