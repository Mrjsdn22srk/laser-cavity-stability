import numpy as np
import matplotlib.pyplot as plt

class LaserCavityAnalyzer:
    def __init__(self, L, R1, R2, wavelength=1064e-9):
        """
        Comprehensive Laser Cavity Analysis Tool
        L: Cavity Length (m)
        R1, R2: Radii of Curvature of mirrors (m). Use 1e10 for flat mirrors.
        wavelength: Laser wavelength (m)
        """
        self.L = L
        self.R1 = R1
        self.R2 = R2
        self.w0_lambda = wavelength

    def calculate_g_parameters(self):
        g1 = 1 - (self.L / self.R1)
        g2 = 1 - (self.L / self.R2)
        return g1, g2

    def analyze_stability(self):
        g1, g2 = self.calculate_g_parameters()
        product = g1 * g2
        is_stable = 0 <= product <= 1
        return is_stable, product

    def calculate_beam_waist_position(self):
        """Calculates minimum waist size and its position from Mirror 1"""
        g1, g2 = self.calculate_g_parameters()
        is_stable, prod = self.analyze_stability()
        
        if not is_stable or prod == 0 or prod == 1:
            return None, None

        # Waist size (w0)
        numerator = self.L * self.w0_lambda
        denominator = np.pi * np.sqrt(prod * (1 - prod))
        term = np.sqrt(g1 * g2 * (1 - g1 * g2)) / np.abs(g1 + g2 - 2*g1*g2)
        w0 = np.sqrt((self.L * self.w0_lambda / np.pi) * term)

        # Distance of waist from Mirror 1 (z1)
        z1 = (self.L * g2 * (1 - g1)) / (g1 + g2 - 2 * g1 * g2)
        return w0, z1

    def plot_results(self):
        is_stable, prod = self.analyze_stability()
        g1, g2 = self.calculate_g_parameters()
        w0, z_waist = self.calculate_beam_waist_position()

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # --- Subplot 1: Stability Diagram ---
        g_range = np.linspace(-2, 2, 500)
        G1, G2 = np.meshgrid(g_range, g_range)
        Stability = G1 * G2
        
        ax1.contourf(G1, G2, Stability, levels=[0, 1], colors=['#90ee90'], alpha=0.5)
        ax1.plot(g1, g2, 'ro', markersize=10, label=f'Your Design (g1*g2={prod:.2f})')
        ax1.axhline(0, color='black', lw=1)
        ax1.axvline(0, color='black', lw=1)
        ax1.set_title("Resonator Stability Region")
        ax1.set_xlabel("g1 = 1 - L/R1")
        ax1.set_ylabel("g2 = 1 - L/R2")
        ax1.grid(True, linestyle='--')
        ax1.legend()

        # --- Subplot 2: Beam Envelope (Waist Propagation) ---
        if is_stable and w0:
            z = np.linspace(0, self.L, 100)
            # Standard beam propagation formula: w(z) = w0 * sqrt(1 + (z/zR)^2)
            z_relative = z - z_waist
            z_rayleigh = (np.pi * w0**2) / self.w0_lambda
            w_z = w0 * np.sqrt(1 + (z_relative / z_rayleigh)**2)

            ax2.plot(z, w_z, 'b', label='Beam Envelope')
            ax2.plot(z, -w_z, 'b')
            ax2.fill_between(z, w_z, -w_z, color='blue', alpha=0.1)
            ax2.set_title("Beam Radius Propagation Inside Cavity")
            ax2.set_xlabel("Cavity Axis z (m)")
            ax2.set_ylabel("Beam Radius (m)")
            ax2.grid(True)
        else:
            ax2.text(0.5, 0.5, "UNSTABLE CAVITY\nNo Guided Mode", ha='center', va='center', color='red', fontsize=14)

        plt.tight_layout()
        plt.show()

# --- Practical Example Run ---
if __name__ == "__main__":
    # Parameters: L=0.5m, R1=0.8m, R2=0.8m
    analyzer = LaserCavityAnalyzer(L=0.5, R1=0.8, R2=0.8)
    
    stable, val = analyzer.analyze_stability()
    print(f"Analysis Complete.")
    print(f"Stability Condition: {'Passed' if stable else 'Failed'}")
    print(f"g1*g2 Product: {val:.4f}")
    
    if stable:
        w0, _ = analyzer.calculate_beam_waist_position()
        print(f"Minimum Waist Radius (w0): {w0*1e6:.2f} microns")
    
    analyzer.plot_results()