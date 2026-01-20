def build_reflection_prompt(user_text, tone, focus):
    return f"""
The user has shared a personal experience.

Your task is to write a reflective emotional summary that:
- Clearly restates what happened in your own words
- Describes how the user felt during and after the event
- Explains why the situation emotionally affected them
- Stays strictly grounded in what the user described

Do NOT invent people or events.
Do NOT write generic emotional statements.

Write the emotional summary as a thoughtful paragraph,
similar to how a human would reflect back the experience.

The emotional summary should be detailed and descriptive
(around 70–90 words).

After the summary, return:
- At least 2 emotions the user felt
- At least 1 stressor from the situation
- At least 1 cognitive pattern (e.g., rumination, self-doubt)
- 2 reflection questions related to the situation
- 2 grounding suggestions appropriate to the situation

User experience:
{user_text}

Support tone: {tone}
Focus mode: {focus}
"""
