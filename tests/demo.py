import time
from src.dsa_profiler.core import profile_dsa

@profile_dsa(problem_id="two-sum", run_name="brute-force", iteration=3)
def solve_via_brute():
    # Simulate high complexity loop latency
    time.sleep(0.1) 
    return "done"

@profile_dsa(problem_id="two-sum", run_name="hash-map-optimized", iteration=3)
def solve_via_map():
    # Simulate high speed indexed lookups
    time.sleep(0.01)
    return "done"

if __name__ == "__main__":
    print("Executing Solution Optimization Workflow Pipeline...\n")
    solve_via_brute()
    solve_via_map()