import pandas as pd

def processing_date(df, col):

    df[col] = pd.to_datetime(df[col], format='%d/%m/%Y')

    return df

def processing_hour(df, col):

    df[col] = pd.to_datetime(df[col], format='%H:%M:%S').dt.time

    return df

def processing_value(df, col):
    
    df[col] = df[col].str.replace(',', '.')
    df[col] = df[col].astype(float)

    return df

def processing_money(df, col):

    df[col] = df[col].str.replace('R$', '')
    df[col] = df[col].str.replace('.', '')
    df[col] = df[col].str.replace(',', '.')
    df[col] = df[col].astype(float)

    return df