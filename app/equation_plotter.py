import matplotlib.pyplot as plt
import numpy as np

def plot_func(f, a=0, b=0, n=1000):
    img_path = "app/static/plots/output.png"
    # full_x = np.linspace(a-2, b+2, n)
    # full_y = [f(x) for x in full_x]

    # x_vals = np.linspace(a, b, n)
    # y_vals = [f(x) for x in x_vals]

    full_x = np.linspace(a - 2, b + 2, n)
    full_y_raw = np.array([f(x) for x in full_x])
    full_y = np.where(np.isfinite(full_y_raw), full_y_raw, np.nan)

    x_vals = np.linspace(a, b, n)
    y_raw = np.array([f(x) for x in x_vals])
    y_vals = np.where(np.isfinite(y_raw), y_raw, np.nan)
    
    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(full_x, full_y, label='f(x)', color='blue')
    plt.fill_between(x_vals, y_vals, color='blue', alpha=0.5)
    plt.title("Function Plot with Area Under the Curve")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.savefig(img_path)
    # plt.show()
    return img_path
