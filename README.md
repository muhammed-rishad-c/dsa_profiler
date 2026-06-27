# DSA Profiler

> **`dsa-profiler-rishad`** — A local-first, production-grade profiling framework for benchmarking Data Structures and Algorithms solutions with precision timing, memory tracking, persistent history, and empirical Big-O complexity prediction.

---

## Features

- **High-Precision Benchmarking** — Uses hardware-level system counters (`time.perf_counter`) with multi-iteration tracking and median runtime calculation to filter out OS process jitter.
- **Peak Memory Tracking** — Integrates `tracemalloc` to capture the exact maximum byte footprint consumed by an algorithm during execution.
- **Persistent History** — Serverless `sqlite3` data layer automatically initializes a hidden `.dsa_profile_history.db` file in your workspace to preserve performance states across runs.
- **Optimization Delta Engine** — Computes exact improvement shifts between successive approaches with color-coded `rich` tables showing runtime speedups or regression warnings.
- **Empirical Big-O Analyzer** — Runs solutions over variable input sizes $N$ using a Pure-Python OLS Linear Regression engine to predict time complexities: $O(1)$, $O(\log N)$, $O(N)$, $O(N \log N)$, $O(N^2)$.

---

## Installation

Requires **Python >= 3.8**.

```bash
pip install dsa-profiler-rishad
```

---

## Usage

### Comparative Solution Tracking

Track runtime and memory shifts across different iterations of an optimization cycle:

```python
import time
from dsa_profiler import profile_dsa

@profile_dsa(problem_id="two-sum", run_name="brute-force", iteration=3)
def solve_via_brute():
    time.sleep(0.1)  # Simulate nested loop overhead
    return "done"

@profile_dsa(problem_id="two-sum", run_name="hash-map-optimized", iteration=3)
def solve_via_map():
    time.sleep(0.01)  # Simulate high-speed lookup
    return "done"

if __name__ == "__main__":
    solve_via_brute()
    solve_via_map()
```

### Big-O Complexity Estimation

Empirically isolate the asymptotic complexity profile of an algorithm over expanding dataset sizes:

```python
import time
from dsa_profiler import profile_big_o

@profile_big_o(n_range=[100, 500, 1000, 2000])
def simulate_linear_growth(n):
    for i in range(n):
        pass
    time.sleep(n * 0.00001)

if __name__ == "__main__":
    simulate_linear_growth()
```

---

## How It Works

### Optimization Delta

When consecutive approaches are registered under the same `problem_id`, the system retrieves the preceding run from the database and computes:

$$\Delta \text{Time} = \left( \frac{\text{Time}_{\text{previous}} - \text{Time}_{\text{current}}}{\text{Time}_{\text{previous}}} \right) \times 100$$

A positive result signals a **Speedup** (green), a negative result triggers a **Regression Warning** (red).

### Big-O Curve Fitting

The analyzer profiles execution time across a scaling range of $N$, transforms inputs into linearized spaces, and applies the Pearson Correlation Coefficient to each transformation:

$$R = \frac{n\sum xy - (\sum x)(\sum y)}{\sqrt{\left[n\sum x^2 - (\sum x)^2\right]\left[n\sum y^2 - (\sum y)^2\right]}}$$

The complexity model with the highest $R^2$ (closest to `1.0`) is selected as the predicted asymptotic bound.

---

## Project Structure

```
dsa_profiler/
├── src/
│   └── dsa_profiler/
│       ├── __init__.py      # Package API exports
│       ├── core.py          # Decorator-based execution interceptors
│       ├── storage.py       # SQLite persistence layer
│       ├── reporter.py      # Analytics engine and rich UI output
│       └── analyzer.py      # OLS regression and Big-O engine
├── tests/
│   └── demo.py              # Sandbox execution suite
├── pyproject.toml           # Package distribution metadata
└── README.md
```

---

## License

This project is open-source software licensed under the **MIT License**.
