import pandas as pd
import numpy as np


def first_valid_data(series: pd.Series):
    for val in series:
        if not np.isnan(val):
            return val


def last_valid_data(series: pd.Series):
    for val in series[::-1]:
        if not np.isnan(val):
            return val


def mfill(series: pd.Series) -> pd.DataFrame:
    series_ = series.copy()
    if np.isnan(series_.iloc[0]):
        series_.iloc[0] = first_valid_data(series_)
    if np.isnan(series_.iloc[len(series_) - 1]):
        series_.iloc[len(series_) - 1] = last_valid_data(series_)

    next_valid_index_series = pd.Series(
        np.where(~series_.isna(), series_.index, np.nan)
    )

    next_valid_index_series = next_valid_index_series.bfill().astype(int)
    next_valid_index_series = next_valid_index_series[series_.isna()]

    for i in series_[series_.isna()].keys():
        next_valid_value = series_.loc[next_valid_index_series.loc[i]]
        prev_valid_value = series_.loc[i - 1]
        series_.loc[i] = (next_valid_value + prev_valid_value) / 2

    return series_


def concat_raw_data(zone: str):
    df = pd.concat(
        [
            pd.read_excel(
                "../../datos/00_raw_datasets/DATOS_HISTORICOS_2020_2021_TODAS_ESTACIONES.xlsx",
                sheet_name=f"{zone}",
                parse_dates=["date"],
            ),
            pd.read_excel(
                "../../datos/00_raw_datasets/DATOS_HISTORICOS_2022_2023_TODAS_ESTACIONES.xlsx",
                sheet_name=f"{zone}",
                parse_dates=["date"],
            ),
        ]
    ).sort_values("date")

    return df


def date_fill(
    df: pd.DataFrame,
    start_period: str = "2020-01-01 00:00:00",
    end_period: str = "2023-08-17 23:00:00",
):
    date_range = (
        pd.date_range(
            start_period,
            end_period,
            freq="h",
        )
        .to_series()
        .reset_index(drop=True)
    )

    date_range.name = "date"
    date_range = date_range.to_frame()

    print(date_range.loc[~date_range["date"].isin(df["date"])])

    # Se imputan las fechas que faltan en el dataset con valores nulos para después llenarlos
    return (
        pd.concat(
            [
                df,
                date_range.loc[~date_range["date"].isin(df["date"])],
            ],
        )
        .sort_values("date")
        .reset_index(drop=True)
    )
