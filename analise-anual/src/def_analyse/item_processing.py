def itens_value(df, category):

    df_itens = df[df['Categoria'] == category]

    df_itens = df_itens.groupby('Item', as_index=False)['Total'].sum()

    df_itens = df_itens.sort_values(by='Total', ascending=False)

    return df_itens