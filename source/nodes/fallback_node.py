from source.agent.agent import EmotionalReflectionResult

def safe_fallback_response(tone: str, user_text: str) -> EmotionalReflectionResult:
    return EmotionalReflectionResult(
        emotional_summary=(
            "Based on the experience described, the user appears to be reflecting on a situation that caused "
            "emotional discomfort and internal tension. The event seems to have had a lingering emotional impact, "
            "leading the user to replay the situation and question their own reactions. There is a sense of regret "
            "and emotional heaviness, suggesting that the interaction or experience mattered deeply to them. "
            "This response reflects an effort to process the situation and understand its emotional significance."
        ),
        detected_emotions=["stress", "self-doubt"],
        emotional_intensity="medium",
        key_stressors=["emotionally difficult interaction"],
        cognitive_patterns=["rumination"],
        reflection_questions=[
            "What part of the situation is staying with you the most?",
            "What emotions came up for you during or after this experience?"
        ],
        grounding_suggestions=[
            "Take a pause and reflect on how the situation made you feel emotionally.",
            "Allow yourself some time before revisiting the situation again."
        ],
        support_tone=tone,
        confidence_score=0.6,
        safety_note="This reflection is not medical or therapeutic advice."
    )
