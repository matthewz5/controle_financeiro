import matplotlib.pyplot as plt

def plot_monthly_balance(df, col, save_path):

    df['Cumulative'] = df['Saldo'].cumsum()
    df['Start'] = df['Cumulative'].shift(1, fill_value=0)

    x_labels = [month.strftime('%b') for month in df['Data']]
    x_positions = range(len(df['Data']))

    plt.figure(figsize=(20, 10))

    for i, row in df.iterrows():
        color = 'green' if row['Saldo'] > 0 else 'red'
        plt.bar(i, row['Saldo'], bottom=row['Start'], color=color, edgecolor='black')
        plt.text(i, row['Start'] + row['Saldo'], f"{row['Saldo']:.2f}", ha='center', va='bottom', fontsize=10, color='black')

    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)

    plt.title('BALANÇO MENSAL', fontsize=16)
    plt.xlabel('Período', fontsize=14)
    plt.ylabel('Valores (R$)', fontsize=14)
    plt.xticks(ticks=x_positions, labels=x_labels, rotation=0)

    plt.gca().spines['top'].set_visible(True)
    plt.gca().spines['right'].set_visible(True)
    plt.gca().spines['left'].set_visible(True)
    plt.gca().spines['bottom'].set_visible(True)

    #plt.show(block=False)

    plt.savefig(f'{save_path}/balance_plot', dpi=500, bbox_inches='tight')
