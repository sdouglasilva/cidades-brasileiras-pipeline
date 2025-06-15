from .api_client import get_all_city_data, logger
from utils.logger_config import setup_logging

def main():
  setup_logging()
  logger.info(f"Iniciando execução do app, para buscar dados de cidades")
  cities_page_1 = get_all_city_data(limit=5,offset=1)
  for index, city  in enumerate(cities_page_1):
    # print(f'Index:{index} \n - Cidade:{city}', type(city))
  
    for key, value in city.items():
      if 'nome' in key:
        print('Tem nome')
        print(key)
        print(value)















main()