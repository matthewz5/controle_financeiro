import pandas as pd
import matplotlib.pyplot as plt

def plot_itens_value(df, category, save_path):
    
    df = pd.concat([df.head(10),
                    pd.DataFrame({'Item': ['Outros'], 'Total': [df['Total'][10:].sum()]})],
                    ignore_index=True)

    plt.figure(figsize=(8, 8))

    colors = ['#000000', '#1A1A1A', '#333333', '#4D4D4D', '#666666', '#808080', '#999999', '#B3B3B3', '#CCCCCC', '#E6E6E6', '#FFFFFF']

    wedges, texts, autotexts = plt.pie(df['Total'], 
                                    autopct='%1.2f%%', 
                                    startangle=90, 
                                    pctdistance=1.15, 
                                    colors=colors, 
                                    wedgeprops=dict(width=0.4, edgecolor='white'))

    plt.setp(autotexts, size=12, weight="bold")

    legendas_itens = [f"{item} | R$ {valor:.2f}" for item, valor in zip(df['Item'], df['Total'])]
    
    plt.legend(legendas_itens, loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12, title="ITENS")

    ax = plt.gca()
    ax.annotate(f"TOTAL\nR$ {df['Total'].sum():.2f}", 
                xy=(0.5, 0.5), 
                xycoords='axes fraction', 
                ha='center', 
                va='center', 
                fontsize=12,
                weight="bold",
                bbox=dict(boxstyle="square", alpha=0))

    plt.title(f"DISTRIBUIÇÃO DOS 10 ITENS DE {category.upper()}", fontsize=16, x=0.75, weight="bold")

    # plt.show(block=False)

    plt.savefig(f'{save_path}/Itens_plot/{category}_itens_plot', dpi=500, bbox_inches='tight')