import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import ticker
import numpy as np

def plot_fractal(root_index, iterations, roots, re_lim, im_lim, filename, title):
    colors = ['#ff0000', '#00ff00', '#0000ff', '#ff00ff', '#ffff00', '#00ffff', '#ff8000']
    n_roots = len(roots)
    cmap = ListedColormap(colors[:n_roots])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5), dpi=150)

    ax1.imshow(root_index, origin='upper', cmap=cmap,
               extent=(re_lim[0], re_lim[1], im_lim[0], im_lim[1]),
               interpolation='nearest')
    ax1.set(title=f'{title}\nБассейны притяжения', xlabel='Re(z)', ylabel='Im(z)')
    ax1.grid(True, alpha=0.2, linestyle='--')

    iter_plot = np.log10(iterations + 1)
    im2 = ax2.imshow(iter_plot, origin='upper', cmap='plasma',
                     extent=(re_lim[0], re_lim[1], im_lim[0], im_lim[1]),
                     interpolation='nearest')
    ax2.set(title=f'{title}\nlog₁₀(итерации + 1)', xlabel='Re(z)', ylabel='Im(z)')

    cbar = plt.colorbar(im2, ax=ax2, orientation='horizontal', shrink=0.8, pad=0.15)
    cbar.set_label('log₁₀(итерации + 1)')

    legend = [plt.Line2D([0],[0], color=colors[i], lw=6,
                         label=f'Корень {i+1}: {r.real:.3f}{"+" if r.imag>=0 else "-"}{abs(r.imag):.3f}i'
                         if abs(r.imag)>1e-10 else f'Корень {i+1}: {r.real:.3f}')
              for i, r in enumerate(roots)]
    ax1.legend(handles=legend, loc='upper right', fontsize=9, framealpha=0.9, shadow=True)

    for ax in (ax1, ax2):
        ax.set_aspect('equal')
        ax.xaxis.set_major_locator(ticker.MaxNLocator(6))
        ax.yaxis.set_major_locator(ticker.MaxNLocator(6))

    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    plt.close(fig)
