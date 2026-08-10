from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title = "RAG API", version="1.0.0")


# In production, I will set this to the real domain from env vars
# FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "https://yourdomain.com")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], #React Dev server later lets replace this with "FRONTEND_ORIGIN" when deploying
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    #we will replace this with our RAG logic
    return {"reply": f"you said: {req.message}"}

@app.get("/")
def read_root():
    return {"message": "welcome to the application"}