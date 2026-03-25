---
title: "Content Development Chain"
category: "chains"
tags: ["content creation", "workflow", "prompt chain", "ideation", "writing", "editing"]
created: "2024-03-22"
updated: "2024-03-22"
version: 1.0
author: "Chain Developer"
dependencies: ["ideation_json_output", "outline_creator", "article_draft_system"]
---

# Content Development Chain

## Context
This prompt chain creates a complete end-to-end workflow for developing high-quality content. It connects multiple specialized prompts in sequence, where the output of each stage becomes the input for the next. This chain is ideal for content creators, marketers, and publishers who want to streamline their content creation process while maintaining quality.

## Chain Overview

```
Ideation → Outline → Draft → Revision
```

This chain connects four specialized prompts:
1. **Ideation**: Generate unique content ideas
2. **Outline**: Create a structured outline based on the selected idea
3. **Draft**: Develop a full draft based on the outline
4. **Revision**: Polish and improve the draft

## Stage 1: Ideation

### Prompt
```
You are an innovative content strategist with expertise in creating engaging, diverse, and thought-provoking {content_type}.

Generate 5 unique ideas for a {content_type} about {topic}. Ensure diversity in angles and subtopics within the main topic. Each idea should be comprehensive, appealing to the target audience: {audience} and tone: {tone}.

For each idea, provide:
1. A compelling title
2. A concise summary (100-150 words)
3. 5-7 key points to cover
4. Why this appeals to the target audience
5. How it aligns with the requested tone
```

### Parameters
- `content_type`: The type of content (article, blog post, etc.)
- `topic`: The main subject for content generation
- `audience`: Description of the target audience
- `tone`: The desired tone or voice for the content

### Output
A list of 5 potential content ideas with titles, summaries, and key points.

## Stage 2: Outline

### Prompt
```
You are an expert article outliner, specializing in creating functional and flexible outlines.

Create a detailed outline for the following content idea:

Title: {selected_title}
Summary: {selected_summary}
Key Points: {selected_key_points}
Target Audience: {audience}
Tone: {tone}
Desired Length: {wordcount} words

The outline should include:
1. A compelling introduction with hook and thesis
2. 3-5 main sections with clear, descriptive headings
3. 2-4 subsections under each main section
4. A conclusion with key takeaways and call to action

For each section and subsection, provide a brief description of its content and purpose.
```

### Parameters
- `selected_title`: The title of the selected idea from Stage 1
- `selected_summary`: The summary of the selected idea
- `selected_key_points`: The key points from the selected idea
- `audience`: The target audience (carried over from Stage 1)
- `tone`: The desired tone (carried over from Stage 1)
- `wordcount`: The desired length of the final content

### Output
A comprehensive, hierarchical outline for the selected content idea.

## Stage 3: Draft

### Prompt
```
You are an expert content writer tasked with creating a comprehensive draft based on a provided outline.

Produce a well-structured, engaging, and informative {content_type} that follows this outline:

{outline}

Write in a {tone} tone appropriate for {audience}. The content should be approximately {wordcount} words.

Use clear headings and subheadings to structure the content. Maintain a cohesive flow and consistent tone throughout, ensuring smooth transitions between sections. Prioritize factual accuracy and provide nuanced, well-researched content that adds value to the reader's understanding of the topic.
```

### Parameters
- `content_type`: The type of content (carried over from Stage 1)
- `outline`: The complete outline from Stage 2
- `tone`: The desired tone (carried over)
- `audience`: The target audience (carried over)
- `wordcount`: The desired length (carried over)

### Output
A complete first draft of the content that follows the outline.

## Stage 4: Revision

### Prompt
```
You are an expert content editor specializing in polishing and improving drafts while maintaining the author's voice and intent.

Review and revise the following draft to enhance its clarity, engagement, and impact:

{draft}

Focus on:
1. Strengthening the introduction and conclusion
2. Improving paragraph transitions and flow
3. Enhancing clarity and readability
4. Ensuring consistent tone and voice
5. Optimizing for engagement with the target audience: {audience}
6. Checking for comprehensiveness in covering the key points
7. Tightening language and eliminating redundancy

Maintain the overall structure but improve the content itself. The final piece should remain approximately {wordcount} words and maintain a {tone} tone.
```

### Parameters
- `draft`: The complete draft from Stage 3
- `audience`: The target audience (carried over)
- `tone`: The desired tone (carried over)
- `wordcount`: The desired length (carried over)

### Output
A polished, publication-ready version of the content.

## Chain Usage Instructions

### Setup
1. Create a new project folder for your content
2. Decide on your content topic, type, audience, and tone
3. Prepare to track outputs from each stage as inputs to the next

### Execution Process
1. Run Stage 1 (Ideation) with your initial parameters
2. Select your preferred idea from the output
3. Run Stage 2 (Outline) using that idea plus additional parameters
4. Review and adjust the outline if needed
5. Run Stage 3 (Draft) using the approved outline
6. Review the draft for major issues
7. Run Stage 4 (Revision) using the draft
8. Make any final adjustments to the revised content

### Tips for Effective Chain Use
- You can pause between any stages for human review/input
- Each stage can be rerun with adjustments if the output isn't satisfactory
- Save the output from each stage for reference
- For best results, be as specific as possible with your initial parameters
- The chain can be modified to include additional specialized stages (e.g., SEO optimization, fact-checking)

## Example Workflow

**Initial Parameters:**
- Content Type: Blog post
- Topic: Sustainable home renovation
- Audience: Eco-conscious homeowners
- Tone: Educational but approachable
- Word Count: 1500 words

**Stage 1:** Generate 5 sustainable home renovation content ideas
**Stage 2:** Create outline for the selected idea "10 Energy-Efficient Upgrades That Pay For Themselves"
**Stage 3:** Draft the full article following the outline
**Stage 4:** Revise the draft for publication

## Variations
- **SEO-Focused Chain**: Add a keyword research stage at the beginning and an SEO optimization stage at the end
- **Visual Content Chain**: Add a stage for generating image concepts/descriptions to accompany the content
- **Social Media Chain**: Add a final stage that creates social promotion snippets from the finished content