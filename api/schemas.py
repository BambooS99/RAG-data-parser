from pydantic import BaseModel


"""this file will hold all of our classes"""

"""this handles the user's input and sends it to the LLM which can transform it into a usable type for our algorithm"""
class ChatRequest(BaseModel):
    message: str

"""this creates the shape of the classifier function's return"""
class ClassificationResult(BaseModel):
    problem_type:  str
    normalized_input: list [int | float]
    confidence: float
    needs_clarification: bool

"""This creates the shape for the router"""
class SolverResult(BaseModel):
    solver_used: str
    success: bool
    result: int | float | None = None
    error_message: str | None = None

"""this prepares a shape of response for the user"""
class ChatResponse(BaseModel):
    message: str
    classification: ClassificationResult
    solver: SolverResult