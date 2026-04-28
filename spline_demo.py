"""
Fibonacci Gravitational Dip : C² Spline Continuity
n=284-289 (JWST z=7-15 tension)
Publication-ready demo
"""

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Fibonacci ticks + scale factor dip (mock JWST data)
n_ticks = np.array([284, 285, 286, 287, 288, 289])
a_fib = np.array([0.85, 0.82, 0.79, 0.81, 0.84, 0.87])

# C² cubic spline (1ère/2ème dérivées continues)
cs = CubicSpline(n_ticks, a_fib)

# Plot haute qualité publication
n_plot = np.linspace(284, 289, 200)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(n_ticks, a_fib, 'ro', markersize=10, label='Fibonacci ticks', zorder=5)
ax.plot(n_plot, cs(n_plot), 'b-', linewidth=3, label='C² spline interpolation')
ax.set_xlabel('Cosmic tick index $n$', fontsize=14)
ax.set_ylabel('Scale factor $a_n$', fontsize=14)
ax.set_title('Fibonacci Gravitational Dip (n=284-289)', fontsize=16, pad=20)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.3)
ax.set_xlim(283.5, 289.5)
plt.tight_layout()
plt.savefig('fib_spline_dip.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Figure générée : fib_spline_dip.png")
print("C² continuity validée entre paliers discrets")
