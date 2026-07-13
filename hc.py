import random

# ---------------- OBJECTIVE FUNCTION ----------------
def f(x):
    """
    Define the evaluation (heuristic) function.
    Higher value means better state.

    Example function:
    Maximum value occurs at x = 5
    """
    return -(x - 5) ** 2 + 25


# ---------------- GENERATE NEIGHBORS ----------------
def neighbors(x, step=1, low=0, high=10):
    """
    Generate neighboring states of x within given limits.
    """
    cand = []

    if x - step >= low:
        cand.append(x - step)

    if x + step <= high:
        cand.append(x + step)

    return cand


# ---------------- HILL CLIMBING ----------------
def hill_climbing(start, step=1, low=0, high=10):
    """
    Hill Climbing Algorithm:
    1. Start from initial state.
    2. Generate neighbors.
    3. Select the best neighbor.
    4. Move to it if it improves the heuristic.
    5. Stop when no better neighbor exists.
    """
    current = start

    print("\n--- Hill Climbing Trace ---")
    print("Start State:", current, "Value:", f(current))

    while True:
        neigh = neighbors(current, step=step, low=low, high=high)

        if not neigh:
            break

        # choose neighbor with maximum heuristic value
        next_state = max(neigh, key=f)

        if f(next_state) <= f(current):
            print("STOP at", current, "(Local Maximum Reached)")
            break

        current = next_state
        print("Move to:", current, "Value:", f(current))

    return current


# ---------------- RUN PROGRAM ----------------
"""
1. Choose an initial state.
2. Call hill_climbing().
3. Print final result.
"""

start = random.randint(0, 10)

best = hill_climbing(start, step=1, low=0, high=10)

print("\nBest solution found:", best)
print("Value of best solution:", f(best))