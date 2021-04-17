import yaml
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects



def getCmcApiKey():
    path = "../Auth/conf.yaml"
    yaml_file = open(path)
    parse_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return parse_yaml["cmcApiKey"]

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': getCmcApiKey(),
}

def get_data():
    session = Session()
    session.headers.update(headers)
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

print(getCmcApiKey())