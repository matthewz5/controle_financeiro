from src.def_data.data_collection import get_data
from src.def_data.data_processing import processing_date, processing_hour, processing_value, processing_money

from src.def_analyse.annual_processing import in_out_accumulated
from src.def_analyse.annual_balance import annual_balance
from src.def_analyse.category_processing import categories_value
from src.def_analyse.item_processing import itens_value
from src.def_analyse.category_distribution import cat_dist

from src.def_plots.plot_in_out_acc import plot_in_out_acc
from src.def_plots.plot_monthly_balance import plot_monthly_balance
from src.def_plots.plot_cat_value import plot_cat_value
from src.def_plots.plot_itens_value import plot_itens_value
from src.def_plots.plot_cat_dist import plot_cat_dist

print("="*200, "\n Collection data...")

print("-"*200, "\n Expense notes: \n")
data_out_main = get_data('dados_saida')
print(data_out_main)

print("-"*200, "\n Earning notes: \n")
data_in_main = get_data('dados_entrada')
print(data_in_main)

print("="*200, "\n Processing data...")

print("-"*200, "\n Processed expense notes: \n")
data_out = data_out_main.copy()
data_out = processing_date(data_out, 'Data')
data_out = processing_hour(data_out, 'Hora')
data_out = processing_value(data_out, 'Quantidade')
data_out = processing_money(data_out, 'Valor')
data_out = processing_money(data_out, 'Total')
# print(data_out)

print("-"*200, "\n Processed earning notes: \n")
data_in = data_in_main.copy()
data_in = processing_date(data_in, 'Data')
data_in = processing_date(data_in, 'Periodo')
data_in = processing_money(data_in, 'Total')
# print(data_in)

print("="*200, "\n Annual analysis...")

print("-"*200, "\n Accumulated values: \n")
df_in_out_acc_value = in_out_accumulated(data_in, data_out)
print(df_in_out_acc_value)
plot_in_out_acc(df_in_out_acc_value, r'path')

print("-"*200, "\n Monthly balance: \n")
df_balance = annual_balance(data_in, data_out)
print(df_balance)
plot_monthly_balance(df_balance, 'Saldo', r'path')

print("-"*200, "\n Earning categories percentage: \n")
data_in_categories = categories_value(data_in, 'Origem')
print(data_in_categories)
plot_cat_value(data_in_categories, 'Origem', 'DISTRIBUIÇÃO DE ORIGENS DOS VALORES DE ENTRADA', r'path')

print("="*200, "\n Categorical analysis...")

print("-"*200, "\n Expense categories percentage: \n")
data_out_categories = categories_value(data_out, 'Categoria')
print(data_out_categories)
plot_cat_value(data_out_categories, 'Categoria', 'DISTRIBUIÇÃO DE CATEGORIAS DOS VALORES DE SAÍDA', r'path')

print("-"*200, "\n Expense items percentage per category: \n")
categories = list(data_out_categories['Categoria'].unique())
for cat in categories:
    print('\n', cat, ':')
    df_cat_itens = itens_value(data_out, cat)
    print(df_cat_itens.head(5))
    plot_itens_value(df_cat_itens, cat, r'path')

print("-"*200, "\n Expense category percentage per month: \n")
df_out_dist_perc = cat_dist(data_out)
for cat in categories:
    print('\n', cat, ':')
    plot_cat_dist(df_out_dist_perc, cat, categories, r'path')
    print(df_out_dist_perc[cat])

input("\n Press Enter to exit...")

print("\n ...Done!")
