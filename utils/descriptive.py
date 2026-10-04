"""Описательные статистики для всего набора и отдельных классов."""

import numpy as np
import pandas as pd


def describe(x):
    """Посчитать характеристики одного массива значений."""
    q1, median, q3 = np.quantile(x, [0.25, 0.5, 0.75])
    return {
        "n": len(x),
        "среднее": x.mean(),
        "дисперсия": x.var(),
        "ст. откл.": x.std(),
        "медиана": median,
        "min": x.min(),
        "max": x.max(),
        "Q1": q1,
        "Q3": q3,
        "IQR": q3 - q1,
    }


def describe_groups(groups):
    """Собрать характеристики всех групп в таблицу."""
    stats = pd.DataFrame({name: describe(x) for name, x in groups.items()}).T
    stats["n"] = stats["n"].astype(int)
    return stats
