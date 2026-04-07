"""Tests for PromptSearcher class (tools/search-prompts.py)."""

import sys
import json
import pytest
from pathlib import Path

# The module has a hyphen in its filename, so we import it dynamically.
TOOLS_DIR = Path(__file__).resolve().parent.parent / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import importlib
_search_mod = importlib.import_module("search-prompts")
PromptSearcher = _search_mod.PromptSearcher
format_prompt_result = _search_mod.format_prompt_result


class TestInit:
    """Test PromptSearcher initialization."""

    def test_loads_index(self, sample_index):
        searcher = PromptSearcher(sample_index)
        assert len(searcher.prompts) == 3

    def test_loads_metadata(self, sample_index):
        searcher = PromptSearcher(sample_index)
        assert "categories" in searcher.index["metadata"]

    def test_invalid_path_raises(self):
        with pytest.raises(FileNotFoundError):
            PromptSearcher("/nonexistent/path.json")


class TestSearchByTags:
    """Tests for search_by_tags()."""

    def test_finds_matching_tag(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_tags(["python"])
        assert len(results) == 2

    def test_case_insensitive(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_tags(["PYTHON"])
        assert len(results) == 2

    def test_no_match_returns_empty(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_tags(["nonexistent_tag"])
        assert results == []

    def test_multiple_tags_union(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_tags(["python", "creative"])
        assert len(results) == 3  # 2 python + 1 creative

    def test_empty_tags_list(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_tags([])
        assert results == []


class TestSearchByCategory:
    """Tests for search_by_category()."""

    def test_finds_category(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_category("coding")
        assert len(results) == 2

    def test_case_insensitive(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_category("CODING")
        assert len(results) == 2

    def test_no_match(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_category("nonexistent")
        assert results == []

    def test_partial_match(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_category("cod")
        assert len(results) == 2  # "cod" in "coding"


class TestSearchByKeyword:
    """Tests for search_by_keyword()."""

    def test_matches_title(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_keyword("Python")
        assert len(results) >= 2

    def test_matches_description(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_keyword("FastAPI")
        assert len(results) >= 1

    def test_matches_tags(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_keyword("api")
        assert len(results) >= 1

    def test_matches_archetype_field(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_keyword("Architect")
        assert len(results) >= 1

    def test_title_match_scores_highest(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_keyword("Python")
        # Title matches should be first (score 1.0)
        assert results[0]["_match_score"] == 1.0

    def test_no_match(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_keyword("zzz_nonexistent_zzz")
        assert results == []

    def test_empty_keyword(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_keyword("")
        # Empty string is in every string, so should match all
        assert len(results) >= 3


class TestSearchByArchetype:
    """Tests for search_by_archetype()."""

    def test_finds_archetype(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_archetype("The Architect")
        assert len(results) == 1
        assert results[0]["title"] == "Python API Builder"

    def test_case_insensitive(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_archetype("the architect")
        assert len(results) == 1

    def test_no_match(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.search_by_archetype("The Wizard")
        assert results == []


class TestFindSimilar:
    """Tests for find_similar()."""

    def test_returns_results(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.find_similar("Python API Developer")
        assert len(results) > 0

    def test_respects_limit(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.find_similar("Python", limit=1)
        assert len(results) <= 1

    def test_results_have_similarity_score(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.find_similar("Python API")
        for r in results:
            assert "_similarity" in r
            assert 0 <= r["_similarity"] <= 1

    def test_sorted_by_similarity(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.find_similar("Python Test")
        if len(results) > 1:
            for i in range(len(results) - 1):
                assert results[i]["_similarity"] >= results[i + 1]["_similarity"]

    def test_empty_title(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.find_similar("")
        assert isinstance(results, list)


class TestRecommendForTask:
    """Tests for recommend_for_task()."""

    def test_returns_list(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.recommend_for_task("review Python code")
        assert isinstance(results, list)

    def test_deduplicates_results(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.recommend_for_task("python testing review")
        paths = [r["path"] for r in results]
        assert len(paths) == len(set(paths))

    def test_limits_to_ten(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.recommend_for_task("python coding testing api writing creative review")
        assert len(results) <= 10

    def test_empty_description(self, sample_index):
        searcher = PromptSearcher(sample_index)
        results = searcher.recommend_for_task("")
        assert isinstance(results, list)


class TestFormatPromptResult:
    """Tests for the format_prompt_result() helper."""

    def test_includes_title(self):
        prompt = {
            "title": "Test Prompt",
            "path": "coding/test.md",
            "category": "coding",
            "tags": ["python"],
            "description": "A test prompt.",
        }
        output = format_prompt_result(prompt)
        assert "Test Prompt" in output
        assert "coding/test.md" in output

    def test_verbose_includes_description(self):
        prompt = {
            "title": "Test Prompt",
            "path": "coding/test.md",
            "category": "coding",
            "tags": ["python"],
            "description": "A detailed description here.",
        }
        output = format_prompt_result(prompt, verbose=True)
        assert "A detailed description here." in output

    def test_non_verbose_omits_description(self):
        prompt = {
            "title": "Test Prompt",
            "path": "coding/test.md",
            "category": "coding",
            "tags": ["python"],
            "description": "A detailed description here.",
        }
        output = format_prompt_result(prompt, verbose=False)
        assert "A detailed description here." not in output

    def test_shows_archetype_if_present(self):
        prompt = {
            "title": "Vibe Prompt",
            "path": "vibes/flow.md",
            "category": "vibecoding",
            "tags": [],
            "description": "",
            "archetype": "The Flow State",
        }
        output = format_prompt_result(prompt)
        assert "The Flow State" in output
