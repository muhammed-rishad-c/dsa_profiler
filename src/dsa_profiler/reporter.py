from typing import List, Dict, Any
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class ConsoleReporter:
    @staticmethod
    def generate_report(problem_id: str, current_run: Dict[str, Any], history: List[Dict[str, Any]]) -> None:
        """Calculates performance deltas and displays a beautiful terminal analytics dashboard."""
        
        
        table = Table(title=f"Performance Logs for: [bold cyan]{problem_id}[/bold cyan]", title_justify="left")
        table.add_column("Run Name", style="bold white")
        table.add_column("Execution Time", justify="right")
        table.add_column("Peak Memory", justify="right")
        table.add_column("Timestamp", style="dim", justify="center")
        
        
        for run in history:
            
            if run['run_name'] == current_run['run_name'] and run['execution_time_ms'] == current_run['execution_time_ms']:
                table.add_row(
                    f"[bold yellow]→ {run['run_name']}[/bold yellow]",
                    f"[bold yellow]{run['execution_time_ms']:.4f} ms[/bold yellow]",
                    f"[bold yellow]{run['peak_memory_mb']:.4f} MB[/bold yellow]",
                    run['timestamp']
                )
            else:
                table.add_row(
                    run['run_name'],
                    f"{run['execution_time_ms']:.4f} ms",
                    f"{run['peak_memory_mb']:.4f} MB",
                    run['timestamp']
                )

        
        console.print("\n")
        console.print(table)
        
        
        if len(history) > 1:
            prev_run = history[-2] 
            
            
            time_delta = ((prev_run['execution_time_ms'] - current_run['execution_time_ms']) / prev_run['execution_time_ms']) * 100
            mem_delta = ((prev_run['peak_memory_mb'] - current_run['peak_memory_mb']) / prev_run['peak_memory_mb']) * 100
            
            if time_delta >= 0:
                time_msg = f"[bold green]🔥 Speedup Success:[/bold green] Your new approach is [bold green]{time_delta:.1f}% FASTER[/bold green] than '{prev_run['run_name']}'!"
            else:
                time_msg = f"[bold red]⚠️ Performance Drop:[/bold red] Execution time slowed down by [bold red]{abs(time_delta):.1f}%[/bold red]."
                
            if mem_delta >= 0:
                mem_msg = f"[bold green]📉 Memory Optimization:[/bold green] Saved [bold green]{mem_delta:.1f}%[/bold green] more space."
            else:
                mem_msg = f"[bold yellow]⚠️ Memory Overhead:[/bold yellow] This approach consumed [bold yellow]{abs(mem_delta):.1f}% MORE[/bold yellow] RAM."
                
            summary_panel = Panel(
                f"{time_msg}\n{mem_msg}",
                title="[bold gold1]Optimization Insights[/bold gold1]",
                border_style="bright_blue",
                expand=False
            )
            console.print(summary_panel)
        else:
            console.print(Panel("[bold green]✨ Baseline Recorded![/bold green]\nCreate an alternate solution setup to generate comparative analytics graphs.", title="Insights", expand=False))