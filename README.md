# Laser Cavity Stability Analysis Tool 🔬

A professional Python-based framework for analyzing optical resonator stability and visualizing Gaussian beam propagation using the **ABCD Matrix Formalism**.

---

## 📖 Overview
This tool provides a comprehensive analysis of laser cavity configurations. It determines whether a cavity is stable, calculates the beam waist ($w_0$) size and position, and plots the beam's physical profile.



## ✨ Features
* **Stability Analysis**: Instant calculation of $g_1$ and $g_2$ parameters.
* **Stability Condition**: Automatically verifies if $0 \leq g_1g_2 \leq 1$.
* **Beam Propagation Mapping**: Visualizes the beam envelope ($w(z)$) across the entire cavity length.
* **Waist Calculation**: Determines the minimum beam radius ($w_0$) and its exact axial location.
* **High-Quality Plots**: Generates stability maps and propagation profiles using Matplotlib.

## 📐 Mathematical Background
The resonator stability is determined by the round-trip ABCD matrix. For a two-mirror cavity with length $L$ and mirror radii $R_1, R_2$:

1.  **Stability Parameters**: 
    $$g_1 = 1 - \frac{L}{R_1}, \quad g_2 = 1 - \frac{L}{R_2}$$
2.  **Stability Condition**:
    $$0 \leq g_1g_2 \leq 1$$
3.  **Beam Waist ($w_0$)**: Based on wavelength ($\lambda$), the tool solves for the self-consistent Gaussian mode.



## 🚀 Installation & Usage

### 1. Prerequisites
Ensure you have Python 3.x installed. 

### 2. Clone the Repository
```bash
git clone [https://github.com/Mrjsdn22srk/laser-cavity-stability.git](https://github.com/Mrjsdn22srk/laser-cavity-stability.git)
cd laser-cavity-stability
