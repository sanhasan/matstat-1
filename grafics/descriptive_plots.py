"""Графики длины лепестка для всего набора Iris и отдельных видов."""

import matplotlib.pyplot as plt
import numpy as np


GROUP_COLORS = {
    "все": "gray",
    "setosa": "tab:blue",
    "versicolor": "tab:orange",
    "virginica": "tab:green",
}


def plot_ecdfs(groups):
    """Показать ЭФР всего набора и трёх видов на соседних панелях."""
    species = [name for name in groups if name != "все"]
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5), sharey=True)

    for ax, names in zip(axes, (["все"], species)):
        for name in names:
            x = np.sort(groups[name])
            y = np.arange(1, len(x) + 1) / len(x)
            ax.step(x, y, where="post", color=GROUP_COLORS[name], label=name)
        for level in (0.25, 0.5, 0.75):
            ax.axhline(level, color="black", linewidth=0.5, linestyle=":")
        ax.set_xlabel("длина лепестка, см")
        ax.grid(alpha=0.3)
        ax.legend()

    axes[0].set_ylabel("доля цветков ≤ x")
    axes[0].set_title("ЭФР по всем цветкам")
    axes[1].set_title("ЭФР по видам")
    fig.tight_layout()
    return fig


def plot_histograms(groups, bins):
    """Построить гистограммы с общими интервалами, средним и медианой."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 7), sharex=True)
    for ax, (name, x) in zip(axes.flat, groups.items()):
        ax.hist(x, bins=bins, color=GROUP_COLORS[name], edgecolor="white")
        ax.axvline(np.mean(x), color="black", linestyle="--", label="среднее")
        ax.axvline(np.median(x), color="red", label="медиана")
        ax.set_title(f"{name} (n = {len(x)})")
        ax.set_ylabel("число цветков")
        ax.legend()

    for ax in axes[1]:
        ax.set_xlabel("длина лепестка, см")
    fig.tight_layout()
    return fig


def plot_boxplots_and_violins(groups):
    """Сравнить box plot и violin plot на общей вертикальной оси."""
    names = list(groups)
    values = [groups[name] for name in names]
    fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True)

    box = axes[0].boxplot(values, patch_artist=True, medianprops={"color": "black"})
    for patch, name in zip(box["boxes"], names):
        patch.set_facecolor(GROUP_COLORS[name])
        patch.set_alpha(0.6)
    axes[0].set_title("Box plot")

    violin = axes[1].violinplot(values, showmedians=True)
    for body, name in zip(violin["bodies"], names):
        body.set_facecolor(GROUP_COLORS[name])
    axes[1].set_title("Violin plot")

    for ax in axes:
        ax.set_xticks(range(1, len(names) + 1), names)
        ax.grid(axis="y", alpha=0.3)
    axes[0].set_ylabel("длина лепестка, см")
    fig.tight_layout()
    return fig
