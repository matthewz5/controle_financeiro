
## Projeto de Controle Financeiro Pessoal

O objetivo desse projeto é realizar o registro, análise e monitoramento da situação financeira pessoal, de modo que possibilite o controle de gastos e acompanhamento dos fluxos.

Para isso, o registro é divido em:

1. **ENTRADAS** Recebimento de salários e demais transferências;
2. **SAÍDAS** Gastos e pagamentos realizados, via cartão de crédito ou débito, como PIX.
3. **SALDO** diferença temporal entre as entradas e saídas registradas.

---


## Entradas 📈

Dados registrados:

1. **Data** - DD/MM/AAAA - Data do recebimento;
2. **Origem** - Texto - Insituição, empresa ou pessoa de origem;
3. **Tipo** - Texto - Categoria da entrada;
4. **Descricao** - Texto - Demais informações relevantes;
5. **Periodo** - MM/AAAA - Data referência da entrada;
6. **Valor** - R$ XX,XX - Valor da entrada.

---

## Saídas 📉

Dados registrados:

1. **Data** - DD/MM/AAAA - Data do gasto;
2. **Hora** - HH:MM - Horário do gasto;
3. **Categoria** - Texto - Categoria do gasto para a sua classificação;
4. **Frequencia** - Texto - Categoria da recorrência, como fixo para um parcelamento ou variado para qualquer outra compra;
5. **Tipo** - Texto - Categoria da fonte de saída, como crédito ou débito;
6. **Fonte** - Texto - Instituição de origem do pagamento, para crédito, ou PIX ou dinheiro;
7. **Local** - Texto - Local, loja, empresa etc. para registrar onde o gasto foi realizado;
8. **Item** - Texto - Produto ou serviço adquirido ou pago;
9.  **Descricao** - Texto - Demais informações relevantes;
10.  **Valor** - R$ XX,XX - Valor da unidade;
11.  **Quantidade** - Número - Quantidade de produto adquirida ou valor com desconto, por exemplo;
12.  **Total** - R$ XX,XX - Valor resultante de Valor x Quantidade.

---

## Saldo 💵

Resultante do cruzamento entre os dados de Entradas 📈 e Saídas 📉.

Para garantir a não entrada em dívidas, é necessário gastar menos do que se entra mensalmente, tendo um saldo positivo.

**Nota** Os valores gastos com Tipo de Crédito, em uma mês X, tendem a ser pagos de fato, via Débito pelo pagamento da fatura, no mês X+1. Nesse caso, a análise de balanço real é realizada por meio do acúmulo dos gastos entre as datas de fatura aberta, com o pagamento na data determinada.

---

## Dashboard 📊

Em desenvolvimento [...]

---

## Análise anual 🐍

Em melhoria [...]

---

## Tecnologias utilizadas 💻

<img alt="Python" src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" />

<img alt="SQL" src="https://img.shields.io/badge/-MySQL-3776AB?style=flat-square&logo=mysql&logoColor=white&labelColor=%23D71F00&color=%23D71F00" />

<img alt="Excel" src="https://img.shields.io/badge/-Excel-3776AB?style=flat-square&logo=microsoftexcel&labelColor=%23217346&color=%23217346" />


<img alt="PowerBI" src="https://img.shields.io/badge/-PowerBI-3776AB?style=flat-square&logo=powerbi&logoColor=%23000000&labelColor=%23F2C811&color=%23F2C811" />

---
