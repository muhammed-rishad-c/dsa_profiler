import functools
import time
import tracemalloc
from typing import Any,Callable,Dict,List
from dsa_profiler.storage import StorageEngine
from dsa_profiler.reporter import ConsoleReporter
from dsa_profiler.analyzer import BigOAnalyzer

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


def profile_big_o(n_range: List[int]) -> Callable:
    
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            from rich.console import Console
            from rich.panel import Panel
            console = Console()
            
            data_points = []
            result = None

            console.print(f"\n[bold magenta][Big-O Analyzer][/bold magenta] Benchmarking [cyan]{func.__name__}[/cyan] over N = {n_range}...")

            for n in n_range:
                
                tracemalloc.start()
                start_time = time.perf_counter()
                
                
                result = func(n, *args, **kwargs)
                
                end_time = time.perf_counter()
                _, peak_bytes = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                time_ms = (end_time - start_time) * 1000
                data_points.append((n, time_ms))
                
                console.print(f"  • N = {n:<7} | Time: {time_ms:.4f} ms | Peak Memory: {peak_bytes/(1024*1024):.4f} MB")

            
            estimated_complexity = BigOAnalyzer.estimate_complexity(data_points)

            console.print(Panel(
                f"Based on empirical growth trends, the estimated time complexity is:\n\n[bold green]🚀 {estimated_complexity}[/bold green]",
                title="[bold magenta]Asymptotic Analysis Result[/bold magenta]",
                border_style="magenta",
                expand=False
            ))
            
            return result
        return wrapper
    return decorator
            
            