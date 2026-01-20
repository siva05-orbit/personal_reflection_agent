from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from source.state.reflection_state import ReflectionInputState
from source.graph.reflection_graph import run_reflection_graph

app = FastAPI(title="Personal Reflection Agent")

@app.post("/reflect")
async def reflect(state: ReflectionInputState):
    result = await run_reflection_graph(state)
    return {
        "success": True,
        "data": result
    }



