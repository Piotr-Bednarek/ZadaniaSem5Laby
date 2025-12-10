import json
import numpy as np

nb_path = r"C:\Users\janek\Documents\ZadaniaSem5Laby\uso\lab7.ipynb"

try:
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Remove the last broken cell if it contains "S2.np.e" or similar incomplete text
    if nb['cells'] and "S2.np.e" in "".join(nb['cells'][-1]['source']):
        nb['cells'].pop()
        print("Removed incomplete last cell from lab7.ipynb")

    new_cell_source = [
        "# LQR Comparison: Infinite vs Finite Horizon\\n",
        "from scipy.linalg import solve_continuous_are, inv\\n",
        "from scipy.integrate import odeint\\n",
        "import matplotlib.pyplot as plt\\n",
        "import numpy as np\\n",
        "\\n",
        "# System Definitions (RLC Model from notebook)\\n",
        "R_sys = 0.5\\n",
        "L = 0.2\\n",
        "C = 0.5\\n",
        "\\n",
        "A = np.array([[0, 1], [-1/(L*C), -R_sys/L]])\\n",
        "B = np.array([[0], [1/L]])\\n",
        "\\n",
        "# User Parameters for LQR\\n",
        "Q = np.eye(2)     # Cost Q = I\\n",
        "R_lqr = 1         # Cost R = 1\\n",
        "S_factor = [1, 100]  # S = 1*I or 100*I\\n",
        "tf_list = [1, 2, 5]  # Time horizons\\n",
        "\\n",
        "# --- 1. Infinite Horizon LQR ---\\n",
        "P_inf = solve_continuous_are(A, B, Q, R_lqr)\\n",
        "K_inf = inv([[R_lqr]]) @ B.T @ P_inf\\n",
        "print(f\"Infinite Horizon K: {K_inf}\")\\n",
        "\\n",
        "def model_lqr_inf(x, t):\\n",
        "    u = -K_inf @ x\\n",
        "    dx = A @ x + B @ u\\n",
        "    return dx.flatten()\\n",
        "\\n",
        "x0 = np.array([2.0, 5.0]) # Initial state\\n",
        "\\n",
        "# --- 2. Finite Horizon LQR & Comparison ---\\n",
        "plt.figure(figsize=(15, 10))\\n",
        "plot_idx = 1\\n",
        "\\n",
        "for s_mult in S_factor:\\n",
        "    S = s_mult * np.eye(2)\\n",
        "    for tf in tf_list:\\n",
        "        # Solve DRE backwards: dP/dtau = A.T P + P A - P B R^-1 B.T P + Q\\n",
        "        # tau = tf - t goes from 0 to tf\\n",
        "        def riccati_rhs(P_flat, tau):\\n",
        "            P = P_flat.reshape(2, 2)\\n",
        "            dP = A.T @ P + P @ A - P @ B @ inv([[R_lqr]]) @ B.T @ P + Q\\n",
        "            return dP.flatten()\\n",
        "        \\n",
        "        tau_span = np.linspace(0, tf, 200)\\n",
        "        P_sol = odeint(riccati_rhs, S.flatten(), tau_span)\\n",
        "        \\n",
        "        # Function to get K(t) from interpolated P(tau)\\n",
        "        def get_K(t):\\n",
        "            tau = tf - t\\n",
        "            if tau < 0: tau = 0\\n",
        "            if tau > tf: tau = tf\\n",
        "            # Simple nearest index for now (or could use interp1d)\\n",
        "            idx = int(tau / tf * (len(tau_span) - 1))\\n",
        "            P_val = P_sol[idx].reshape(2, 2)\\n",
        "            val = inv([[R_lqr]]) @ B.T @ P_val\\n",
        "            return val\\n",
        "\\n",
        "        def model_lqr_fin(x, t):\\n",
        "             if t > tf:\\n",
        "                 return (A @ x).flatten() # Free response after control ends\\n",
        "             K_t = get_K(t)\\n",
        "             u = -K_t @ x\\n",
        "             dx = A @ x + B @ u\\n",
        "             return dx.flatten()\\n",
        "        \\n",
        "        # Comparison Simulation\\n",
        "        t_sim = np.linspace(0, tf + 2, 500) # Sim longer than tf to see effect\\n",
        "        \\n",
        "        x_inf = odeint(model_lqr_inf, x0, t_sim)\\n",
        "        x_fin = odeint(model_lqr_fin, x0, t_sim)\\n",
        "        \\n",
        "        plt.subplot(2, 3, plot_idx)\\n",
        "        plt.plot(t_sim, x_inf[:, 0], 'r--', label='Inf Horizon', alpha=0.6)\\n",
        "        plt.plot(t_sim, x_fin[:, 0], 'b-', label=f'Fin Horizon (tf={tf})')\\n",
        "        plt.axvline(x=tf, color='k', linestyle=':', label='End of Control')\\n",
        "        plt.title(f\"S={s_mult}I, tf={tf}s\")\\n",
        "        plt.xlabel(\"Time [s]\")\\n",
        "        plt.ylabel(\"State x1\")\\n",
        "        plt.legend()\\n",
        "        plt.grid(True)\\n",
        "        plot_idx += 1\\n",
        "\\n",
        "plt.suptitle(\"LQR Finite vs Infinite Horizon Comparison (y=x1)\")\\n",
        "plt.tight_layout()\\n",
        "plt.show()\\n",
        "\\n",
        "print(\"Analysis: Finite horizon controller converges towards the infinite horizon path (turnpike property) when time horizon is large enough.\")\\n",
        "print(\"However, near the end of the horizon (tf), the finite controller deviates to minimize terminal cost S.\")\\n",
        "print(\"If S is small (e.g., I), deviation is larger. If S is large (100*I ~ approximating inf cost), it stays closer.\")\\n"
    ]

    new_cell = {
        "cell_type": "code",
        "execution_count": None,
        "id": "lqr_lab7_comparison",
        "metadata": {},
        "outputs": [],
        "source": new_cell_source
    }

    nb['cells'].append(new_cell)

    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print("Successfully corrected lab7.ipynb and appended LQR comparison.")

except Exception as e:
    print(f"Error: {e}")
