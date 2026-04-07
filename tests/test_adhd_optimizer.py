"""Tests for ADHDPromptOptimizer class.

NOTE: Recursion bug fixed (2026-04-07) —
analyze_prompt() calls _assess_complexity() which calls analyze_prompt()
again. Fixed by extracting components directly in _assess_complexity().
"""

import pytest
from tests.conftest import ADHDPromptOptimizer


class TestInit:
    """Verify optimizer initializes with expected state."""

    def test_emoji_map_populated(self, optimizer):
        assert isinstance(optimizer.emoji_map, dict)
        assert len(optimizer.emoji_map) > 0

    def test_patterns_populated(self, optimizer):
        assert "task_indicators" in optimizer.patterns
        assert "context_indicators" in optimizer.patterns
        assert "requirement_indicators" in optimizer.patterns
        assert "constraint_indicators" in optimizer.patterns

    def test_filler_words_populated(self, optimizer):
        assert isinstance(optimizer.filler_words, list)
        assert len(optimizer.filler_words) > 0


class TestAnalyzePrompt:
    """Tests for analyze_prompt().

    analyze_prompt() triggers infinite recursion because _assess_complexity()
    calls analyze_prompt() internally. These tests document the bug.
    """

    def test_returns_expected_keys(self, optimizer):
        result = optimizer.analyze_prompt("I need to build a REST API.")
        assert "original" in result

    def test_components_have_expected_keys(self, optimizer):
        result = optimizer.analyze_prompt("Help me fix a bug in my code.")
        components = result["components"]
        assert "task" in components

    def test_word_count_accurate(self, optimizer):
        prompt = "one two three four five"
        result = optimizer.analyze_prompt(prompt)
        assert result["word_count"] == 5

    def test_char_count_accurate(self, optimizer):
        prompt = "hello"
        result = optimizer.analyze_prompt(prompt)
        assert result["char_count"] == 5

    def test_empty_prompt(self, optimizer):
        result = optimizer.analyze_prompt("")
        assert result["char_count"] == 0

    def test_single_word_prompt(self, optimizer):
        result = optimizer.analyze_prompt("deploy")
        assert result["word_count"] == 1


class TestExtractTask:
    """Tests for _extract_task()."""

    def test_extracts_from_i_need(self, optimizer):
        task = optimizer._extract_task("I need to build a REST API for my project.")
        assert task is not None
        assert len(task) > 0

    def test_extracts_from_help_me(self, optimizer):
        task = optimizer._extract_task("Help me understand recursion.")
        assert task is not None

    def test_extracts_from_create(self, optimizer):
        task = optimizer._extract_task("Create a dashboard component.")
        assert task is not None

    def test_fallback_to_first_sentence(self, optimizer):
        task = optimizer._extract_task("This is a plain statement without indicators.")
        assert task == "This is a plain statement without indicators"

    def test_empty_input(self, optimizer):
        task = optimizer._extract_task("")
        assert task is not None  # falls back to first split element


class TestExtractContext:
    """Tests for _extract_context()."""

    def test_extracts_context_phrases(self, optimizer):
        prompt = "I'm using React and working with GraphQL for this project."
        context = optimizer._extract_context(prompt)
        assert isinstance(context, list)
        assert len(context) > 0

    def test_no_context_returns_empty(self, optimizer):
        context = optimizer._extract_context("Deploy the app.")
        assert isinstance(context, list)

    def test_limits_to_five(self, optimizer):
        # Craft a prompt with many context indicators
        prompt = (
            "I have a server. I'm using Python. Working with Docker. "
            "Based on microservices. Currently in staging. "
            "Background in DevOps. Experience with Kubernetes. Familiar with Terraform."
        )
        context = optimizer._extract_context(prompt)
        assert len(context) <= 5


class TestExtractRequirements:
    """Tests for _extract_requirements()."""

    def test_extracts_requirements(self, optimizer):
        prompt = "The app should handle 1000 users and must be responsive."
        reqs = optimizer._extract_requirements(prompt)
        assert isinstance(reqs, list)
        assert len(reqs) > 0

    def test_no_requirements(self, optimizer):
        reqs = optimizer._extract_requirements("Hello world.")
        assert isinstance(reqs, list)
        assert len(reqs) == 0


class TestExtractConstraints:
    """Tests for _extract_constraints()."""

    def test_extracts_constraints(self, optimizer):
        prompt = "Budget is limited to 500 dollars. Don't use external libraries."
        constraints = optimizer._extract_constraints(prompt)
        assert isinstance(constraints, list)
        assert len(constraints) > 0

    def test_no_constraints(self, optimizer):
        constraints = optimizer._extract_constraints("Build an app.")
        assert isinstance(constraints, list)


class TestIdentifyImplicitNeeds:
    """Tests for _identify_implicit_needs()."""

    def test_api_without_docs(self, optimizer):
        needs = optimizer._identify_implicit_needs("Build an API endpoint.")
        assert "API documentation" in needs

    def test_api_with_docs(self, optimizer):
        needs = optimizer._identify_implicit_needs("Build an API endpoint with documentation.")
        assert "API documentation" not in needs

    def test_build_without_test(self, optimizer):
        needs = optimizer._identify_implicit_needs("Build a user registration system.")
        assert "Testing approach" in needs

    def test_build_with_test(self, optimizer):
        needs = optimizer._identify_implicit_needs("Build and test a login form.")
        assert "Testing approach" not in needs

    def test_security_without_auth(self, optimizer):
        needs = optimizer._identify_implicit_needs("Make it secure against attacks.")
        assert "Authentication method" in needs

    def test_no_implicit_needs(self, optimizer):
        needs = optimizer._identify_implicit_needs("Explain how loops work.")
        assert isinstance(needs, list)
        assert len(needs) == 0


class TestDetectStyle:
    """Tests for _detect_style()."""

    def test_debug_style(self, optimizer):
        assert optimizer._detect_style("Fix the bug in my login page.") == "debug"

    def test_learning_style(self, optimizer):
        assert optimizer._detect_style("Explain how closures work in JavaScript.") == "learning"

    def test_creative_style(self, optimizer):
        assert optimizer._detect_style("Write a blog article about AI trends.") == "creative"

    def test_technical_style(self, optimizer):
        assert optimizer._detect_style("Implement an API endpoint for user search.") == "technical"

    def test_general_fallback(self, optimizer):
        assert optimizer._detect_style("Do the thing.") == "general"


class TestOptimize:
    """Tests for optimize().

    optimize() calls analyze_prompt() which hits the recursion bug.
    These are marked xfail to document the issue.
    """

    def test_returns_expected_keys(self, optimizer):
        result = optimizer.optimize("Help me build a web app.")
        assert "original" in result

    def test_metrics_shape(self, optimizer):
        result = optimizer.optimize("Create a Python function.")
        metrics = result["metrics"]
        assert "original_tokens" in metrics

    def test_token_reduction_is_percentage_string(self, optimizer):
        result = optimizer.optimize("I really need help basically creating a function.")
        assert "%" in result["metrics"]["token_reduction"]

    def test_explicit_style_override(self, optimizer):
        result = optimizer.optimize("Help me build something.", style="debug")
        assert result["style"] == "debug"

    def test_auto_style_detection(self, optimizer):
        result = optimizer.optimize("Fix the error in my code.")
        assert result["style"] == "debug"

    def test_optimized_is_nonempty_string(self, optimizer):
        result = optimizer.optimize("I want to learn about databases.")
        assert isinstance(result["optimized"], str)

    def test_optimized_has_structure(self, optimizer):
        result = optimizer.optimize("I need to build a REST API using Python and FastAPI.")
        optimized = result["optimized"]
        assert "\n" in optimized

    def test_all_styles_produce_output(self, optimizer):
        prompt = "Help me review and fix the code for my project."
        for style in ["technical", "debug", "learning", "creative", "general"]:
            result = optimizer.optimize(prompt, style=style)
            assert len(result["optimized"]) > 0, f"Style '{style}' produced empty output"


class TestScoringMethods:
    """Tests for clarity and structure scoring."""

    def test_clarity_score_range(self, optimizer):
        score = optimizer._calculate_clarity_score("Some text here.")
        assert 0 <= score <= 100

    def test_clarity_penalizes_filler(self, optimizer):
        clean = optimizer._calculate_clarity_score("Build a REST API endpoint.")
        filler = optimizer._calculate_clarity_score(
            "I basically really think you should probably definitely build a REST API endpoint."
        )
        assert clean > filler

    def test_structure_score_range(self, optimizer):
        score = optimizer._calculate_structure_score("Some text here.")
        assert 0 <= score <= 100

    def test_structure_rewards_bullets(self, optimizer):
        flat = optimizer._calculate_structure_score("Build this. Do that. Ship it.")
        structured = optimizer._calculate_structure_score(
            "TASK: Build this\n- Step one\n- Step two\n- Step three\nOUTPUT: Done"
        )
        assert structured > flat


class TestEstimateTokens:
    """Tests for _estimate_tokens()."""

    def test_empty_string(self, optimizer):
        assert optimizer._estimate_tokens("") == 0

    def test_positive_for_nonempty(self, optimizer):
        assert optimizer._estimate_tokens("hello world") > 0

    def test_longer_text_more_tokens(self, optimizer):
        short = optimizer._estimate_tokens("hi")
        long = optimizer._estimate_tokens("this is a much longer piece of text for token estimation")
        assert long > short


class TestComplexityAssessment:
    """Tests for _assess_complexity().

    _assess_complexity() calls analyze_prompt() which calls _assess_complexity()
    again, causing infinite recursion. Marked xfail.
    """

    def test_low_complexity(self, optimizer):
        assert optimizer._assess_complexity("Fix the typo.") == "low"

    def test_high_complexity_long_prompt(self, optimizer):
        long_prompt = " ".join(["word"] * 120)
        assert optimizer._assess_complexity(long_prompt) == "high"

    def test_returns_valid_level(self, optimizer):
        level = optimizer._assess_complexity("Build an API with authentication.")
        assert level in ("low", "medium", "high")


class TestOptimizationPotential:
    """Tests for _calculate_optimization_potential()."""

    def test_returns_valid_level(self, optimizer):
        level = optimizer._calculate_optimization_potential("Build an app.")
        assert level in ("low", "medium", "high")

    def test_high_for_wordy_unstructured(self, optimizer):
        wordy = (
            "I basically really think that perhaps maybe you should definitely "
            "certainly create something that is quite good and very nice. "
            "I believe it seems like the right approach in my opinion."
        )
        level = optimizer._calculate_optimization_potential(wordy)
        assert level in ("medium", "high")
