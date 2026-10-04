from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from api.solvers import arithmetic
from dotenv import load_dotenv
from anthropic import Anthropic
from api import schemas

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
    #we will replace this with our RAG logic
    message= req.message
    classification = classify_problem(message)
    solver = route_problem(classification)

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


"""router function (/router)"""
def route_problem(classification: schemas.ClassificationResult) -> schemas.SolverResult:
   if classification.problem_type == "addition":
       return schemas.SolverResult(
           solver_used= "addition",
           success= True,
           result = arithmetic.add(classification.normalized_input),
       )
   if classification.problem_type == "multiplication":
       return schemas.SolverResult(
           solver_used= "multiplication",
           success= True,
           result = arithmetic.multiplication(classification.normalized_input),
       )
   if classification.problem_type == "subtraction" :
       return schemas.SolverResult(
           solver_used= "subtraction",
           success= True,
           result = arithmetic.subtract(classification.normalized_input),
       )
   
   else:
       return schemas.SolverResult(
       solver_used= "N/A",
       success=False,
       error_message= "Please try again later. This feature is not currently supported",
   )



@app.get("/")

def read_root():
    return {"message": "welcome to the application"}