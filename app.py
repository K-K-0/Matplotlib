# Creating an advanced Matplotlib practice notebook for the user
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
import os

cells = []

# Title and intro
cells.append(new_markdown_cell("# 🚀 Advanced Matplotlib Practice Notebook\n\n"
                               "This notebook contains **progressive practice exercises** (intermediate → advanced) to deepen your Matplotlib skills. "
                               "Each exercise has a description, starter code, and hints. Try to solve the problems in the provided code cells.\n\n"
                               "**How to use:** Run the first cell (imports & helpers). For each exercise, write your solution in the code cell below the prompt.\n"))

# Imports cell
imports = """
# Run this cell first
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Optional: for 3D plotting
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# Make plots appear inline in Jupyter
%matplotlib inline

# Set a default figure size for convenience
plt.rcParams['figure.figsize'] = (8, 5)
print('Libraries loaded. Ready to practice!')
"""
cells.append(new_code_cell(imports))

exercises = [
    {
        "title": "1. Line plot — advanced styling",
        "desc": "Plot x = np.linspace(0, 2*np.pi, 100). Plot sin(x) and cos(x) with different linestyles, markers every 10 points, and a legend. Add grid and a title that shows the functions' formulas.",
        "starter": "# Data\nx = np.linspace(0, 2*np.pi, 100)\n\n# Your code here\n"
    },
    {
        "title": "2. Multiple subplots with GridSpec",
        "desc": "Create a 2x2 layout using GridSpec. Top-left: line plot of sin(x). Top-right: scatter of random points. Bottom: a bar chart spanning both bottom cells.",
        "starter": "# Data\nx = np.linspace(0, 10, 50)\ny = np.sin(x)\n\n# Your code here\n"
    },
    {
        "title": "3. Twin axes (different scales)",
        "desc": "Plot x vs x^2 on the left y-axis and x vs exp(x)/1000 on the right y-axis using twin axes. Label both y-axes and use different colors.",
        "starter": "x = np.linspace(0, 10, 200)\n\n# Your code here\n"
    },
    {
        "title": "4. Scatter with colormap + colorbar",
        "desc": "Create 300 random points for x and y, color them by their distance from origin, and add a colorbar. Use marker size variation too.",
        "starter": "rng = np.random.default_rng(42)\nx = rng.normal(size=300)\ny = rng.normal(size=300)\n\n# Your code here\n"
    },
    {
        "title": "5. Histogram: density, cumulative, and overlay",
        "desc": "Generate 1000 samples from a normal distribution and plot both a histogram (density=True) and the corresponding KDE-like smooth curve (you can use np.histogram to compute bin centers). Also produce a cumulative histogram on a twin axis.",
        "starter": "data = np.random.normal(loc=0, scale=1, size=1000)\n\n# Your code here\n"
    },
    {
        "title": "6. Bar chart — grouped bars with error bars",
        "desc": "Create grouped bars for 3 categories over 4 groups (use random values). Add error bars and annotated bar values on top of bars.",
        "starter": "groups = ['G1', 'G2', 'G3', 'G4']\ncat_values = np.abs(np.random.randn(3, 4)) * 10\nerrors = np.random.rand(3,4)\n\n# Your code here\n"
    },
    {
        "title": "7. Stacked bar chart and percentage annotation",
        "desc": "Create a stacked bar chart from a (4 x 3) dataset and annotate each segment with its percentage contribution within the bar.",
        "starter": "data = np.abs(np.random.randn(4,3))\nlabels = ['A','B','C']\nindex = np.arange(4)\n\n# Your code here\n"
    },
    {
        "title": "8. Boxplot and violin plot comparison",
        "desc": "Generate 4 groups of data with different distributions and plot them side-by-side using boxplot and violinplot for comparison.",
        "starter": "rng = np.random.default_rng(0)\ngroups = [rng.normal(loc=i, scale=0.6, size=200) for i in range(4)]\n\n# Your code here\n"
    },
    {
        "title": "9. Heatmap from 2D array with annotations",
        "desc": "Create a 10x10 matrix with a smooth gradient (e.g., outer product or Gaussian) and plot it using imshow. Add value annotations on each cell (rounded to 2 decimals).",
        "starter": "x = np.linspace(-1,1,10)\nX, Y = np.meshgrid(x, x)\nZ = np.exp(-(X**2 + Y**2))\n\n# Your code here\n"
    },
    {
        "title": "10. Image display with imshow (use a random RGB array)",
        "desc": "Create and show a 200x200 RGB image array with a circular gradient (use radius to set intensity). Turn off the axes.",
        "starter": "h, w = 200, 200\ncy, cx = h//2, w//2\nY, X = np.ogrid[:h, :w]\nR = np.sqrt((X-cx)**2 + (Y-cy)**2)\n\n# Your code here\n"
    },
    {
        "title": "11. Polar plot: rose curve",
        "desc": "Plot r = sin(5*theta) in polar coordinates. Make it visually pleasing with filled area and gridlines.",
        "starter": "theta = np.linspace(0, 2*np.pi, 400)\n\n# Your code here\n"
    },
    {
        "title": "12. 3D surface plot",
        "desc": "Create a 3D surface plot of z = sin(sqrt(x^2+y^2))/(sqrt(x^2+y^2)) over a grid. Add a colorbar from a ScalarMappable.",
        "starter": "x = np.linspace(-6,6,80)\ny = np.linspace(-6,6,80)\nX, Y = np.meshgrid(x, y)\nR = np.sqrt(X**2 + Y**2)\nZ = np.sin(R) / (R + 1e-6)\n\n# Your code here\n"
    },
    {
        "title": "13. Errorbars + fill_between for uncertainty visualization",
        "desc": "Plot y = sin(x) with shaded uncertainty (mean ± std) using fill_between. Also add errorbar points at sampled x locations.",
        "starter": "x = np.linspace(0, 4*np.pi, 200)\nmean = np.sin(x)\nstd = 0.2 + 0.2 * np.abs(np.sin(0.5*x))\n\n# Your code here\n"
    },
    {
        "title": "14. Custom ticks, minor ticks and formatters",
        "desc": "Plot any function and customize major ticks to be at every pi/2 and minor ticks at pi/8. Use formatted tick labels (e.g., 0, π/2, π).",
        "starter": "x = np.linspace(0, 2*np.pi, 100)\ny = np.sin(x)\n\n# Your code here\n"
    },
    {
        "title": "15. Final challenge — Mini dashboard (combine 3 plots)",
        "desc": "Using a pandas DataFrame with a time index of 60 days and columns 'A', 'B', 'C' (random walks), create a mini-dashboard: left large line plot (time series of A,B,C), top-right histogram of returns of A, bottom-right boxplot of returns grouped by weekday. Make the layout clean and annotated.",
        "starter": "rng = np.random.default_rng(1)\ndates = pd.date_range(end=pd.Timestamp.today(), periods=60)\nvals = rng.normal(scale=0.02, size=(60,3))\nprices = 100 + np.cumsum(vals, axis=0)\ndf = pd.DataFrame(prices, index=dates, columns=['A','B','C'])\n\n# Your code here\n"
    }
]

# Add exercises to cells
for ex in exercises:
    cells.append(new_markdown_cell(f"## {ex['title']}\n\n{ex['desc']}"))
    cells.append(new_code_cell(ex['starter']))
    # Add a hint cell
    hint = "### Hint\n- Think about using `ax.twinx()`, `plt.subplots()` with `gridspec_kw`, `np.meshgrid`, and `plt.imshow`.\n- Use `ax.annotate(...)` for annotation tasks.\n- For grouped bars: compute bar positions with `np.arange()` and offsets.\n\n# When you finish, run the cell above to display your plot."
    cells.append(new_markdown_cell(hint))

# Add optional solutions section (hidden by default to avoid spoiling)
cells.append(new_markdown_cell("----\n\n## (Optional) Solutions\n\nIf you'd like, I can add a separate notebook with full solutions after you attempt these. Tell me when you're ready to see solutions—I'll create a solutions notebook so you can compare approaches."))

nb = new_notebook(cells=cells)

# Save notebook
file_path = "matplotlib_practice_advanced.ipynb"
with open(file_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

file_path, os.path.exists(file_path)
