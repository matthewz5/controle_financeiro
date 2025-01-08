import matplotlib.pyplot as plt
from src.def_config.colors_dict import colors_dict

def plot_cat_value(df, col_cat, plot_title, save_path):

    plt.figure(figsize=(8, 8))

    wedges, texts, autotexts = plt.pie(df['Total'],
                                    autopct='%1.2f%%',
                                    startangle=90,
                                    pctdistance=1.15,
                                    wedgeprops=dict(width=0.4, edgecolor='white'),
                                    colors=[colors_dict[color] for color in df[col_cat]])

    plt.setp(autotexts, size=12, weight="bold")

    legendas_categorias = [f"{categoria} | R$ {valor:.2f}" for categoria, valor in zip(df[col_cat], df['Total'])]

    plt.legend(legendas_categorias, loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12, title=col_cat.upper())

    ax = plt.gca()
    ax.annotate(f"TOTAL\nR$ {df['Total'].sum():.2f}", 
                xy=(0.5, 0.5), 
                xycoords='axes fraction', 
                ha='center', 
                va='center', 
                fontsize=12,
                weight="bold",
                bbox=dict(boxstyle="square", alpha=0))

    plt.title(plot_title)

    # plt.show(block=False)

    plt.savefig(f'{save_path}/{col_cat}_value_plot', dpi=500, bbox_inches='tight')