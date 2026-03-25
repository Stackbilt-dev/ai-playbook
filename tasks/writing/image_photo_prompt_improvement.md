---
title: "Image and Photo Prompt Improvement"
category: "tasks/writing"
tags: ["image generation", "photography", "prompt engineering", "visual design", "AI art"]
created: "2024-03-22"
updated: "2024-03-22"
version: 1.0
author: "Original Author"
---

# Image and Photo Prompt Improvement

## Context
This prompt is designed to help users refine their simple image ideas into detailed, effective prompts for photographic image generation. It's particularly useful for creating prompts for AI image generators like DALL-E, Midjourney, or Stable Diffusion when aiming for photorealistic results.

## Prompt Content

### System Instructions
You are a social media graphic designer and LLM expert, whose job it is to improve user requests into exceptional prompts for photographic images.

### User Instructions
Create a prompt to be used for a photographic image generation for the below idea. Use precise, visual descriptions (rather than metaphorical concepts).

Try to keep the prompt short, yet precise.

Prompt Structure:
"A [image type] of [subject], [subject's characteristics], [relation to background] [background]. [Details of background] [Interactions with color and lighting]. Taken on [Details of camera, lens, style and settings]."

The photo composition should be simple.

The idea: {USER_INPUT}

## Parameters
- `USER_INPUT`: The user's original image idea or concept that needs refinement

## Guidelines
1. Focus on visual, concrete descriptions rather than abstract concepts
2. Keep compositions simple with clear subject-background relationships
3. Include specific details about lighting, color, and atmosphere
4. Add technical photographic details (camera type, lens, settings) for realism
5. Maintain brevity while ensuring all essential elements are included

## Example Usage
```
Create a prompt to be used for a photographic image generation for the below idea. Use precise, visual descriptions (rather than metaphorical concepts).

Try to keep the prompt short, yet precise.

The idea: An elderly man feeding pigeons in a park at sunset
```

## Expected Output
```
A portrait photograph of an elderly man with weathered skin and silver hair, sitting on a wooden bench feeding pigeons in a tranquil park. Golden sunset light casts long shadows across the scene, illuminating the man's profile with warm amber tones. The background features blurred autumn trees and a winding path. Taken on a Canon EOS R5 with an 85mm f/1.4 lens, shallow depth of field, soft bokeh effect.
```