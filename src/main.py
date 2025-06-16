import logging
from utils.logger_config import setup_logging
from .data_extraction import extract_all_city_data
from .data_transformation import transformation_data
from .data_analysis import analize_city_data

def main():
  logger = logging.getLogger(__name__)
  setup_logging()
  logger.info(f"Iniciando execução do app, para buscar dados de cidades")
  # cities_page_1 = get_all_cities_data(limit=5,offset=1)
  cities_page = extract_all_city_data()
  processed_data = transformation_data(cities_page)
  analysis_data = analize_city_data(processed_data)
  print(analysis_data)

  
  # for index, city  in enumerate(cities_page):
  #   print(f'Index:{index} \n - Cidade:{city["nome"],city["microrregiao"]["mesorregiao"]["UF"]["regiao"]["nome"]}', type(city))
  
    # for key, value in city.items():
    #   if 'nome' in key:
    #     print(key)
    #     print(value)















main()