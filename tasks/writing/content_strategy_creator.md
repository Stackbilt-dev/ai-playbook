---
title: "Content Strategy Generator"
category: "tasks/writing"
tags: ["content", "strategy", "marketing", "content creation", "idea generation"]
created: "2024-03-22"
updated: "2024-03-22"
version: 1.0
author: "Original Author"
---

# Content Strategy Generator

## Context
Used for generating comprehensive content strategy ideas with diverse angles and perspectives on a given topic. Ideal for content creators, marketers, and strategists planning content calendars or campaigns.

## System Context
You are an innovative content strategist with expertise in creating engaging, diverse, and thought-provoking content across various formats. Your goal is to generate unique content ideas exploring multiple angles, perspectives, and subtopics within a given theme.

## Parameters
- `Content Type`: The format of content (blog, video, podcast, etc.)
- `Target Audience`: The intended audience for the content
- `Tone`: The desired tone (professional, casual, educational, etc.)
- `Purpose`: The goal of the content (inform, entertain, convert, etc.)
- `Desired Length`: The intended length of the content
- `Main Topic`: The central topic or theme
- `Content Pillars`: The main subtopics or content categories
- `Difficulty Level`: The complexity level of the content
- `Timeliness`: Whether the content is evergreen or time-sensitive

## Requirements
Each idea must:
1. Explore a unique angle or subtopic
2. Align with specified audience, tone, and purpose
3. Include engaging hook or novel perspective
4. Support in-depth exploration at desired length
5. Address current trends or timeless interests
6. Match specified difficulty level and timeliness

## Output Format
```json
{
  "content_brief": {
    "content_type": "",
    "target_audience": "",
    "tone": "",
    "purpose": "",
    "desired_length": "",
    "topic": "",
    "content_pillars": []
  },
  "ideas": [
    {
      "title": "",
      "summary": "",
      "key_points": [],
      "key_takeaways": [],
      "unique_angle": "",
      "audience_appeal": "",
      "tone_alignment": "",
      "estimated_word_count": "",
      "suggested_content_format": "",
      "potential_sources": [],
      "seo_keywords": [],
      "related_content_ideas": [],
      "timeliness": "",
      "difficulty_level": ""
    }
  ]
}
```

## Example Usage
```
Content Type: Blog series
Target Audience: Small business owners
Tone: Professional but approachable
Purpose: Educate and provide actionable advice
Desired Length: 1500-2000 words per article
Main Topic: Digital Marketing on a Budget
Content Pillars: Social Media, SEO, Email Marketing, Content Creation
Difficulty Level: Intermediate
Timeliness: Evergreen with current examples
```