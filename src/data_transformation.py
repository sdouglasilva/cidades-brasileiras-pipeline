import logging
import random

logger = logging.getLogger(__name__)

def transformation_data(data):
  logger.info('Iniciando transformação dos dados.')
  rows = []
  for city in data:
    row = {
      "Nome": city["nome"],
      "UF": city["microrregiao"]["mesorregiao"]["UF"]["sigla"],
      "Região": city["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"],
      "População": random.randint(10_000, 800_00),
      "Área": random.randint(500, 10_000)
    }
    rows.append(row)
    return rows