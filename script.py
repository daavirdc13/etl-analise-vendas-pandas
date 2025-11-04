import pandas as pd
from pathlib import Path

RAW_PATH = Path('data/raw')
PROCESSED_PATH = Path('data/processed')

def carregar_dados():
    df_clientes = pd.read_csv(RAW_PATH / 'clientes.csv')
    df_vendas = pd.read_csv(RAW_PATH / 'vendas.csv')
    return df_clientes, df_vendas

def transformar_dados(df_clientes, df_vendas):
    df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])
    df = pd.merge(df_clientes, df_vendas, on='id_cliente', how='left')
    return df

def salvar_dados(df):
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH / 'vendas_clientess_v2.csv', index=False)

if __name__ == "__main__":
    clientes, vendas = carregar_dados()
    df_final = transformar_dados(clientes, vendas)
    salvar_dados(df_final)
    print("✅ ETL concluído e salvo em data/processed/vendas_clientes.csv")
