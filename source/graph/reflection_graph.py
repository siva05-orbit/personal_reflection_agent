from source.state.reflection_state import ReflectionInputState
from source.nodes.reflection_node import run_reflection_node

async def run_reflection_graph(state):
    return await run_reflection_node(state)

