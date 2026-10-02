User submits text, or later an image.
A parser or classifier decides whether it is arithmetic, algebra, calculus, matrix math, etc.
The app converts that into a structured representation like:
{"type":"quadratic","expression":"x^2 + 5x + 6 = 0"}
A real math engine executes it.
The response returns the answer, steps, and confidence.
That is better than letting an LLM "solve" the math because:

Deterministic math is repeatable and auditable.
You can show exact intermediate steps.
You avoid hallucinated answers.
It is easier to test.