import numpy as np
import pandas as pd


def n_var_mean(eps, sigma, tau):
    return (1 - eps) * sigma**2 + eps * tau**2


def n_var_median(eps, sigma, tau):
    return np.pi / 2 / ((1 - eps) / sigma + eps / tau) ** 2


def find_crossings(eps_grid, mean_curve, median_curve):
    difference = mean_curve - median_curve
    return eps_grid[1:][np.diff(np.sign(difference)) != 0]


def variance_table(results, n, sigma, tau):
    rows = []
    for eps, (means, medians) in results.items():
        rows.append({
            "ε": eps,
            "среднее средних": means.mean(),
            "среднее медиан": medians.mean(),
            "nVar среднего (опыт)": n * means.var(),
            "nVar среднего (формула)": n_var_mean(eps, sigma, tau),
            "nVar медианы (опыт)": n * medians.var(),
            "nVar медианы (формула)": n_var_median(eps, sigma, tau),
        })
    return pd.DataFrame(rows).set_index("ε")
