# Hill Climbing Search Algorithm

A minimal Python implementation of the **Hill Climbing** local search algorithm, demonstrated on a simple 1D optimization problem.

## Overview

Hill Climbing is a greedy, local search algorithm that starts at an arbitrary point and repeatedly moves toward the neighboring state with the highest heuristic value, stopping once no neighbor improves on the current state (a **local maximum**).

This script uses a simple quadratic function as a stand-in "landscape" to search over, making the algorithm's behavior easy to trace and visualize.

## The Objective Function

```python
f(x) = -(x - 5)^2 + 25
```

This is an inverted parabola with its peak (global maximum, value `25`) at `x = 5`. It's used here purely as a toy example — in a real application, `f(x)` would be replaced with whatever heuristic or fitness function you're actually optimizing.

## How It Works

1. **Start** — Begin from a random integer state between `low` and `high` (default `0`–`10`).
2. **Generate Neighbors** — From the current state `x`, generate candidate moves `x - step` and `x + step`, respecting the `low`/`high` bounds.
3. **Select Best Neighbor** — Evaluate `f()` on all neighbors and pick the one with the highest value.
4. **Move or Stop**:
   - If the best neighbor's value is *better* than the current state's, move there and repeat.
   - If no neighbor improves on the current value, stop — this is a local (in this case, also global) maximum.
5. **Return** — The final state reached is returned as the best solution found.

## Usage

Run the script directly:

```bash
python hill_climbing.py
```

Each run picks a random starting integer in `[0, 10]` and prints a step-by-step trace of the climb, e.g.:

```
--- Hill Climbing Trace ---
Start State: 2 Value: 16
Move to: 3 Value: 21
Move to: 4 Value: 24
Move to: 5 Value: 25
STOP at 5 (Local Maximum Reached)

Best solution found: 5
Value of best solution: 25
```

## Functions Reference

| Function | Purpose |
|---|---|
| `f(x)` | The evaluation/heuristic function being maximized. |
| `neighbors(x, step, low, high)` | Returns valid neighboring states of `x` within bounds. |
| `hill_climbing(start, step, low, high)` | Runs the hill climbing loop from `start`, printing each move, and returns the final state. |

## Known Limitation: Local Maxima

Because this example's landscape is a single smooth peak, hill climbing always finds the global maximum. In general, however, plain hill climbing is vulnerable to:

- **Local maxima** — a peak lower than the true global maximum, where the algorithm gets stuck since no immediate neighbor is better.
- **Plateaus** — flat regions where neighbors have equal value, causing the algorithm to stop prematurely.
- **Ridges** — cases where the maximum lies along a path not directly reachable by single-step moves.

## Requirements

- Python 3.x (uses only the standard library — `random`)

## Possible Extensions

- Try multiple random restarts (**random-restart hill climbing**) to reduce the risk of settling on a poor local maximum.
- Add **simulated annealing**-style random moves to escape local maxima/plateaus.
- Extend `f(x)` to a multi-dimensional or more complex/non-convex landscape.
- Track and print the number of steps taken to convergence.
