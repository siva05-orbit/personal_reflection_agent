import gradio as gr
import requests

API_URL = "/api/reflect"  


def reflect_ui(user_text, support_tone, focus_mode):
    if not user_text.strip():
        return "Please enter your experience.", "", "", ""

    payload = {
        "user_text": user_text,
        "support_tone": support_tone,
        "focus_mode": focus_mode
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()["data"]

        summary = data["emotional_summary"]

        emotions = ", ".join(data["detected_emotions"])

        questions = "\n".join(
            f"- {q}" for q in data["reflection_questions"]
        )

        grounding = "\n".join(
            f"- {g}" for g in data["grounding_suggestions"]
        )

        return summary, emotions, questions, grounding

    except Exception as e:
        return f"Error: {e}", "", "", ""


with gr.Blocks(title="Personal Reflection Agent") as demo:
    gr.Markdown("##  Personal Reflection Agent")
    gr.Markdown(
        "Share a situation or experience that affected you emotionally. "
        "The agent will reflect your experience back in a grounded and structured way."
    )

    user_text = gr.Textbox(
        label="Describe your experience",
        placeholder="Example: I had a difficult meeting at work today...",
        lines=6
    )

    with gr.Row():
        support_tone = gr.Dropdown(
            ["gentle", "neutral", "direct"],
            value="gentle",
            label="Support Tone"
        )

        focus_mode = gr.Dropdown(
            ["emotion", "thought", "action"],
            value="thought",
            label="Focus Mode"
        )

    submit_btn = gr.Button("Reflect")

    gr.Markdown("###  Emotional Summary")
    summary_out = gr.Textbox(lines=6, interactive=False)

    gr.Markdown("###  Detected Emotions")
    emotions_out = gr.Textbox(interactive=False)

    gr.Markdown("###  Reflection Questions")
    questions_out = gr.Textbox(lines=4, interactive=False)

    gr.Markdown("###  Grounding Suggestions")
    grounding_out = gr.Textbox(lines=4, interactive=False)

    submit_btn.click(
        reflect_ui,
        inputs=[user_text, support_tone, focus_mode],
        outputs=[summary_out, emotions_out, questions_out, grounding_out]
    )


if __name__ == "__main__":
    demo.launch()
