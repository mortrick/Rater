import yaml
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os
#

def get_yaml_path():
    if "DavidYafe" in os.getcwd():
        path =  "C:\\Users\DavidYafe\Desktop\MyCryptoAPI\Auth\conf.yaml"
    else:
        path = "C:\\Users\\1\PycharmProjects\Rater\Auth\conf.yaml"
    return path





def get_creds():
    path = get_yaml_path()
    yaml_file = open(path)
    parse_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return [parse_yaml["url"], parse_yaml["parameters"], parse_yaml["headers"]]



# def get_data():
#     session = Session()
#     session.headers.update(headers)
#     try:
#       response = session.get(url, params=parameters)
#       data = json.loads(response.text)
#       print(data)
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#       print(e)



print(get_creds())