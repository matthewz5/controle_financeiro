import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_in_out_acc(df, save_path):

    plt.figure(figsize=(20, 5))

    plt.plot(df['Data'], 
            df['Valor_entrada_acc'],
            linestyle='--',
            linewidth=2,
            color='green', 
            label='Entradas')

    plt.plot(df['Data'], 
            df['Valor_saida_acc'],
            linestyle='-', 
            linewidth=2,
            color='red', 
            label='Saidas')

    plt.title('ENTRADAS E SAÍDAS ACUMULADAS')
    plt.xlabel('Período')
    plt.ylabel('Valores (R$)')
    plt.grid(False)

    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(True)
    plt.gca().spines['bottom'].set_visible(True)

    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=10, title="")

    # plt.show(block=False)

    plt.savefig(f'{save_path}/in_out_acc_plot', dpi=500, bbox_inches='tight')