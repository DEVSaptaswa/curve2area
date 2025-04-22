import math
import numpy as np

def string_to_function(equation_str):
    # Allowed names in the equation
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    
    # Add 'x' as a placeholder
    def f(x):
        try:
            return eval(equation_str, {
                "x": x,
                "sin": np.sin, "cos": np.cos, "tan": np.tan,
                "log": np.log, "exp": np.exp, "sqrt": np.sqrt,
                "pi": np.pi, "e": np.e
            })
        except (ZeroDivisionError, ValueError, OverflowError, FloatingPointError):
            return np.nan
    return f
    
    return f