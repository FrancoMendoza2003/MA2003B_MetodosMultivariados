import pandas as pd


def print_variable_info(df: pd.DataFrame, variables: list[str] | None = None) -> None:
    if not variables:
        variables = list(df.columns)

    for variable in variables:
        print(f"Variable: {df[variable].name}")

        dtype = df[variable].dtype.__str__()
        variable_type = (
            "Numérico"
            if ("int" in dtype) or ("float" in dtype) or ("datetime" in dtype)
            else "Categórico"
        )
        print(f"Tipo de Variable: {variable_type}")
        print(f"Valores Posbles: [{df[variable].min()}, {df[variable].max()}]")
        print(
            f"Cantidad de Valores Nulos: {df[variable].isna().sum()}/{df.shape[0]} -> {(df[variable].isna().sum()/df.shape[0])*100:.02f}%"
        )

        print("-----\n")


def describe_variables(
    df: pd.DataFrame,
    interest_variables: list[str] | None = None,
) -> pd.DataFrame:
    if interest_variables:
        df = df[interest_variables]

    info = (
        df.drop(columns=["date"])
        .describe()
        .rename(
            index={
                "mean": "Media",
                "25%": "Q1",
                "75%": "Q3",
                "50%": "Mediana",
                "max": "Max",
                "min": "Min",
                "std": "Desv. Éstandar",
            }
        )
        .drop(index=["count"])
    )

    info.loc["Varianza"] = info.loc["Desv. Éstandar"] ** 2
    info.loc["Rango"] = info.loc["Max"] - info.loc["Min"]

    return info.apply(lambda var: var.round(2))


def filter_final_data(df: pd.DataFrame) -> pd.DataFrame:
    df["month"] = df["date"].dt.month

    oct_ = df["month"] == 10
    nov_ = df["month"] == 11
    dec_ = df["month"] == 12

    df = df[oct_ | nov_ | dec_].drop("month", axis=1)
    df = df.groupby(pd.Grouper(key="date", freq="D")).mean().reset_index()
    return df
