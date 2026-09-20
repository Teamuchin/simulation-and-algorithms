# Algorithms & Simulation Exercises

An array-scanning algorithms exercise, and a set of Monte-Carlo simulation experiments built on random sampling with NumPy and Matplotlib.

**Course:** CENG218 (algorithms) and CENG222 (simulation)  
**Institution:** İzmir Institute of Technology (IYTE) — İzmir, Türkiye

## Files

| File | What it does |
|---|---|
| `contiguous-window-max.py` | Scans a temperature series for the contiguous range whose sum is largest, extending the window while the running sum stays positive — the same greedy structure as Kadane's algorithm |
| `law-of-large-numbers.py` | Rolls a die 30,000 times and tracks the running sample mean and variance, plotting the means converging on the theoretical value |
| `sample-mean-experiments.py` | The same convergence experiment across several independent random sources, comparing how quickly each sample mean stabilises |
| `inverse-transform-sampling.py` | Generates a population from a target distribution with the inverse-transform method, then validates the generated sample against the expected density |
| `variance-experiments.py` | Compares empirical variance across sample sizes to show the spread shrinking with n |

## Running

```bash
pip install numpy matplotlib
python law-of-large-numbers.py
```

---

Submitted reports, worksheets and lecture material are archived outside this
repository rather than committed, so the repo stays code-only.
