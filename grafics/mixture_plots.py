import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def plot_asymptotic_variances(epsilon, mean_variance, median_variance, crossings):
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
    for ax, right in zip(axes, (1.0, 0.1)):
        mask = epsilon <= right
        ax.plot(epsilon[mask], mean_variance[mask], color="blue", label="среднее")
        ax.plot(epsilon[mask], median_variance[mask], color="green", label="медиана")
        for crossing in crossings[crossings <= right]:
            ax.axvline(crossing, color="gray", linestyle="--", linewidth=1)
        ax.set_xlabel("доля выбросов ε")
        ax.set_ylabel("n · Var")
        ax.grid(alpha=0.3)
        ax.legend()

    axes[0].set_title("ε от 0 до 1")
    axes[1].set_title("то же, крупно при маленьких ε")
    fig.tight_layout()
    return fig


def plot_estimator_distributions(results, theoretical):
    limit = 4 * np.sqrt(theoretical[max(results)][0])
    x = np.linspace(-limit, limit, 400)
    fig, axes = plt.subplots(
        2, len(results), figsize=(14, 6.5), sharex=True, squeeze=False,
    )

    for column, (eps, (mean_errors, median_errors)) in enumerate(results.items()):
        mean_variance, median_variance = theoretical[eps]
        rows = [
            ("среднее", mean_errors, mean_variance, "skyblue"),
            ("медиана", median_errors, median_variance, "lightgreen"),
        ]
        for row, (name, errors, variance, color) in enumerate(rows):
            ax = axes[row, column]
            ax.hist(errors, bins=60, range=(-limit, limit),
                    density=True, color=color, alpha=0.6)
            ax.plot(x, norm.pdf(x, scale=np.sqrt(variance)), color="red")
            ax.set_title(f"{name}, ε = {eps}")

    for ax in axes[1]:
        ax.set_xlabel("√n (оценка − μ)")
    fig.tight_layout()
    return fig
