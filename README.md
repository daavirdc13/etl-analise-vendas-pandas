🎯 Processo de Engenharia de Dados (ETL)

O projeto segue as três fases clássicas de um pipeline de dados:

1. Extract (Extração)
Leitura dos DataFrames clientes.csv e vendas.csv.

2. Transform (Transformação)
Inspeção de Qualidade: Verificação de tipos de dados (.info()) e tratamento de formatos.

Ação Principal: Conversão da coluna data_venda (string) para o tipo datetime.

Enriquecimento de Dados: Junção (pd.merge()) da tabela de Vendas com a de Clientes, utilizando id_cliente como chave. (Simulação de um JOIN de SQL).

Agregação de Negócio: Cálculo das seguintes métricas:

Receita Total por Estado.

Receita Total por Produto.

3. Load (Carregamento)
O DataFrame final, contendo as métricas de desempenho, é salvo em um novo arquivo CSV (desempenho_regional.csv), concluindo o ciclo ETL.