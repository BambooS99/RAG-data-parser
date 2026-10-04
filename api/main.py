from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from anthropic import Anthropic
from api import schemas
from api.services import problem_router

load_dotenv()
client = Anthropic()


CLASSIFIER_INSTRUCTIONS = """
Classify the users message as a simple arithmetic operation:
addition, subtraction, multiplication, or division.


do not calculate or solve anything. Extract only numeric operands, 
preserving their original order.

If the message is unclear, combines operands, or is not one of these simple arithmetic problems, use problem_type: "unknown", 
normalized input  as an empty list, and needs_clarification as true. 

return only the fields required by the provided schema

"""

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

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: schemas.ChatRequest) -> schemas.ChatResponse:
    message= req.message
    classification = classify_problem(message)
    solver = problem_router.route_problem(classification)

    return schemas.ChatResponse(
        message = message,
        classification = classification,
        solver = solver,
    )

#functions

"""classification function"""
def classify_problem(message: str) -> schemas.ClassificationResult:
    response = client.messages.parse(
        model = "claude-haiku-4-5",
        max_tokens=256,
        system=CLASSIFIER_INSTRUCTIONS,
        messages=[{"role": "user", "content": message}],
        output_format=schemas.ClassificationResult,
    )
    return response.parsed_output






@app.get("/")

def read_root():
    return {"message": "welcome to the application"}