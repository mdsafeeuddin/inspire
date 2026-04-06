import pandas as pd
from scipy.stats import iqr

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df.convert_dtypes()


def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    cols_to_drop = [
        'race',
        'cpbon_time','cpboff_time','icuin_time','icuout_time',
        'inhosp_death_time','allcause_death_time','case_id'
    ]
    
    existing_cols = [col for col in cols_to_drop if col in df.columns]
    return df.drop(columns=existing_cols)


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['opend_time','opstart_time','anstart_time','anend_time'])

    df['asa'] = df['asa'].fillna(df['asa'].mode()[0])
    df['height'] = df['height'].fillna(df['height'].median())
    df['weight'] = df['weight'].fillna(df['weight'].median())

    return df


def winsorize(df: pd.DataFrame, col: str) -> pd.DataFrame:
    _iqr = iqr(df[col])
    upper = df[col].quantile(0.75) + 1.5 * _iqr
    lower = df[col].quantile(0.25) - 1.5 * _iqr

    df[col] = df[col].astype(float).clip(lower=lower, upper=upper)
    return df


def convert_time(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        'admission_time','orin_time','anstart_time','opstart_time',
        'anend_time','opend_time','orout_time','discharge_time'
    ]

    for col in cols:
        if col in df.columns:
            df[col] = pd.to_timedelta(df[col], unit='m')

    return df


def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['opdate'] == 0]

    outliers = df[df['opstart_time'] >= pd.Timedelta(days=9)].index
    df = df.drop(outliers)

    mask = df.groupby('subject_id')['hadm_id'].transform('count') == 1
    return df[mask]


def preprocess(path: str) -> pd.DataFrame:
    df = load_data(path)
    df = drop_columns(df)
    df = handle_missing(df)

    for col in ['height', 'weight']:
        df = winsorize(df, col)

    df = convert_time(df)
    df = filter_data(df)

    return df