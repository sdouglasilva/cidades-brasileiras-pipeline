import requests
import logging
from utils.constants import BASE_URL


logger = logging.getLogger(__name__)

def get_all_city_data(limit=10, offset=0):
        #tratamento da url para definir um limite de cidades por requisição - 
        request_url = f'{BASE_URL}?limit={limit}&offset={offset}'
        logger.info(f'Requisitando lista de cidades{request_url}')
        try:
          response =  requests.get(request_url, timeout=10)
          response.raise_for_status()
          all_cities_data = response.json()
          logger.info(f'Dados brutos recebidos com sucesso. Total de itens {len(all_cities_data)}')
          #Paginação manual
          start_index = limit
          end_index = offset + limit
          paginated_cities = all_cities_data[start_index:end_index]
          logger.info(f'Retornando. {len(paginated_cities)} - \n Municípios para limit={limit}, offset = {offset}')
          return paginated_cities
          #Implementando Erro HTTP
        except requests.HTTPError as http_err:
          logger.error(f'Erro HTTP:{http_err.response.status_code}') - {http_err}
          #Implementando erro de Conexão
        except requests.ConnectionError:
            logger.error(f'Erro de conexão ao buscar cidades')
          #Implementando erro de TimeOut
        except requests.ConnectTimeout:
            logger.error(f'Erro de tempo excedido na requisição')
          #Implementando erro inesperado
        except requests.RequestException as e:
            logger.error(f'Erro inesperado na requisição da lista e de cidades{e}')
        return []
            