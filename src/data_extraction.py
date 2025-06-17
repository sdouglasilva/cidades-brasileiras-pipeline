from .api_client import get_all_cities_data
import logging

logger = logging.getLogger(__name__)
def extract_all_city_data():
  logger.info('Iniciando a extração de dados das cidades brasileiras')
  all_cities = get_all_cities_data(limit=0, offset=100)

  if not all_cities:
    logger.warning('Nenhum dado foi extraído da API')
    return []
  
  logger.info(f'{len(all_cities)} - Cidades extraídas com sucesso')
  return all_cities
