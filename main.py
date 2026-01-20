from fastapi import FastAPI
import gradio as gr

from app import app as fastapi_app
from gradio_app import demo

# Parent FastAPI app
app = FastAPI()

# Mount backend API under /api
app.mount("/api", fastapi_app)

# Mount Gradio UI at root /
app = gr.mount_gradio_app(app, demo, path="/")
