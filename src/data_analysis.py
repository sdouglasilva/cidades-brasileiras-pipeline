import pandas as pd
from utils.logger_config import logger

def analize_city_data(rows):
    logger.info('Iniciando criação do Data Frame.')
    df = pd.DataFrame(rows)
    bins = [0,100_00,500_00,1000_00]
    labels = ["Pequena", "Média", "Grande"]
    logger.info("Categorizando o porte")
    df["Porte"] = pd.cut(df["População"], bins=bins, labels=labels)
    stats_by_region = df.groupby("Região").agg({
        "População":"mean"
    }).round(0).astype(int)
    logger.info("Dados analisados com sucesso!")
    return {"city_df":df,
            "stats_by_region": stats_by_region}