from api.solvers import arithmetic
from api import schemas

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