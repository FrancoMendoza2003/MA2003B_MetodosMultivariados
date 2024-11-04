import pandas as pd
import numpy as np

from sklearn.preprocessing import PowerTransformer


def yeo_johnson_transformation(df: pd.DataFrame) -> pd.DataFrame:
    transformer = PowerTransformer(method="yeo-johnson")

    new_df = df.copy()
    lambdas = dict()
    for variable in df.drop("date", axis=1):
        data = df[variable].to_numpy().reshape(-1, 1)

        transformer.fit(data)
        lambdas.update({variable: transformer.lambdas_[0]})

        new_df[variable] = transformer.transform(data).reshape(1, -1)[0]

    return new_df, lambdas


def log_transformation(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df.copy()
    for variable in df.drop("date", axis=1):
        new_df[variable] = np.log(new_df[variable])

    return new_df
