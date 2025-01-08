def cat_dist(df):

    df = df.groupby([df['Data'].dt.to_period("M"), 'Categoria'])['Total'].sum().reset_index()

    df['Data'] = df['Data'].dt.strftime('%b')

    df_value = df.pivot(index='Data', columns='Categoria', values='Total').fillna(0)

    ordem_meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    df_value = df_value.reindex(ordem_meses)

    df_porcentagem = (df_value.divide(df_value.sum(axis=1), axis=0) * 100).round(2)

    return df_value