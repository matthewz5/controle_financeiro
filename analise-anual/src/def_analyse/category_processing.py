import pandas as pd #type: ignore

def categories_value(df, col_cat):

    df_cat = df.groupby(col_cat, as_index=False)['Total'].sum()

    df_cat = df_cat.sort_values(by='Total', ascending=False)

    return df_cat