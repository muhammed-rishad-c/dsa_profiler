import time
from src.dsa_profiler.core import profile_big_o

@profile_big_o(n_range=[100, 500, 1000, 2000])
def simulate_linear(n):
    # O(N) loop simulation
    for i in range(n):
        pass
    time.sleep(n * 0.00001) # Realistic scaling delay

@profile_big_o(n_range=[100, 500, 1000, 2000])
def simulate_quadratic(n):
    # O(N^2) nested loop simulation
    for i in range(n):
        for j in range(100): # simulated inner growth workload
            pass
    time.sleep((n ** 2) * 0.00000001) # Quadratic scaling delay

if __name__ == "__main__":
    simulate_linear()
    print("-" * 60)
    simulate_quadratic()