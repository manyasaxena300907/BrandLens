# BrandLens

<!-- README.md: the first page people see on GitHub. Update the details below as the project grows. -->

BrandLens is an AI-assisted brand-governance platform for text content (blogs, social posts, marketing emails,
landing page copy and press releases). A brand manager uploads the brand rule book, creators upload their content,
and the AI checks it for tone, terminology, factual accuracy and unsupported claims. Each issue is explained with a
suggested fix, then a human reviewer approves the final content.

**AI-Assisted | Human-Controlled | Explainable Brand Governance**

## Workflow
Upload rule book -> Upload content -> AI review -> Suggestions -> Creator fixes -> Human review -> Approved

## Tech stack
- Frontend: Next.js (JavaScript)
- Backend: FastAPI (Python)
- Database: MongoDB
- AI: Gemini API (can be switched to Azure OpenAI in `backend/app/services/llm_client.py`)

## Project structure
- `backend/` - FastAPI server, AI checkers, routes
- `frontend/` - Next.js web app
- `sample_data/` - demo rule book and sample content with planted mistakes
- `docs/` - architecture, workflow and API notes

## Run the backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows  (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
copy ..\.env.example .env     # Mac/Linux: cp ../.env.example .env  (then fill in your keys)
uvicorn app.main:app --reload
```
Open http://localhost:8000/health to check it works.

## Run the frontend
```bash
cd frontend
copy .env.local.example .env.local   # Mac/Linux: cp .env.local.example .env.local
npm install
npm run dev
```
Open http://localhost:3000

## Team
- [Member 1 name] - backend and AI checks
- [Member 2 name] - frontend and workflow screens

Built for the CODEAXIS Hackathon.
