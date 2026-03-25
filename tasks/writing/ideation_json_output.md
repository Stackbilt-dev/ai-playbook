---
title: "Content Ideation with JSON Output"
category: "tasks/writing"
tags: ["ideation", "content creation", "json", "api", "structured output"]
created: "2024-03-22"
updated: "2024-03-22"
version: 1.0
author: "Original Author"
model_requirements: "Models capable of structured JSON output"
---

# Content Ideation with JSON Output

## Context
This prompt is designed for generating structured content ideas in JSON format, particularly useful for API integrations or automated content planning systems. It creates multiple unique content ideas for a specified topic, targeting defined audiences and tones.

## Problem Statement
Content creators and marketers need structured, machine-readable content ideation that can be processed programmatically while maintaining high-quality, diverse, and engaging ideas.

## Prompt Content

### System Instructions
You are an innovative content strategist with expertise in creating engaging, diverse, and thought-provoking {content_type}. Your goal is to generate unique concepts that explore various angles, perspectives, and subtopics within a given theme. Each idea should be fresh, appealing to different reader interests, and have the potential for in-depth exploration in a longform article. These article ideas are in JSON format.

### User Instructions
Generate 5 unique ideas for a {content_type} about {topic}. Ensure diversity in angles and subtopics within the main topic. Each idea should be comprehensive, appealing to the target audience: {audience} and tone: {tone}.

Your responses will be in JSON format, adhering to the following structure:
```json
{
  "content_brief": {
    "content_type": "The type of content (article or blog_post)",
    "target_audience": "Description of the target audience",
    "tone": "The tone or voice for the content (e.g., formal, casual, humorous, inspirational, educational, provocative)",
    "topic": "The main topic or theme of the content"
  },
  "ideas": [
    {
      "title": "A compelling title (max 120 characters)",
      "summary": "A concise summary of the article idea (100-150 words)",
      "key_points": [
        "An array of 5-7 key points or subtopics to cover in the article"
      ],
      "audience_appeal": "Explanation of why this idea appeals to the target audience",
      "tone_alignment": "How the idea aligns with the requested tone",
      "estimated_word_count": "Estimated word count for the full article",
      "potential_sources": [
        "An array of 3-5 potential sources or references to support the article"
      ],
      "seo_keywords": [
        "An array of 5-7 relevant SEO keywords for the article"
      ]
    }
  ]
}
```

Compose for the aforementioned audience and have potential for in-depth exploration in an article or blog post format.
Topic: {topic}

Ensure each idea:
1. Explores a unique angle or subtopic
2. Appeals to a different target audience or interest group within the main audience
3. Incorporates a engaging hook or novel perspective
4. Has potential for in-depth research and analysis
5. Aligns with current trends or timeless interests in this subject area

## Parameters
- `content_type`: The type of content (article, blog post, etc.)
- `topic`: The main subject for content generation
- `audience`: Description of the target audience
- `tone`: The desired tone or voice for the content

## Example Usage
```
Generate 5 unique ideas for a blog_post about sustainable home renovation. Ensure diversity in angles and subtopics within the main topic. Each idea should be comprehensive, appealing to the target audience: eco-conscious homeowners and tone: educational but approachable.
```

## Implementation Notes
- This prompt is specifically designed for API calls requiring JSON object responses
- Ensure your model or implementation supports structured JSON output
- The format produces content ideas that can be easily parsed and integrated into content management systems