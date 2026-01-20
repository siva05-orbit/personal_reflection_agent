Personal Reflection Agent

A full-stack generative AI application designed to help users reflect on emotionally significant experiences in a structured, grounded, and non-judgmental manner.

The system analyzes a user’s personal narrative and returns a validated, structured reflection including emotional context, stressors, cognitive patterns, reflection questions, and grounding suggestions. The application does not provide therapy, diagnosis, or medical advice.

Project Motivation

People often struggle to clearly understand their emotional state after difficult experiences such as workplace conflicts, relationship issues, or moments of self-doubt. This project explores how a structured AI agent can support personal reflection by accurately restating a user’s experience and highlighting emotional and cognitive signals present in their narrative.

Live Deployment

Live application URL:
https://personal-reflection-agent.onrender.com

Technology Stack
Backend

FastAPI for API development

Pydantic AI for agent orchestration and strict output validation

Pydantic v2 for request and response schemas

OpenRouter (OpenAI-compatible API) for language model access

Frontend

Gradio for interactive user interface

Infrastructure

Render for cloud deployment

GitHub for version control

Environment variables for secure configuration

Core Features

Structured emotional reflection based on real user input

Context-aware emotional summaries grounded in the user’s experience

Detection of emotions, stressors, and cognitive patterns

Reflection questions aligned with the situation described

Grounding suggestions appropriate to the user’s context

Configurable support tone and focus mode

Strict schema validation using Pydantic AI

Retry handling and safe fallbacks for model reliability

Application Flow

User submits a personal experience via the UI

Optional parameters allow customization of tone and focus

Request is processed by a Pydantic AI agent

Agent generates a validated structured response

Frontend displays the reflection results to the user

API Specification
Endpoint

POST /reflect

Request Body
{
  "user_text": "I had a stressful meeting at work...",
  "support_tone": "gentle",
  "focus_mode": "thought"
}

Response Body
{
  "success": true,
  "data": {
    "emotional_summary": "...",
    "detected_emotions": ["stress", "self-doubt"],
    "emotional_intensity": "medium",
    "key_stressors": ["workplace feedback"],
    "cognitive_patterns": ["rumination"],
    "reflection_questions": [...],
    "grounding_suggestions": [...],
    "support_tone": "gentle"
  }
}

Local Development Setup
Clone the Repository
git clone https://github.com/siva05-orbit/personal_reflection_agent.git
cd personal_reflection_agent

Create Virtual Environment
python -m venv .venv
source .venv/bin/activate


Windows:

.venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Create Environment File
OPENAI_API_KEY=your_openrouter_key
OPENAI_BASE_URL=https://openrouter.ai/api/v1
API_URL=http://127.0.0.1:8000/reflect

Run Backend
uvicorn app:app --reload

Run Frontend
python gradio_app.py

Deployment

The application is deployed on Render as a web service

Environment variables are configured through the Render dashboard

No secrets or configuration values are committed to GitHub

Automatic redeployment occurs on every push to the main branch
