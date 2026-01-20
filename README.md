Personal Reflection Agent

A full-stack generative AI application that helps users reflect on emotionally difficult experiences by transforming free-form personal input into a structured emotional reflection.

Built using Pydantic AI, with strict schema validation, fallback handling, and a polished end-to-end user experience.

🔍 What This Project Does

The Personal Reflection Agent allows users to describe a personal situation or experience they found emotionally challenging.
The system analyzes the input and returns a structured reflective response that is grounded strictly in the user’s story.

Each response includes:

A detailed emotional summary

Detected emotions and emotional intensity

Key stressors involved in the situation

Cognitive patterns (e.g., rumination, self-doubt)

Reflection questions for self-awareness

Grounding suggestions appropriate to the situation

⚠️ This application is designed for reflection and emotional awareness, not therapy, diagnosis, or medical advice.

🧭 User Flow

User enters a description of a personal experience

User selects:

Support tone (gentle / neutral / direct)

Focus mode (emotion / thought / action)

The AI agent processes the input

A structured emotional reflection is returned in real time

🏗️ Technical Architecture
Backend

FastAPI – API layer and request handling

Pydantic AI – Agent orchestration and LLM interaction

Pydantic models – Strict output schema validation

Fallback handling – Ensures a safe, schema-valid response when input is unclear or the model fails

Retry & validation controls – Improves reliability and stability

Frontend

Gradio – Simple and responsive UI for user interaction

Model Access

Uses OpenRouter via an OpenAI-compatible API for LLM access

🛡️ Validation & Reliability

All AI outputs must conform to a predefined Pydantic schema

Minimum structure and content constraints are enforced

If the model output fails validation or the input is unclear, a fallback response is returned

This prevents crashes, retry loops, and invalid responses

🌐 Live Deployment

🔗 Live App:
https://personal-reflection-agent.onrender.com

Note: On Render Free tier, the app may take ~30–50 seconds to wake up after inactivity.

📂 Repository Structure
personal_reflection_agent/
├── app.py              # FastAPI backend
├── main.py             # ASGI entrypoint (Render)
├── gradio_app.py       # Gradio UI
├── requirements.txt
├── source/
│   ├── agent/
│   ├── graph/
│   ├── nodes/
│   ├── schema/
│   ├── state/
│   └── utils/

▶️ Run Locally
1️⃣ Clone the repository
git clone https://github.com/siva05-orbit/personal_reflection_agent.git
cd personal_reflection_agent

2️⃣ Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://openrouter.ai/api/v1

5️⃣ Run the app
uvicorn main:app --host 127.0.0.1 --port 8000


Open:

http://127.0.0.1:8000
