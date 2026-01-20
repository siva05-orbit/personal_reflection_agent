from source.agent.agent import EmotionalReflectionResult

def safe_fallback_response(support_tone: str) -> EmotionalReflectionResult:
    return EmotionalReflectionResult(
        emotional_summary=(
            "I’m having difficulty clearly understanding what you’re trying to express right now. "
            "Your message seems to contain something important, but the situation or emotions behind it "
            "aren’t coming through in a way I can confidently reflect back. This can happen when thoughts "
            "are still forming or when an experience feels hard to put into words."
        ),
        detected_emotions=["uncertainty", "confusion"],
        emotional_intensity="low",
        key_stressors=["unclear or incomplete expression"],
        cognitive_patterns=["difficulty articulating thoughts"],
        reflection_questions=[
            "Would you like to share more details about what happened?",
            "What part of the situation feels hardest to explain right now?"
        ],
        grounding_suggestions=[
            "Take a moment to pause and collect your thoughts before continuing.",
            "Try describing one specific moment or feeling from the experience."
        ],
        support_tone=support_tone
    )
