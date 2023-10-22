# Projeto de Controle Financeiro

O objetivo desse projeto é realizar o registro, análise e monitoramento da situação financeira pessoal anual.

O projeto é subdivido em duas frentes:

1. **ENTRADAS** - Registro de pagamentos e transferências recebidas;
2. **SAÍDAS**  - Registro de todos os gastos e pagamentos realizados, sejam em crédito (cartão crédito) ou débito (cartão de débito,  dinheiro ou PIX).

Cada frente fora desenvolvida e melhorada separadamente, para que ao final fosse possível fazer uma análise do **SALDO**, ou seja, a diferença entre as ENTRADAS e SAÍDAS registradas.

---

# ENTRADAS 📈

Tecnologias utilizadas: **Python**; **SQL**.

O objetivo é registrar todas as entradas de dinheiro, seja por meio de PIX de transferências do dia a dia, salários ou auxílios.

Aglutinando todos eles de uma forma coerente para possibilitar a análise em conjunta.

Para tal, teremos 2 frentes de ENTRADAS:

1. [Extratos mensais do NuBank](https://github.com/matthewz5/controle_financeiro/blob/main/read_extrato_nubank_to_SQL.ipynb) (script em Py desenvolvido com base no modelo de extrato deles);
2. Salário e benefícios;
3. Demais entradas (renda extra, rendimentos, etc.)

Todas as entradas são armazenas em um banco de dados em MySQL, cujo [*schema* está disponível aqui](https://github.com/matthewz5/controle_financeiro/blob/main/script_banco_dados_entrada.sql).

---

# SAÍDAS 📉

Tecnologias utilizadas: **Excel**; **PowerBI**; **Python**. 

A lógica do registro das informações de saídas é a seguinte:

1. **Data** - Data da saída - formato DD/MM/AAAA;
2. **Hora** - Hora da saída - formato HH:MM:00;
3. **Categoria** - Categoria da saída, uma forma de classificação primária dos gastos e pagamentos:
    
    [Alimentacao; Aluguel; Assinatura; Carro; Cartao de Credito; Contas; Educacao; Externos; Lazer; Mercado; Namoro; Saude; Tecnologia; Trabalho; Transporte; Variados]
    
4. **Tipo_de_gasto** - Tipo da saída, uma segunda forma de classificação primária dos gastos e pagamentos, mais focada no tipo de ocorrência da operação em si:
    
    [Fixo; Variavel]
    
5. **Fonte** - Fonte dos valores da saída,  uma terceira forma de classificação primária dos gastos e pagamentos, mais focada na origem dos valores em si:
    
    [Credito; Debito]
    
6. **Sub_fonte** - Sub fonte dos valores da saída, uma classificação secundária da terceira forma (Fonte), mais focada na instituição bancária ou forma de pagamento utilizada:
    
    [Banco do Brasil; Caju; Dinheiro; NuBank; PIX; Vale Refeição]
    
7. **Local** - Local, loja, lugar ou etc. para registrar de forma primária onde o gasto ou pagamento foi realizado;
8. **Item** - Descrição simplificada do item do gasto ou pagamento, de forma a identificar primariamente o que foi comprado ou pago;
9. **Descricao_item** - Registro de informações, extensas ou não, sobre o item comprado ou pago, de modo a fornecer detalhes sobre a marca/fabricante; descrição; especiações; etc.
10.  **Valor_unitario** - Informe do valor da unidade, seja uma parte (Kg) ou um todo;
11.  **Quantidade** - Informe da quantidade de produto adquirida, podendo informar também valores de desconto (0,XX);
12.  **Valor_total** - Resultado automático da multiplicação de **Valor_unitario** por **Quantidade**.

Dentre as 12 informações de saídas, há os seguintes agrupamentos:

Automático - Informações preenchidas automaticamente pela Macro do Excel desenvolvida;

Lista Suspensa - Informações pré-definidas, como mostrado anteriormente;

Descritivo - Informações adicionadas manualmente, apenas com restrição de formato e sem pontuações específicas do Português BR.

<img src="images\Entrada_dados.png" width="800">

A planilha com a macro pode ser baixado [clicando aqui](https://github.com/matthewz5/controle_financeiro/blob/main/planilha_macro_dados_entrada.xlsm).