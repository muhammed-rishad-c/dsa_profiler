import functools
import time
import tracemalloc
from typing import Any,Callable,Dict

def profile_dsa(problem_id:str,run_name:str,iteration:int=5)->Callable:
    
    def decorator(func:Callable[...,Any])->Callable[...,Any]:
        @functools.wraps(func)
        def wrapper(*args:Any,**kwargs:Any)->Any:
            
            tracemalloc.start()
            execution_times=[]
            result=None
            
            for i in range(iteration):
                
                start_time=time.perf_counter()
                if i==0:
                    result=func(*args,**kwargs)
                else:
                    _=func(*args,**kwargs)
                    
                    
                end_time=time.perf_counter()
                execution_times.append((end_time-start_time)*1000)
                
            _,peak_bytes=tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            execution_times.sort()
            median_time_ms=execution_times[len(execution_times)//2]
            peak_memory_mb=peak_bytes/(1024*1024)
            
            print(f"\n[DSA Profiler] Probing Results for: '{problem_id}' ({run_name})")
            print(f"  - Median Execution Time : {median_time_ms:.4f} ms (over {iteration} runs)")
            print(f"  - Peak Memory Consumption: {peak_memory_mb:.4f} MB")
            print("-" * 60)
            
            return result
        return wrapper
    return decorator
            
            