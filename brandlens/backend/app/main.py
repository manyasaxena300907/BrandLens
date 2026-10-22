# main.py
# Starts the FastAPI server, enables CORS for the frontend and connects all the routers.
# TODO: include the routers from routes/ (auth, rulebook, content, review) once they are written.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="BrandLens API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # TODO: read FRONTEND_URL from config.py
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}
