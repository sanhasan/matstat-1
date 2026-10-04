import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma, norm


def plot_normal(statistics):
    titles = {
        "mean": "Выборочное среднее",
        "variance": "Выборочная дисперсия",
        "median": "Выборочная медиана",
    }
    fig, axes = plt.subplots(
        len(statistics), 3, figsize=(14, 3.4 * len(statistics)),
        sharex=True, sharey=True, squeeze=False, layout="constrained",
    )
    x = np.linspace(-4, 4, 500)

    for row, (n, values) in enumerate(statistics.items()):
        for column, (name, title) in enumerate(titles.items()):
            ax = axes[row, column]
            ax.hist(values[name], bins=55, range=(-4, 4), density=True,
                    color="skyblue", edgecolor="white", alpha=0.75)
            ax.plot(x, norm.pdf(x), color="red", label="Плотность N(0, 1)")
            ax.set_title(f"{title}, n = {n}")
            ax.set_xlim(-4, 4)

        axes[row, 0].set_ylabel("Плотность")

    axes[0, 0].legend()
    return fig


def plot_gamma(statistics, k, j):
    fig, axes = plt.subplots(
        2, len(statistics), figsize=(14, 6.5),
        squeeze=False, layout="constrained",
    )

    for column, (n, (lower, upper)) in enumerate(statistics.items()):
        rows = [
            (lower, k, rf"$nF(X_{{({k})}})$"),
            (upper, j, rf"$n[1-F(X_{{(n-{j-1})}})]$"),
        ]

        for row, (values, shape, title) in enumerate(rows):
            ax = axes[row, column]
            right = gamma.ppf(0.999, a=shape)
            x = np.linspace(0, right, 500)

            ax.hist(
                values, bins=55, range=(0, right), density=True,
                color="lightgreen", edgecolor="white", alpha=0.75,
            )
            ax.plot(
                x, gamma.pdf(x, a=shape), color="red",
                label=rf"Плотность $\Gamma({shape},1)$",
            )
            ax.set_title(f"{title}, n = {n}")
            ax.set_xlim(0, right)

    for ax in axes[:, 0]:
        ax.set_ylabel("Плотность")
        ax.legend()

    return fig