---
title: "Storyboard with Inferred Audio Properties Incorporated"
category: "tasks/audio"
tags: ["storyboard", "audio properties", "lyrics", "music video"]
created: "2025-03-25"
updated: "2025-03-25"
version: 1.0
author: "Cline"
---

# Storyboard with Inferred Audio Properties Incorporated

## Context
This prompt is designed to guide the AI in creating a timestamped lyrical storyboard for a song, building upon the information from the inferred audio analysis and the song's lyrics.

## Problem Statement
Translating both the lyrics and the inferred audio properties into a visual storyboard outline.

## Prompt Content
Now, **building upon the audio property analysis you just performed**, please create a timestamped lyrical storyboard for this song.

Your goal is to translate both the **lyrics and the audio properties you identified** into a visual storyboard outline. For each section of the song (indicated by timestamps and lyrics), consider:

*   How can the **visuals of the storyboard scene reflect the inferred audio properties**? For example, if you identified the tempo as "fast and energetic," how can the visuals convey that pace and energy? If you noted "lush orchestral instrumentation," how can the scene's visual style match that sonic richness? Actively connect the visual ideas to the audio characteristics you previously described.
*   Incorporate all the elements of a music video storyboard we've discussed previously: scene setting, character focus, camera angles, visual style, action, transitions, and connection to the audio.

For each timestamp and lyric line, please:

*   **Include the timestamp in `[MM:SS]` format**.
*   **Present the lyric line itself**.
*   **Precede the lyric line with a descriptive annotation in parentheses `()`**. This annotation should now *explicitly* link the **visual storyboard ideas** to both the **lyrics** AND the **inferred audio properties**. Reference specific audio properties from your analysis where relevant (e.g., "Visuals match the *upbeat tempo* by showing fast cuts...", "Scene's *melancholy mood* reflected in muted color palette...").

## System Instructions
```
Now, **building upon the audio property analysis you just performed**, please create a timestamped lyrical storyboard for this song.

Your goal is to translate both the **lyrics and the audio properties you identified** into a visual storyboard outline.  For each section of the song (indicated by timestamps and lyrics), consider:

*   How can the **visuals of the storyboard scene reflect the inferred audio properties**?  For example, if you identified the tempo as "fast and energetic," how can the visuals convey that pace and energy? If you noted "lush orchestral instrumentation," how can the scene's visual style match that sonic richness?  Actively connect the visual ideas to the audio characteristics you previously described.
*   Incorporate all the elements of a music video storyboard we've discussed previously: scene setting, character focus, camera angles, visual style, action, transitions, and connection to the audio.

For each timestamp and lyric line, please:

*   **Include the timestamp in `[MM:SS]` format**.
*   **Present the lyric line itself**.
*   **Precede the lyric line with a descriptive annotation in parentheses `()`**.  This annotation should now *explicitly* link the **visual storyboard ideas** to both the **lyrics** AND the **inferred audio properties**.  Reference specific audio properties from your analysis where relevant (e.g., "Visuals match the *upbeat tempo* by showing fast cuts...", "Scene's *melancholy mood* reflected in muted color palette...").
```

## User Instructions
```
Now, **building upon the audio property analysis you just performed**, please create a timestamped lyrical storyboard for this song.

Your goal is to translate both the **lyrics and the audio properties you identified** into a visual storyboard outline. For each section of the song (indicated by timestamps and lyrics), consider:

*   How can the **visuals of the storyboard scene reflect the inferred audio properties**? For example, if you identified the tempo as "fast and energetic," how can the visuals convey that pace and energy? If you noted "lush orchestral instrumentation," how can the scene's visual style match that sonic richness? Actively connect the visual ideas to the audio characteristics you previously described.
*   Incorporate all the elements of a music video storyboard we've discussed previously: scene setting, character focus, camera angles, visual style, action, transitions, and connection to the audio.

For each timestamp and lyric line, please:

*   **Include the timestamp in `[MM:SS]` format**.
*   **Present the lyric line itself**.
*   **Precede the lyric line with a descriptive annotation in parentheses `()`**. This annotation should now *explicitly* link the **visual storyboard ideas** to both the **lyrics** AND the **inferred audio properties**. Reference specific audio properties from your analysis where relevant (e.g., "Visuals match the *upbeat tempo* by showing fast cuts...", "Scene's *melancholy mood* reflected in muted color palette...").

**Example of Desired Output (Markdown - Storyboard Linking Audio Properties):**

[00:00] (Intro - Soft piano melody, *inferred as 'gentle and reflective'*. **Visual Idea:** Open on a misty landscape, *matching the 'calm' audio mood*, slow camera pan.)
Instrumental

[00:05] (Verse 1 - Male vocals, gentle rhythm, *tempo inferred as 'moderate'*. **Visual Idea:** Singer close-up, *keeping pace with the 'moderate tempo'*, simple background, *reflecting the 'intimate' sonic character*.)
(Verse 1) Line of lyrics here

[00:20] (Chorus - Full band explodes, energetic mood, *tempo 'fast and upbeat', dynamics 'high energy'*. **Visual Idea:** Cut to full band performance, *visual energy matches the 'high energy' dynamics*, fast cuts *synchronized to the 'fast tempo'*, vibrant colors to enhance the *'upbeat mood'*.)
(Chorus) Chorus lyric line, loud and clear

... and so on, explicitly linking visuals to both lyrics and inferred audio properties ...
```

## Parameters
- `lyrics`: The lyrics of the song.
- `audio_properties`: The inferred audio properties of the song.
- `timestamped_lines`: A list of lyric lines, each associated with a start timestamp (in `[MM:SS]` format).

## Example Usage
```
I have the lyrics, inferred audio properties, and timestamped lines for a song and I need to create a timestamped lyrical storyboard that incorporates the inferred audio properties.
```

## Expected Output
A timestamped lyrical storyboard, ensuring the visual ideas are directly informed by and connected to the audio property analysis.
