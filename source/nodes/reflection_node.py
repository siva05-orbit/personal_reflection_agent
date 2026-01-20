from source.agent.agent import reflection_agent
from source.state.reflection_state import ReflectionInputState
from source.nodes.fallback_node import safe_fallback_response
from source.utils.logger import logger
from source.utils.prompt import build_reflection_prompt

async def run_reflection_node(state:ReflectionInputState):
    logger.info("Running reflection agent")

    prompt = build_reflection_prompt(
        state.user_text,
        state.support_tone,
        state.focus_mode
    )

    try:
        result = await reflection_agent.run(
            prompt
        )
        logger.info("Reflection agent succeeded")
        return result.output

    except Exception as e:
        logger.error(f"Reflection agent failed: {e}")
        raise

