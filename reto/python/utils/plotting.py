import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils.const import VARIABLE_COLORS, INTEREST_VARS
from utils.stats import describe_variables

from typing import Literal

sns.set(style="whitegrid", font_scale=1.5)


def box_plot(
    df: pd.DataFrame,
    interest_vars: list[str],
    title: str,
):
    fig, axes = plt.subplots(
        nrows=len(interest_vars) - 1,
        ncols=1,
        figsize=(14, 24),
        sharex=False,
    )

    for i, variable in enumerate(df[interest_vars].drop("date", axis=1)):
        sns.boxplot(
            x=variable,
            data=df,
            ax=axes[i],
            orient="horizontal",
            color=VARIABLE_COLORS.get(variable, "pink"),
        )
        if i == 0:
            axes[i].set_title(title)

        axes[i].set_ylabel(variable)
        axes[i].set_xlabel("")

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()


def hist_plot(
    df: pd.DataFrame,
    interest_vars: list[str],
    title: str,
    bins: int = 50,
):
    fig, axes = plt.subplots(
        nrows=len(interest_vars) - 1,
        ncols=1,
        figsize=(14, 24),
        sharex=False,
    )

    for i, variable in enumerate(df[interest_vars].drop("date", axis=1)):
        sns.histplot(
            df[variable],
            bins=bins,
            kde=False,
            ax=axes[i],
            edgecolor="black",
            color=VARIABLE_COLORS.get(variable, "pink"),
        )
        if i == 0:
            axes[i].set_title(title)

        axes[i].set_ylabel(variable)
        axes[i].set_xlabel("")

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()


def plot_series(
    df: pd.DataFrame,
    title: str,
    interest_vars: list[str],
    freq: Literal["D", "W", "M"],
):
    df_daily = df.set_index("date").groupby(pd.Grouper(freq=freq)).mean()

    for variable in interest_vars[1:]:
        df_daily[variable].plot(
            linewidth=3,
            figsize=(16, 8),
            legend=True,
            color=VARIABLE_COLORS.get(variable, "pink"),
            title=title,
            xlabel="Fecha",
        )


def data_exploration(
    df: pd.DataFrame,
    zone: str,
    interest_vars: list[str] = INTEREST_VARS,
):
    box_plot(
        df,
        interest_vars=interest_vars,
        title=f"Medidas de posición no-central\n{zone}",
    )
    hist_plot(
        df,
        interest_vars=INTEREST_VARS,
        title=f"Distribución de Datos\n{zone}",
    )
    correlation_matrix = df[INTEREST_VARS].drop(columns="date").corr()
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
        annot_kws={"size": 12},
        mask=mask,
        vmin=-1,
        vmax=1,
    )

    info = describe_variables(
        df,
        interest_variables=INTEREST_VARS,
    )

    return info
