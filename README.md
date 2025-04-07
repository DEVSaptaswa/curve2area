# 📐 curve2area

**curve2area** is a web application that calculates the **area under a curve** using two modes:

- 📤 **Image Upload:** Analyze a graph image to extract and integrate the plotted curve.
- ✍️ **Equation Input:** Enter a mathematical function using LaTeX-style syntax with custom limits.

---

## 🚀 Features

- Upload graph images and extract curves using OpenCV
- Auto-detect x and y axis limits
- Enter mathematical functions like `sin(x)`, `x**2 + 3`, `exp(-x**2)`
- Specify lower and upper integration limits (e.g. 0 to π)
- Compute numerical area using trapezoidal or Simpson's rule
- Display result and visual output (processed image or plot)
- Simple and intuitive web interface (Flask-powered)

---

## 🧱 Project Structure

```
curve2area/
├── app/
│   ├── image_processing.py      # Handles image-based curve extraction
│   ├── integration.py           # Numerical integration logic
│   └── equation_plotter.py      # Parses, plots, and integrates equations
│
├── web/
│   ├── static/                  # CSS / JS assets
│   ├── templates/
│   │   ├── index.html           # Main form (upload or input)
│   │   └── result.html          # Display results
│   └── app.py                   # Flask application logic
│
├── uploads/                     # Temporary upload folder
├── requirements.txt             # Python dependencies
├── .gitignore                   # Ignore virtual env and temporary files
└── README.md                    # You're reading this!
```

---

## 📦 Requirements

Install Python packages using:

```bash
pip install -r requirements.txt
```

### Required Libraries:

- `flask`
- `opencv-python`
- `numpy`
- `scipy`
- `sympy`
- `matplotlib`

---

## 🛠️ Running the App

```bash
# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the web app
python web/app.py
```

Open your browser at [http://localhost:5000](http://localhost:5000)

---

## ✍️ Equation Input Example

```text
Equation:     sin(x)**2
x min:        0
x max:        pi
```

You’ll get:
- The plotted curve
- The computed area under it
- A smooth visual of the result

---

## 📌 Roadmap

- [ ] OCR or axis calibration for graph scales
- [ ] Annotated output images
- [ ] Multiple curve handling
- [ ] CSV export
- [ ] Production deployment (e.g. Render, Heroku)
- [ ] UI enhancements

---

## 🤝 Contributing

Open to contributions! Fork the repo, create a new branch, and submit a PR.

---

## 📜 License

MIT License — free to use, modify, and distribute.
```

Let me know if you want this turned into an actual `README.md` file in your project, or if you'd like a badge section or project screenshot included!