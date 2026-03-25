---
title: "Image Idea Generator"
category: "tasks/writing"
tags: ["creativity", "image", "idea generation", "visual"]
created: "2024-03-22"
updated: "2024-03-22"
version: 1.0
author: "Original Author"
---

# Image Idea Generator

## Context
Used for generating concise image composition ideas based on user input and specified image type.

## Prompt Content
Create a short idea for the selected image type: [IMAGE_TYPE], that would pair well with the user's raw multiline input: [USER_INPUT].

## Template Structure
The idea template (should be a simple composition):
A [IMAGE_TYPE] of [SUBJECT] [in relation to] [BACKGROUND]

## Guidelines
1. Keep composition simple and clear
2. Focus on single subject-background relationship
3. Ensure visual hierarchy
4. Consider platform-specific requirements

## Parameters
- `IMAGE_TYPE`: Type of image to be created (e.g., photograph, illustration, 3D render)
- `USER_INPUT`: Raw multiline input from the user that will inform the image concept

## Output Format
The [IMAGE_TYPE] idea: [GENERATED_IDEA]

## Example Usage
```
Create a short idea for the selected image type: photograph, that would pair well with the user's raw multiline input: 
"The calm after the storm
When everything settles
And a new beginning emerges"
```

## Expected Output
```
The photograph idea: A solitary tree sprouting new leaves against a clearing sky with puddles reflecting sunlight
```