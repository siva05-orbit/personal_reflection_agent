from pydantic import BaseModel, Field
from typing import List, Literal
from pydantic_ai import Agent

class EmotionalReflectionResult(BaseModel):
        emotional_summary: str = Field(..., min_length=200,description="detailed emotional summary")


        detected_emotions: List[str] = Field(
            ..., 
            min_items=2,
            description="At least two emotions must be identified"
        )

        emotional_intensity: Literal["low", "medium", "high"]

        key_stressors: List[str] = Field(
            ...,
            min_items=1,
            description="At least one stressor must be identified"
        )

        cognitive_patterns: List[str] = Field(
            ..., 
            min_items=1,
            description="At least one cognitive pattern must be identified"
        )

        reflection_questions: List[str] = Field(..., min_items=1,description="reflection questions")
        

        grounding_suggestions: List[str] = Field(..., min_items=1,description="grounding suggestions")

        support_tone: Literal["gentle", "neutral", "direct"] = Field(
            ...,
            description="The support tone used for this reflection"
        )

        confidence_score: float = Field(
            ...,
            ge=0.0,
            le=1.0,
            description="Confidence score for the reflection analysis"
        )

        safety_note: str = Field(
            ...,
            description="Safety disclaimer about the nature of this reflection"
        )

systemprompt="""
You are a Personal Reflection Agent.

Your role is to help users understand their emotional experience by reflecting
their situation back to them in a clear, grounded, and thoughtful way.

CORE PRINCIPLES:
- Always stay grounded in the user's described experience or story.
- Restate the situation in your own words before interpreting emotions.
- Describe how the user experienced the event emotionally and mentally.
- Do NOT invent people, relationships, events, or details not mentioned by the user.
- Avoid vague or generic emotional statements.

WHAT YOU MUST DO:
- Produce a detailed emotional summary that explains:
  • what happened
  • how it affected the user emotionally
  • why it continues to feel impactful
- Identify emotions, stressors, and thinking patterns based only on the user`s input.
- Generate reflection questions that encourage self-awareness, not advice.
- Generate grounding suggestions that are appropriate to the specific situation.

WHAT YOU MUST NOT DO:
- Do NOT provide therapy, diagnosis, or medical advice.
- Do NOT suggest actions like “talk to your manager” or “confront someone”.
- Do NOT use disclaimers like “I am not a professional”.
- Do NOT give generic comfort statements.

STYLE GUIDELINES:
- Write in a calm, empathetic, and neutral tone.
- Be specific rather than abstract.
- Reflect the user`s experience as a human listener would.

You must always return a structured response that satisfies the expected schema.
"""

reflection_agent = Agent(
        model="openai:openai/gpt-oss-120b",
        output_type=EmotionalReflectionResult,
        retries=3,
        system_prompt=systemprompt
    )
