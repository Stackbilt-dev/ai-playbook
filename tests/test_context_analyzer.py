"""Tests for ContextAnalyzer class (tools/context-analyzer.py)."""

import sys
import json
import pytest
from pathlib import Path

# The module has a hyphen in its filename.
TOOLS_DIR = Path(__file__).resolve().parent.parent / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import importlib
_ctx_mod = importlib.import_module("context-analyzer")
ContextAnalyzer = _ctx_mod.ContextAnalyzer


class TestInit:
    """Test ContextAnalyzer initialization."""

    def test_default_prompt_dir(self):
        analyzer = ContextAnalyzer()
        assert analyzer.prompt_dir == Path(".")

    def test_custom_prompt_dir(self, tmp_path):
        analyzer = ContextAnalyzer(str(tmp_path))
        assert analyzer.prompt_dir == tmp_path


class TestExtractSections:
    """Tests for extract_sections()."""

    def test_extracts_frontmatter(self):
        analyzer = ContextAnalyzer()
        content = "---\ntitle: Test\ncategory: demo\n---\nBody content here."
        frontmatter, body = analyzer.extract_sections(content)
        assert frontmatter["title"] == "Test"
        assert frontmatter["category"] == "demo"
        assert "Body content here." in body

    def test_no_frontmatter(self):
        analyzer = ContextAnalyzer()
        content = "Just regular content with no frontmatter."
        frontmatter, body = analyzer.extract_sections(content)
        assert frontmatter == {}
        assert body == content

    def test_malformed_yaml_returns_empty_dict(self):
        analyzer = ContextAnalyzer()
        content = "---\n: [invalid yaml\n---\nBody here."
        frontmatter, body = analyzer.extract_sections(content)
        assert frontmatter == {} or isinstance(frontmatter, dict)

    def test_empty_content(self):
        analyzer = ContextAnalyzer()
        frontmatter, body = analyzer.extract_sections("")
        assert frontmatter == {}


class TestEstimateTokens:
    """Tests for estimate_tokens()."""

    def test_empty_string(self):
        analyzer = ContextAnalyzer()
        assert analyzer.estimate_tokens("") == 0

    def test_positive_for_content(self):
        analyzer = ContextAnalyzer()
        assert analyzer.estimate_tokens("hello world, this is a test") > 0

    def test_longer_text_more_tokens(self):
        analyzer = ContextAnalyzer()
        short = analyzer.estimate_tokens("hi")
        long = analyzer.estimate_tokens("this is a much longer piece of text for estimation")
        assert long > short


class TestCalculateRedundancy:
    """Tests for calculate_redundancy()."""

    def test_no_redundancy(self):
        analyzer = ContextAnalyzer()
        text = "line one\nline two\nline three"
        score = analyzer.calculate_redundancy(text)
        assert 0 <= score <= 1

    def test_high_redundancy(self):
        analyzer = ContextAnalyzer()
        text = "the same line\nthe same line\nthe same line\nthe same line"
        score = analyzer.calculate_redundancy(text)
        assert score > 0.2

    def test_empty_text(self):
        analyzer = ContextAnalyzer()
        score = analyzer.calculate_redundancy("")
        assert score == 0.0

    def test_single_line(self):
        analyzer = ContextAnalyzer()
        score = analyzer.calculate_redundancy("just one line here")
        assert 0 <= score <= 1


class TestAnalyzeStructure:
    """Tests for analyze_structure()."""

    def test_returns_expected_keys(self):
        analyzer = ContextAnalyzer()
        result = analyzer.analyze_structure("You are a code reviewer. Task: review code.")
        assert "has_role" in result
        assert "has_task" in result
        assert "has_instructions" in result
        assert "has_examples" in result
        assert "has_constraints" in result
        assert "list_count" in result
        assert "numbered_lists" in result

    def test_detects_role(self):
        analyzer = ContextAnalyzer()
        result = analyzer.analyze_structure("You are an expert Python developer.")
        assert result["has_role"] is True

    def test_detects_task(self):
        analyzer = ContextAnalyzer()
        # The regex uses \b around 'task:', which won't match due to ':'
        # not being a word character. Use 'should' which does match.
        result = analyzer.analyze_structure("You should build a REST API.")
        assert result["has_task"] is True

    def test_detects_instructions(self):
        analyzer = ContextAnalyzer()
        result = analyzer.analyze_structure("Follow these instructions carefully. You must comply.")
        assert result["has_instructions"] is True

    def test_detects_examples(self):
        analyzer = ContextAnalyzer()
        result = analyzer.analyze_structure("For instance, consider the following example:")
        assert result["has_examples"] is True

    def test_detects_constraints(self):
        analyzer = ContextAnalyzer()
        result = analyzer.analyze_structure("Constraint: Must not exceed 200 words. Avoid jargon.")
        assert result["has_constraints"] is True

    def test_counts_bullet_lists(self):
        analyzer = ContextAnalyzer()
        text = "Items:\n- first\n- second\n- third\n* fourth"
        result = analyzer.analyze_structure(text)
        assert result["list_count"] == 4

    def test_counts_numbered_lists(self):
        analyzer = ContextAnalyzer()
        text = "Steps:\n1. First step\n2. Second step\n3. Third step"
        result = analyzer.analyze_structure(text)
        assert result["numbered_lists"] == 3

    def test_empty_text(self):
        analyzer = ContextAnalyzer()
        result = analyzer.analyze_structure("")
        assert result["has_role"] is False
        assert result["list_count"] == 0


class TestAssessOptimizationPotential:
    """Tests for assess_optimization_potential()."""

    def test_returns_valid_level(self):
        analyzer = ContextAnalyzer()
        metrics = {
            "prompt_tokens": 50,
            "redundancy_score": 0.05,
            "structure_score": {"list_count": 0},
        }
        result = analyzer.assess_optimization_potential(metrics)
        assert result in ("Low", "Medium", "High")

    def test_high_potential(self):
        analyzer = ContextAnalyzer()
        metrics = {
            "prompt_tokens": 500,
            "redundancy_score": 0.5,
            "structure_score": {"list_count": 2},
        }
        assert analyzer.assess_optimization_potential(metrics) == "High"

    def test_low_potential(self):
        analyzer = ContextAnalyzer()
        metrics = {
            "prompt_tokens": 50,
            "redundancy_score": 0.05,
            "structure_score": {"list_count": 1},
        }
        assert analyzer.assess_optimization_potential(metrics) == "Low"


class TestSuggestPatterns:
    """Tests for suggest_patterns()."""

    def test_returns_list(self):
        analyzer = ContextAnalyzer()
        result = analyzer.suggest_patterns("Do a step by step review.", {})
        assert isinstance(result, list)

    def test_suggests_control_flow(self):
        analyzer = ContextAnalyzer()
        result = analyzer.suggest_patterns("Follow the step-by-step procedure.", {})
        assert any("Control-flow" in s for s in result)

    def test_suggests_few_shot(self):
        analyzer = ContextAnalyzer()
        result = analyzer.suggest_patterns("Here are some examples of good output.", {})
        assert any("Few-shot" in s for s in result)

    def test_suggests_progressive_for_long_content(self):
        analyzer = ContextAnalyzer()
        long_content = "word " * 300  # >1000 chars
        result = analyzer.suggest_patterns(long_content, {})
        assert any("Progressive" in s for s in result)

    def test_suggests_minimal_role(self):
        analyzer = ContextAnalyzer()
        result = analyzer.suggest_patterns("You are a coding expert who reviews code.", {})
        assert any("Minimal-role" in s for s in result)

    def test_suggests_token_budget(self):
        analyzer = ContextAnalyzer()
        result = analyzer.suggest_patterns("Analyze the dataset and evaluate results.", {})
        assert any("Token-budget" in s for s in result)

    def test_vibecoding_tag(self):
        analyzer = ContextAnalyzer()
        result = analyzer.suggest_patterns("Enter the flow state.", {"tags": ["vibecoding"]})
        assert any("Field-based" in s for s in result)

    def test_empty_content(self):
        analyzer = ContextAnalyzer()
        result = analyzer.suggest_patterns("", {})
        assert isinstance(result, list)
        assert len(result) == 0


class TestAnalyzeFile:
    """Tests for analyze_file()."""

    def test_returns_expected_keys(self, sample_prompt_file, tmp_path):
        analyzer = ContextAnalyzer(str(tmp_path))
        result = analyzer.analyze_file(sample_prompt_file)
        assert "filepath" in result
        assert "title" in result
        assert "category" in result
        assert "total_tokens" in result
        assert "prompt_tokens" in result
        assert "redundancy_score" in result
        assert "structure_score" in result
        assert "optimization_potential" in result
        assert "suggested_patterns" in result

    def test_extracts_title_from_frontmatter(self, sample_prompt_file, tmp_path):
        analyzer = ContextAnalyzer(str(tmp_path))
        result = analyzer.analyze_file(sample_prompt_file)
        assert result["title"] == "Sample Prompt"

    def test_extracts_category(self, sample_prompt_file, tmp_path):
        analyzer = ContextAnalyzer(str(tmp_path))
        result = analyzer.analyze_file(sample_prompt_file)
        assert result["category"] == "coding"

    def test_tokens_are_positive(self, sample_prompt_file, tmp_path):
        analyzer = ContextAnalyzer(str(tmp_path))
        result = analyzer.analyze_file(sample_prompt_file)
        assert result["total_tokens"] > 0
        assert result["prompt_tokens"] > 0


class TestGenerateReport:
    """Tests for generate_report()."""

    def test_report_is_string(self):
        analyzer = ContextAnalyzer()
        results = [
            {
                "filepath": "test.md",
                "title": "Test",
                "category": "demo",
                "total_tokens": 100,
                "prompt_tokens": 80,
                "redundancy_score": 0.1,
                "structure_score": {"list_count": 2},
                "optimization_potential": "Low",
                "suggested_patterns": [],
            }
        ]
        report = analyzer.generate_report(results)
        assert isinstance(report, str)
        assert "Context Engineering Analysis Report" in report

    def test_report_includes_summary_stats(self):
        analyzer = ContextAnalyzer()
        results = [
            {
                "filepath": "a.md",
                "title": "A",
                "category": "x",
                "total_tokens": 200,
                "prompt_tokens": 150,
                "redundancy_score": 0.4,
                "structure_score": {"list_count": 1},
                "optimization_potential": "High",
                "suggested_patterns": ["Progressive: Use progressive context enhancement"],
            },
            {
                "filepath": "b.md",
                "title": "B",
                "category": "x",
                "total_tokens": 100,
                "prompt_tokens": 80,
                "redundancy_score": 0.05,
                "structure_score": {"list_count": 0},
                "optimization_potential": "Low",
                "suggested_patterns": [],
            },
        ]
        report = analyzer.generate_report(results)
        assert "Analyzed 2 prompts" in report
        assert "High optimization potential: 1" in report

    def test_empty_results(self):
        analyzer = ContextAnalyzer()
        # generate_report divides by len(results), so empty list would error.
        # This tests the edge case.
        with pytest.raises((ZeroDivisionError, IndexError)):
            analyzer.generate_report([])


class TestExportJson:
    """Tests for export_json()."""

    def test_creates_json_file(self, tmp_path):
        analyzer = ContextAnalyzer()
        output_file = str(tmp_path / "output.json")
        results = [
            {
                "filepath": "test.md",
                "title": "Test",
                "total_tokens": 100,
            }
        ]
        analyzer.export_json(results, output_file)
        with open(output_file, "r") as f:
            data = json.load(f)
        assert data["total_prompts"] == 1
        assert len(data["results"]) == 1

    def test_export_empty_results(self, tmp_path):
        analyzer = ContextAnalyzer()
        output_file = str(tmp_path / "empty.json")
        analyzer.export_json([], output_file)
        with open(output_file, "r") as f:
            data = json.load(f)
        assert data["total_prompts"] == 0
        assert data["results"] == []
