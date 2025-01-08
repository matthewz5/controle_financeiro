import pandas as pd

def annual_balance(df_in, df_out):

    df_in_monthly = df_in.groupby(df_in['Data'].dt.to_period('M'))['Total'].sum()
    df_out_monthly = df_out.groupby(df_out['Data'].dt.to_period('M'))['Total'].sum()

    serie_balance = df_in_monthly - df_out_monthly
    df_balance = serie_balance.to_frame()
    df_balance = df_balance.reset_index()

    df_balance = pd.merge(df_balance, df_in_monthly, on='Data', how='left')
    df_balance = pd.merge(df_balance, df_out_monthly, on='Data', how='left')

    df_balance = df_balance.rename(columns={'Valor_x': 'Saldo', 'Valor_y': 'Saldo Entrada', 'Total': 'Saldo Saida'})

    return df_balance