# 📊 DSA Profiler (`dsa-profiler-rishad`)

A local-first, production-grade profiling framework engineered for developers and students to benchmark Data Structures and Algorithms (DSA) solutions. The tool captures high-precision runtime execution metrics, monitors dynamic peak memory allocation, tracks local performance history via an embedded relational database, and utilizes empirical statistical curve-fitting to programmatically predict algorithmic Big-O complexities.

## ✨ Core Engineering Features

- **⏱️ High-Precision Performance Benchmarking:** Bypasses standard wrapper latencies using hardware-level system counters (`time.perf_counter`). Utilizes customizable multi-iteration tracking and calculates **median execution runtimes** to systematically filter out background operating system process jitter.
- **🧠 Dynamic Peak Memory Tracking:** Integrates native virtual memory space tracking via `tracemalloc` to capture the exact maximum byte footprint utilized by an algorithm during execution.
- **💾 Persistent Local Data Storage Engine:** Built with a serverless relational `sqlite3` data layer. Automatically initializes and manages a hidden repository file (`.dsa_profile_history.db`) inside the execution workspace to preserve historical performance states across terminal runs.
- **📈 Automated Optimization Delta Engine:** Computes exact optimization shifts between successive approaches using structural percentage metrics. Generates beautiful, color-coded tabular comparisons (`rich`) displaying runtime shifts, memory gains, or regression warnings.
- **🚀 Empirical Asymptotic Analyzer:** Runs solutions over variable scaling input sizes ($N$) and implements a **Pure-Python Ordinary Least Squares (OLS) Linear Regression Engine**. Computes Pearson Correlation Coefficients ($R^2$) across distinct linearized transformation spaces to predict mathematical time complexities ($O(1)$, $O(\log N)$, $O(N)$, $O(N \log N)$, $O(N^2)$).

---

## 🛠️ System Architecture & Mathematical Foundations

### 1. The Optimization Delta Logic
When consecutive alternative approaches are registered under the same `problem_id`, the system isolates the immediately preceding run from the relational database to calculate the exact structural evolution metric:

$$\Delta \text{Time} = \left( \frac{\text{Time}_{\text{previous}} - \text{Time}_{\text{current}}}{\text{Time}_{\text{previous}}} \right) \times 100$$

A positive result signals a **Speedup Success** (color-coded green), whereas a negative result automatically trips a **Performance Drop** warning (color-coded red).

### 2. Empirical Big-O Curve Fitting
Instead of reading code text structures statically, the library profiles data points across a scaling range of $N$ and transforms input parameters to find linear relationships. The system manual regression uses the Pearson Correlation Coefficient ($R$) formula:

$$R = \frac{n\sum xy - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}$$

The model evaluating the highest Coefficient of Determination ($R^2$) closest to `1.0` is programmatically crowned as the predicted asymptotic complexity bound.

---

## 📦 Installation

Ensure you have Python >= 3.8 installed, then fetch the package from the index:

```bash
pip install --index-url [https://test.pypi.org/simple/](https://test.pypi.org/simple/) --extra-index-url [https://pypi.org/simple/](https://pypi.org/simple/) dsa-profiler-rishad


🚀 Practical Guide & Usage
1. Comparative Solution Tracking
Track execution shifts across different iterations of an optimization cycle:

import time
from dsa_profiler import profile_dsa

@profile_dsa(problem_id="two-sum", run_name="brute-force", iteration=3)
def solve_via_brute():
    time.sleep(0.1)  # Simulate nested loop overhead
    return "done"

@profile_dsa(problem_id="two-sum", run_name="hash-map-optimized", iteration=3)
def solve_via_map():
    time.sleep(0.01) # Simulate high-speed lookup
    return "done"

if __name__ == "__main__":
    solve_via_brute()
    solve_via_map()


2. Algorithmic Big-O Estimation
Empirically isolate the asymptotic complexity profile of an approach over expanding dataset sizes:

import time
from dsa_profiler import profile_big_o

@profile_big_o(n_range=[100, 500, 1000, 2000])
def simulate_linear_growth(n):
    for i in range(n):
        pass
    time.sleep(n * 0.00001)

if __name__ == "__main__":
    simulate_linear_growth()


🧱 Project Directory Layout
dsa_profiler/
│
├── src/
│   └── dsa_profiler/
│       ├── __init__.py     # Clean package API exports
│       ├── core.py         # Main execution interceptor decorators
│       ├── storage.py      # SQLite data access persistence layer
│       ├── reporter.py     # Analytics engine & UI generator
│       └── analyzer.py     # Mathematical OLS regression engine
│
├── tests/
│   └── demo.py             # Sandbox execution suite
│
├── pyproject.toml          # Package distribution metadata configurations
└── README.md               # Architecture documentation centerpiece


📄 License
This framework is open-source software licensed under the MIT License.

---

### What to do next:
1. Save this into `README.md`.
2. Follow our rebuild sequence to update the package version to `0.1.1` in `pyproject.toml` and compile it:
   ```cmd
   rmdir /s /q dist
   python -m build


Upload it to TestPyPI:

python -m twine upload --repository testpypi dist/*