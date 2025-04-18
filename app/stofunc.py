import math

def string_to_function(equation_str):
    # Allowed names in the equation
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    
    # Add 'x' as a placeholder
    def f(x):
        return eval(equation_str, {"__builtins__": {}}, {**allowed_names, "x": x})
    
    return f