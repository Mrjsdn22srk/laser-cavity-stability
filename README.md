# laser-cavity-stability
A Python tool for laser resonator stability analysis and beam waist propagation using ABCD matrix formalism.
# Laser Cavity Stability Analysis Tool 🔬

A professional Python framework for analyzing the stability of optical resonators and visualizing Gaussian beam propagation using the **ABCD Matrix Formalism**.

---

## 📖 Overview
This tool allows researchers and students to simulate laser cavity configurations. It calculates the stability criteria, determines the beam waist size and position, and provides visual representations of the resonator's mode.



## ✨ Features
* **Stability Analysis**: Instant calculation of $g_1$ and $g_2$ parameters.
* **Stability Condition**: Checks the criteria $0 \leq g_1g_2 \leq 1$.
* **Beam Propagation Mapping**: Visualizes the beam envelope ($w(z)$) across the cavity length.
* **Waist Calculation**: Determines the minimum beam radius ($w_0$) and its exact location.
* **Automated Plotting**: Generates high-quality stability maps and propagation profiles.

## 📐 Mathematical Background
The stability of a two-mirror resonator is governed by the round-trip ABCD matrix. For a cavity with length $L$ and mirrors with radii $R_1$ and $R_2$:

1.  **Stability Parameters**: 
    $$g_1 = 1 - \frac{L}{R_1}, \quad g_2 = 1 - \frac{L}{R_2}$$
2.  **Stability Condition**:
    $$0 \leq g_1g_2 \leq 1$$
3.  **Beam Waist ($w_0$)**: Calculated based on the wavelength ($\lambda$) and cavity geometry to ensure a self-consistent Gaussian mode.



## 🚀 Installation & Usage

### Prerequisites
Make sure you have Python installed, then install the required libraries:
```bash
pip install numpy matplotlib
