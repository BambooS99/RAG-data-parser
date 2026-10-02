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
def chat(req: ChatRequest) -> "ChatResponse":
    #we will replace this with our RAG logic
    message= req.message
    classification = classify_problem(message)
    solver = route_problem(classification)

    return ChatResponse(
        message = message,
        classification = classification,
        solver = solver,
    )


#classes


"""this creates the shape of the classifier function's return"""
class ClassificationResult(BaseModel):
    problem_type:  str
    normalized_input: str
    confidence: float
    needs_clarification: bool

"""This creates the shape for the router"""
class SolverResult(BaseModel):
    solver_used: str
    success: bool
    result: str

"""this prepares a shape of response for the user"""
class ChatResponse(BaseModel):
    message: str
    classification: ClassificationResult
    solver: SolverResult


#functions

"""classification function"""
def classify_problem(message: str) -> ClassificationResult:
    return ClassificationResult(
        problem_type= "addition",
        normalized_input = message,
        confidence= 1.0,
        needs_clarification= False,
    )


"""router function (/router)"""
def route_problem(classification: ClassificationResult) -> SolverResult:
   if classification.problem_type == "addition":
       return SolverResult(
           solver_used= "addition",
           success= True,
           result = classification.normalized_input,
       )
   else:
       return SolverResult(
       solver_used= "N/A",
       success=False,
       result= "",
   )



@app.get("/")
def read_root():
    return {"message": "welcome to the application"}