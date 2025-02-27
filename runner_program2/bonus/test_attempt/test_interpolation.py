import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
x = np.arange(10)
y = np.sin(x)
cs = CubicSpline(x, y)
xs = np.arange(-0.5, 9.6, 0.1)
fig, ax = plt.subplots(figsize=(6.5, 4))


ax.plot(x, y, 'o', label='data')
ax.plot(xs, np.sin(xs), label='true')
ax.plot(xs, cs(xs), label="S")
ax.plot(xs, cs(xs, 1), label="S'")
ax.plot(xs, cs(xs, 2), label="S''")
ax.plot(xs, cs(xs, 3), label="S'''")
ax.set_xlim(-0.5, 9.5)
ax.legend(loc='lower left', ncol=2)
plt.show()

# t = np.arange(10)
# csx = CubicSpline(t, X)
# csy = CubicSpline(t, Y)
# tc = np.arange(0, 10, 0.1)
# curvx = csx(tc) # tc absc curv
# curvy = csy(tc) # tc absc curv
ax.plot(curvx, curvy)
# curvx_der1 = csx(tc,1) # tc absc curv
# curvy_der1 = csy(tc,1) # tc absc curv
