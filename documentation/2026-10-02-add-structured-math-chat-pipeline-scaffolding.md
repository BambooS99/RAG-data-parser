# Add Structured Math Chat Pipeline Scaffolding

**Suggested commit message:** `Add structured math chat pipeline scaffolding`  
**Date:** 2026-10-02

## Summary

This change introduces the initial structure for a math-focused chat backend. The `/chat` endpoint coordinates classification, routing, and response construction, using Pydantic models to define the data passed between those stages.

## What Changed

- Added `ClassificationResult` to represent the predicted problem type, normalized input, classifier confidence, and whether clarification is needed.
- Added `SolverResult` to represent the selected solver, whether it succeeded, and its result text.
- Added `ChatResponse` to combine the original user message with the classification and solver results.
- Added `classify_problem(message)` as a temporary classifier stub. It currently always labels input as `addition`, uses the original message as normalized input, and returns fixed confidence and clarification values.
- Added `route_problem(classification)` as a temporary router. It returns the normalized input for `addition` without evaluating it; other types return an unsupported result.
- Updated `/chat` to call the classifier, pass its result to the router, and construct a `ChatResponse`.

## Current Limitations

This is scaffolding, not a working math-solving implementation:

- No AI provider is connected. Classification is hardcoded.
- No deterministic arithmetic operation is performed. For example, an input of `5+5` is currently returned as text, not calculated as `10`.
- There is only a placeholder route for `addition`; other problem types are unsupported.
- Step-by-step explanations are not included in `SolverResult` yet.
- The `/chat` route currently declares its response type as the string annotation `"ChatResponse"` before that model is defined. A request produced a 500 error because FastAPI/Pydantic could not resolve this forward reference. Define the response models before the route and annotate it as `ChatResponse` to resolve that issue.

## Intended Request and Response

Request body:

```json
{
  "message": "5+5"
}
```

The intended response structure is:

```json
{
  "message": "5+5",
  "classification": {
    "problem_type": "addition",
    "normalized_input": "5+5",
    "confidence": 1.0,
    "needs_clarification": false
  },
  "solver": {
    "solver_used": "addition",
    "success": true,
    "result": "5+5"
  }
}
```

The response example describes the current stub behavior after the response-model annotation issue is fixed; it does not represent a computed arithmetic answer.

## Verification

- `api/main.py` passed Python syntax compilation with `python -m py_compile api/main.py`.
- The API process started successfully with Uvicorn.
- A `POST /chat` request returned HTTP 500 due to the unresolved `ChatResponse` forward reference described above.
