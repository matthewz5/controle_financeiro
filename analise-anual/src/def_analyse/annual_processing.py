from src.def_config.date import start_date, end_date

import pandas as pd

dates = pd.date_range(start=start_date, end=end_date, freq='D')

def in_out_accumulated(df_in, df_out):

    df_out_value = df_out.groupby('Data', as_index=False)['Total'].sum()
    df_in_value = df_in.groupby('Data', as_index=False)['Total'].sum()

    df_out_acc_value = pd.merge(pd.DataFrame({'Data': dates}), df_out_value, on='Data', how='left')
    df_in_acc_value = pd.merge(pd.DataFrame({'Data': dates}), df_in_value, on='Data', how='left')
    
    df_out_acc_value.fillna({'Total': 0}, inplace=True)
    df_in_acc_value.fillna({'Total': 0}, inplace=True)

    df_in_out_acc_value = pd.DataFrame({'Data': dates})

    df_in_out_acc_value = pd.merge(df_in_out_acc_value, df_out_acc_value, on='Data', how='left')
    df_in_out_acc_value = pd.merge(df_in_out_acc_value, df_in_acc_value, on='Data', how='left')

    df_in_out_acc_value = df_in_out_acc_value.rename(columns={'Valor_x': 'Valor_saida', 'Valor_y': 'Valor_entrada'})

    df_in_out_acc_value['Valor_saida_acc'] = df_in_out_acc_value['Valor_saida'].cumsum()
    df_in_out_acc_value['Valor_entrada_acc'] = df_in_out_acc_value['Valor_entrada'].cumsum()
    
    return df_in_out_acc_value