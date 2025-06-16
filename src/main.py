import logging
from .api_client import get_all_cities_data
from utils.logger_config import setup_logging
from .data_extraction import extract_all_city_data

def main():
  logger = logging.getLogger(__name__)
  setup_logging()
  logger.info(f"Iniciando execução do app, para buscar dados de cidades")
  # cities_page_1 = get_all_cities_data(limit=5,offset=1)
  cities_page = extract_all_city_data()
  # for index, city  in enumerate(cities_page_1):
  #   # print(f'Index:{index} \n - Cidade:{city}', type(city))
  
  #   for key, value in city.items():
  #     if 'nome' in key:
  #       print('Tem nome')
  #       print(key)
  #       print(value)















main()