import functools
import time
import tracemalloc
from typing import Any,Callable,Dict
from src.dsa_profiler.storage import StorageEngine
from src.dsa_profiler.reporter import ConsoleReporter

storage=StorageEngine()

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
            
            storage.save_run(problem_id,run_name,median_time_ms,peak_memory_mb)
            
            historical_runs=storage.get_history(problem_id=problem_id)
            
            current_run_payload = {
                "run_name": run_name,
                "execution_time_ms": median_time_ms,
                "peak_memory_mb": peak_memory_mb
            }
            
            ConsoleReporter.generate_report(problem_id,current_run_payload,historical_runs)
            
            return result
        return wrapper
    return decorator
            
            