import matplotlib.pyplot as plt
import pandas as pd
from utils.logger_config import logging


def generate_reports(data):
  df = data["city_df"]
  stats = data["stats_by_region"]

  try:
    df.to_csv("data/reports/cidades_brasil.csv", index=False)
    stats.to_csv("data/reports/stats_por_regiao.csv")
    
    stats.plot(kind="bar",title="Média de População por Região")
    plt.tight_layout()
    plt.savefig("data/reports/populacao_por_regiao.png")
    logging.info("Relatórios gerados com sucesso.")
  except Exception as e:
    logging.error(f"Erro ao gerar relatórios{e}")
