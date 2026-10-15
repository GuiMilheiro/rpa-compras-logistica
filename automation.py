"""
Automação RPA: Atualização de Custo de Insumos e Câmbio para Compras/Logística
Requisitos: Consumo de API RESTful pública (AwesomeAPI), processamento e exportação em Excel.
"""

import sys
import logging
from datetime import datetime
from pathlib import Path
import pandas as pd
import requests

# Configuração de logging estruturado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)

DATA_DIR = Path("data")
OUTPUT_FILE = DATA_DIR / "relatorio_compras_atualizado.xlsx"
EXCHANGE_API_URL = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"


def obter_cotacoes() -> dict:
    """Consome a API pública da AwesomeAPI para obter a taxa de câmbio de USD e EUR."""
    logging.info("Consultando cotações de câmbio via API RESTful...")
    try:
        response = requests.get(EXCHANGE_API_URL, timeout=10)
        response.raise_for_status()
        dados = response.json()

        usd_rate = float(dados["USDBRL"]["bid"])
        eur_rate = float(dados["EURBRL"]["bid"])

        logging.info("Cotações obtidas: USD/BRL = R$ %.4f | EUR/BRL = R$ %.4f", usd_rate, eur_rate)
        return {"USD": usd_rate, "EUR": eur_rate, "BRL": 1.0}
    except requests.RequestException as exc:
        logging.error("Falha ao comunicar com a API de câmbio: %s", exc)
        sys.exit(1)


def carregar_pedidos_base() -> pd.DataFrame:
    """Simula ou lê o lote de solicitações de compras de insumos para produção/logística."""
    logging.info("Carregando base de ordens de compra pendentes...")
    itens = [
        {"id_pedido": "PED-101", "insumo": "Controlador Microchip", "moeda": "USD", "preco_original": 14.50, "qtd": 500},
        {"id_pedido": "PED-102", "insumo": "Painel LCD TFT", "moeda": "USD", "preco_original": 28.00, "qtd": 250},
        {"id_pedido": "PED-103", "insumo": "Sensores Industriais", "moeda": "EUR", "preco_original": 42.00, "qtd": 100},
        {"id_pedido": "PED-104", "insumo": "Embalagens Reforçadas", "moeda": "BRL", "preco_original": 5.80, "qtd": 1200},
        {"id_pedido": "PED-105", "insumo": "Placas de Circuito Impresso", "moeda": "USD", "preco_original": 9.20, "qtd": 800},
    ]
    return pd.DataFrame(itens)


def processar_precificacao(df: pd.DataFrame, cotacoes: dict) -> pd.DataFrame:
    """Calcula taxas de conversão, custos unitários convertidos e totais em BRL."""
    logging.info("Executando regras de negócio e cálculo de conversão...")
    
    df["taxa_cambio"] = df["moeda"].map(cotacoes)
    df["preco_unitario_brl"] = (df["preco_original"] * df["taxa_cambio"]).round(2)
    df["valor_total_brl"] = (df["preco_unitario_brl"] * df["qtd"]).round(2)
    
    # Aplica regra de conformidade: valores acima de R$ 30.000 requerem validação gerencial
    df["requer_aprovacao_diretoria"] = df["valor_total_brl"].apply(
        lambda x: "SIM" if x >= 30000.0 else "NÃO"
    )
    df["data_processamento"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df


def exportar_relatorio(df: pd.DataFrame) -> None:
    """Exporta o resultado processado para uma planilha Excel formatada."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    logging.info("Salvando relatório consolidado em: %s", OUTPUT_FILE)
    
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Resumo_Compras", index=False)
        
    logging.info("Processo concluído com sucesso. %d registros exportados.", len(df))


def main():
    logging.info("=== Iniciando Rotina RPA de Compras e Câmbio ===")
    cotacoes = obter_cotacoes()
    df_pedidos = carregar_pedidos_base()
    df_processado = processar_precificacao(df_pedidos, cotacoes)
    exportar_relatorio(df_processado)
    logging.info("=== Execução Finalizada ===")


if __name__ == "__main__":
    main()