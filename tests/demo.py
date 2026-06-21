import time
from src.dsa_profiler.core import profile_dsa

@profile_dsa(problem_id="two_sum",run_name="brute_force",iteration=5)
def brute_force_simulation(n):
    data_list=[i for i in range(n)]
    time.sleep(0.05)
    return sum(data_list)

if __name__=="__main__":
    print("starting student code simulation")
    output=brute_force_simulation(1_000_000)
    print(f"function output: {output}")