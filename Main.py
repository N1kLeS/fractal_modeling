from newton import newton_fractal
from plotting import plot_fractal

# Настройки
re_lim = (-2, 2)
im_lim = (-2, 2)
N = 1500
MAX_ITER = 255
TOL = 1e-7

# Функции и корни
def f_cubic(z): return z**3 - 1
def df_cubic(z): return 3*z**2
roots_cubic = [1, -0.5 + 0.86602540378j, -0.5 - 0.86602540378j]

def f_quartic(z): return z**4 - 1
def df_quartic(z): return 4*z**3
roots_quartic = [1, -1, 1j, -1j]

def f_complex(z): return z**3 + 2*z + 2
def df_complex(z): return 3*z**2 + 2
roots_complex = [-0.770916997059248 + 0j,
                 0.385458498529624 + 1.12188537484296j,
                 0.385458498529624 - 1.12188537484296j]

def f_multiple(z): return z**3 - z**2
def df_multiple(z): return 3*z**2 - 2*z
roots_multiple = [0, 1]

def f_interesting(z): return z**3 - 2*z + 2
def df_interesting(z): return 3*z**2 - 2
roots_interesting = [-1.76929235423863 + 0j,
                     0.884646177119315 + 0.589742805022206j,
                     0.884646177119315 - 0.589742805022206j]

equations = [
    (f_cubic, df_cubic, roots_cubic, "z³ - 1", "fractal_cubic.png"),
    (f_quartic, df_quartic, roots_quartic, "z⁴ - 1", "fractal_quartic.png"),
    (f_complex, df_complex, roots_complex, "z³ + 2z + 2", "fractal_complex.png"),
    (f_multiple, df_multiple, roots_multiple, "z³ - z²", "fractal_multiple.png"),
    (f_interesting, df_interesting, roots_interesting, "z³ - 2z + 2", "fractal_interesting.png")
]

for f, df, roots, title, fname in equations:
    root_idx, iters, conv = newton_fractal(f, df, roots, re_lim, im_lim, N, MAX_ITER, TOL)
    plot_fractal(root_idx, iters, roots, re_lim, im_lim, fname, title)
