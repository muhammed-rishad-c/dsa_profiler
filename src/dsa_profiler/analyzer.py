import math
from typing import List, Tuple

class BigOAnalyzer:
    @staticmethod
    def estimate_complexity(data_points: List[Tuple[int, float]]) -> str:
        
        if len(data_points) < 3:
            return "Inconclusive (Need at least 3 data points)"

        
        models = {
            "O(1)": lambda n, t: (1.0, t),
            "O(log N)": lambda n, t: (math.log(n) if n > 1 else 0.0, t),
            "O(N)": lambda n, t: (float(n), t),
            "O(N log N)": lambda n, t: (n * math.log(n) if n > 1 else 0.0, t),
            "O(N^2)": lambda n, t: (float(n ** 2), t)
        }

        best_fit = "O(1)"
        highest_r_squared = -1.0

        
        for complexity, transform in models.items():
            try:
                transformed_points = [transform(n, t) for n, t in data_points]
                r_sq = BigOAnalyzer._calculate_r_squared(transformed_points)
                
                if r_sq > highest_r_squared:
                    highest_r_squared = r_sq
                    best_fit = complexity
            except (ValueError, ZeroDivisionError):
                continue

        return best_fit

    @staticmethod
    def _calculate_r_squared(points: List[Tuple[float, float]]) -> float:
        
        n = len(points)
        sum_x = sum(p[0] for p in points)
        sum_y = sum(p[1] for p in points)
        sum_x_sq = sum(p[0]**2 for p in points)
        sum_y_sq = sum(p[1]**2 for p in points)
        sum_xy = sum(p[0] * p[1] for p in points)

        numerator = (n * sum_xy) - (sum_x * sum_y)
        denominator_x = (n * sum_x_sq) - (sum_x ** 2)
        denominator_y = (n * sum_y_sq) - (sum_y ** 2)

        if denominator_x == 0 or denominator_y == 0:
            return 0.0

        
        r = numerator / math.sqrt(denominator_x * denominator_y)
        return r ** 2