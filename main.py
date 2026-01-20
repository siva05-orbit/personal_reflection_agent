from fastapi import FastAPI
from gradio_app import demo
import gradio as gr
from app import app as fastapi_app

app = FastAPI()

app.mount("/api", fastapi_app)
app = gr.mount_gradio_app(app, demo, path="/")
