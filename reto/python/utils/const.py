VARIABLE_COLORS = {
    "CO": "#FFA070",
    "NO": "#FFB090",
    "NO2": "#FFC0A8",
    "NOX": "#FFCC98",
    "O3": "#7EAA92",
    "PM10": "#FF5B22",
    "PM2.5": "#FF9130",
    "PRS": "#9ED2BE",
    "RAINF": "#FFC0FF",
    "RH": "#90D0FF",
    "SO2": "#FFB8B0",
    "SR": "#FFC8A8",
    "TOUT": "#90C8B8",
    "WSR": "#FFD9B7",
    "WDR": "#FFC090",
}

ALL_ZONES = [
    "CENTRO",
    "NORESTE",
    "NORESTE2",
    "NOROESTE",
    "NOROESTE2",
    "NORTE",
    "NORTE2",
    "SUR",
    "SURESTE",
    "SURESTE2",
    "SURESTE3",
    "SURESTE",
    "SURESTE2",
]

SELECTED_ZONES = [
    "NORTE2",
    "CENTRO",
    "SURESTE3",
]

ALL_VARS = [
    "date",
    "CO",
    "NO",
    "NO2",
    "NOX",
    "O3",
    "PM10",
    "PM2.5",
    "PRS",
    "RAINF",
    "RH",
    "SO2",
    "SR",
    "TOUT",
    "WSR",
    "WDR",
]

INTEREST_VARS = [
    "PM2.5",
    "PM10",
    "SO2",
    "NO2",
    "WDR",
    "WSR",
    "RH"
]

METEOR_VARS = [
    "PM2.5",
    "WDR",
    "WSR",
    "RH"
]


COMPLETE_DATASETS_PATH = [
    "../../datos/01_complete_datasets/NORTE2_2020_2023.csv",
    "../../datos/01_complete_datasets/NOROESTE2_2020_2023.csv",
    "../../datos/01_complete_datasets/SURESTE3_2020_2023.csv",
    "../../datos/01_complete_datasets/CENTRO_2020_2023.csv",
    "../../datos/01_complete_datasets/NORESTE_2020_2023.csv",
    "../../datos/01_complete_datasets/NORESTE2_2020_2023.csv",
    "../../datos/01_complete_datasets/NOROESTE_2020_2023.csv",
    "../../datos/01_complete_datasets/NORTE_2020_2023.csv",
    "../../datos/01_complete_datasets/SURESTE_2020_2023.csv",
    "../../datos/01_complete_datasets/SURESTE2_2020_2023.csv",
    "../../datos/01_complete_datasets/SUROESTE_2020_2023.csv",
    "../../datos/01_complete_datasets/SUROESTE2_2020_2023.csv",
    "../../datos/01_complete_datasets/SUR_2020_2023.csv",
]

CLEANED_DATASETS_PATH = [
    "../../datos/02_cleaned_datasets/NORTE2_2020_2023.csv",
    "../../datos/02_cleaned_datasets/NOROESTE2_2020_2023.csv",
    "../../datos/02_cleaned_datasets/SURESTE3_2020_2023.csv",
    "../../datos/02_cleaned_datasets/CENTRO_2020_2023.csv",
    "../../datos/02_cleaned_datasets/NORESTE_2020_2023.csv",
    "../../datos/02_cleaned_datasets/NORESTE2_2020_2023.csv",
    "../../datos/02_cleaned_datasets/NOROESTE_2020_2023.csv",
    "../../datos/02_cleaned_datasets/NORTE_2020_2023.csv",
    "../../datos/02_cleaned_datasets/SURESTE_2020_2023.csv",
    "../../datos/02_cleaned_datasets/SURESTE2_2020_2023.csv",
    "../../datos/02_cleaned_datasets/SUROESTE_2020_2023.csv",
    "../../datos/02_cleaned_datasets/SUROESTE2_2020_2023.csv",
    "../../datos/02_cleaned_datasets/SUR_2020_2023.csv",
]

GROUPED_DATASETS_PATH = [
    "../../datos/03_grouped_datasets/NORTE2_2020_2023.csv",
    "../../datos/03_grouped_datasets/NOROESTE2_2020_2023.csv",
    "../../datos/03_grouped_datasets/SURESTE3_2020_2023.csv",
    "../../datos/03_grouped_datasets/CENTRO_2020_2023.csv",
    "../../datos/03_grouped_datasets/NORESTE_2020_2023.csv",
    "../../datos/03_grouped_datasets/NORESTE2_2020_2023.csv",
    "../../datos/03_grouped_datasets/NOROESTE_2020_2023.csv",
    "../../datos/03_grouped_datasets/NORTE_2020_2023.csv",
    "../../datos/03_grouped_datasets/SURESTE_2020_2023.csv",
    "../../datos/03_grouped_datasets/SURESTE2_2020_2023.csv",
    "../../datos/03_grouped_datasets/SUROESTE_2020_2023.csv",
    "../../datos/03_grouped_datasets/SUROESTE2_2020_2023.csv",
    "../../datos/03_grouped_datasets/SUR_2020_2023.csv",
]

"""
df_norte2 = pd.read_csv(
    "../../datos/01_complete_datasets/NORTE2_2020_2023.csv", parse_dates=["date"]
)
df_noroeste2 = pd.read_csv(
    "../../datos/01_complete_datasets/NOROESTE2_2020_2023.csv", parse_dates=["date"]
)
df_sureste3 = pd.read_csv(
    "../../datos/01_complete_datasets/SURESTE3_2020_2023.csv", parse_dates=["date"]
)

df_centro = pd.read_csv(
    "../../datos/01_complete_datasets/CENTRO_2020_2023.csv", parse_dates=["date"]
)
df_noreste = pd.read_csv(
    "../../datos/01_complete_datasets/NORESTE_2020_2023.csv", parse_dates=["date"]
)
df_noreste2 = pd.read_csv(
    "../../datos/01_complete_datasets/NORESTE2_2020_2023.csv", parse_dates=["date"]
)
df_noroeste = pd.read_csv(
    "../../datos/01_complete_datasets/NOROESTE_2020_2023.csv", parse_dates=["date"]
)
df_norte = pd.read_csv(
    "../../datos/01_complete_datasets/NORTE_2020_2023.csv", parse_dates=["date"]
)
df_sureste = pd.read_csv(
    "../../datos/01_complete_datasets/SURESTE_2020_2023.csv", parse_dates=["date"]
)
df_sureste2 = pd.read_csv(
    "../../datos/01_complete_datasets/SURESTE2_2020_2023.csv", parse_dates=["date"]
)
df_suroeste = pd.read_csv(
    "../../datos/01_complete_datasets/SUROESTE_2020_2023.csv", parse_dates=["date"]
)
df_suroeste2 = pd.read_csv(
    "../../datos/01_complete_datasets/SUROESTE2_2020_2023.csv", parse_dates=["date"]
)
df_sur = pd.read_csv(
    "../../datos/01_complete_datasets/SUR_2020_2023.csv", parse_dates=["date"]
)
"""