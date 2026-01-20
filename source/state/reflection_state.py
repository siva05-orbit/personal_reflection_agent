from pydantic import BaseModel, Field
from typing import Literal

class ReflectionInputState(BaseModel):
    user_text: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        description="User thoughts or feelings or a story the user is willing to share"
    )
    support_tone: Literal["gentle", "neutral", "direct"] = "gentle"
    focus_mode: Literal["emotion", "thought", "action"] = "emotion"
