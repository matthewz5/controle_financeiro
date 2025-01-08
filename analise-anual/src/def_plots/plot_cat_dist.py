import matplotlib.pyplot as plt
import seaborn as sns

from src.def_config.colors_dict import colors_dict

def plot_cat_dist(df, category, categories, save_path):

    categories = sorted(categories)

    paleta_cores_cinza = sns.color_palette("gray", n_colors=len(categories))
    colors = {cat: paleta_cores_cinza[i] for i, cat in enumerate(categories)}
    colors[category] = colors_dict[category]

    df.plot(kind='bar', stacked=True, color=[colors[col] for col in df.columns],  width=0.75)

    plt.title('DISTRIBUIÇÃO MENSAL DAS CATEGORIAS DE SAÍDA', fontsize=16)

    plt.xlabel('Período')
    plt.ylabel('Porcentagem do Valor Total (%)')

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(True)
    plt.gca().spines['bottom'].set_visible(True)

    plt.legend('', frameon=False)

    # plt.show()

    plt.savefig(f'{save_path}/Cat_plot/{category}_dist_plot', dpi=500, bbox_inches='tight')