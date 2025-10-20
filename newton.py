import numpy as np
import time

def newton_fractal(f, df, roots, re_lim, im_lim, N=1000, max_iter=255, tol=1e-7):
    """
    Вычисляет фрактал Ньютона.
    Возвращает:
        root_index — массив индексов корней
        iterations — массив числа итераций
        converged — булев массив сходимости
    """
    start = time.time()
    re, im = np.linspace(*re_lim, N), np.linspace(*im_lim, N)
    X, Y = np.meshgrid(re, im[::-1])
    Z = np.array(X + 1j*Y, dtype=np.complex128)

    root_index = np.full(Z.shape, -1, dtype=int)
    iterations = np.zeros(Z.shape, dtype=int)
    converged = np.zeros(Z.shape, dtype=bool)

    for k in range(1, max_iter + 1):
        denom = df(Z)
        denom = np.where(np.abs(denom) < 1e-12, 1e-12, denom)
        Z -= f(Z)/denom

        for i, r in enumerate(roots):
            close = np.abs(Z - r) < tol
            new = close & ~converged
            root_index[new] = i
            iterations[new] = k
            converged[new] = True

        if converged.all():
            break

    iterations[~converged] = max_iter
    root_index[~converged] = len(roots)
    print(f"done in {time.time() - start:.1f}s, convergence {np.mean(converged)*100:.1f}%, max iter {np.max(iterations)}")
    return root_index, iterations, converged
