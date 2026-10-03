# Implement API with Working AI Integration

**Suggested commit message:** `Implement API with working AI integration`  
**Date:** 2026-10-03

## Summary

This change replaces the hardcoded classifier stub from the previous scaffolding with a real call to Anthropic's Claude model, and connects the `addition` route to an actual arithmetic solver instead of echoing the unevaluated input. It also fixes the `/chat` response-model forward-reference issue noted as a limitation in the previous entry.

## What Changed

- Added `api/solvers/arithmetic.py` with `add(numbers: list[int | float]) -> int | float`, which sums a list of numeric operands.
- Imported the new solver module into `api/main.py` via `from api.solvers import arithmetic`.
- Added Anthropic SDK integration: `load_dotenv()` loads environment variables and `client = Anthropic()` creates the API client, so the Anthropic API key is expected to be supplied through a local `.env` file (already covered by `.gitignore`).
- Added `CLASSIFIER_INSTRUCTIONS`, a system prompt instructing the model to classify a message as addition, subtraction, multiplication, or division, extract only the numeric operands in order without solving them, and fall back to `problem_type: "unknown"` with an empty operand list and `needs_clarification: true` when the message is unclear or unsupported.
- Changed `ClassificationResult.normalized_input` from `str` to `list[int | float]` so it holds extracted numeric operands instead of the raw message text.
- Rewrote `classify_problem(message)` to call `client.messages.parse(...)` with `output_format=ClassificationResult`, returning `response.parsed_output` instead of a fixed `"addition"` stub result.
- Updated `route_problem(classification)` to call `arithmetic.add(classification.normalized_input)` for the `addition` case, producing a real computed sum instead of returning the normalized input unevaluated.
- Reordered `api/main.py` so the `ChatRequest`, `ClassificationResult`, `SolverResult`, and `ChatResponse` models are defined before the `/health` and `/chat` route handlers, and changed the `/chat` return annotation from the string `"ChatResponse"` to the direct `ChatResponse` type. This resolves the forward-reference 500 error reported in the previous entry.

## Current Limitations

- Only `addition` is wired to a real solver. `subtraction`, `multiplication`, and `division` are mentioned in `CLASSIFIER_INSTRUCTIONS` but still fall through `route_problem`'s `else` branch, returning `solver_used: "N/A"` and `success: False`.
- `classify_problem`'s `"unknown"` / `needs_clarification` outcome is not handled as its own case; it is also routed through the same unsupported `else` branch as unimplemented operations, so the clarification signal is dropped before it reaches the response.
- `SolverResult.result` is typed as `str`, but `arithmetic.add` returns `int | float`. Pydantic v2 does not coerce numeric types into `str`, so a successful addition currently raises a validation error (`Input should be a valid string [type=string_type]`) instead of returning the computed result. `result` needs to become `int | float | str` (or the value needs to be cast to `str`) before this path will work end to end.
- `__pycache__` directories for `api` and `api/solvers` were included in this change. `.gitignore` currently excludes `.env` but not `__pycache__`, so compiled bytecode is being tracked.

## Intended Request and Response

Request body:

```json
{
  "message": "5+5"
}
```

Intended response once the `SolverResult.result` typing limitation above is fixed:

```json
{
  "message": "5+5",
  "classification": {
    "problem_type": "addition",
    "normalized_input": [5, 5],
    "confidence": 1.0,
    "needs_clarification": false
  },
  "solver": {
    "solver_used": "addition",
    "success": true,
    "result": 10
  }
}
```

## Verification

- `api/main.py` and `api/solvers/arithmetic.py` passed Python syntax compilation with `python -m py_compile`.
- `arithmetic.add` was exercised directly (`add([5, 5])` → `10`, `add([1.5, 2.5, 3])` → `7.0`) and produces correct sums.
- Reproduced the `SolverResult.result` typing issue directly against Pydantic: constructing the model with an `int` value for the `str`-typed `result` field raises `1 validation error ... Input should be a valid string [type=string_type]`, confirming the limitation above.
- Did not exercise `POST /chat` end-to-end against the live Anthropic API as part of this review; `classify_problem` requires a configured `ANTHROPIC_API_KEY`.
