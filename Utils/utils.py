import yaml
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os
#


def get_file_path(file_id):
    # 1 = conf.yaml
    # 2 = data.json
    elad = "C:\\Users\\1\PycharmProjects\Rater\\"
    david = "C:\\Users\DavidYafe\Desktop\MyCryptoAPI\\"
    yaml_path = "Auth\conf.yaml"
    json_path = "Files\Data.json"
    if file_id ==1:
        if "DavidYafe" in os.getcwd():
            path =  david + yaml_path
        else:
            path = elad + yaml_path
        return path
    elif file_id ==2:
        if "DavidYafe" in os.getcwd():
            path =  david + json_path
        else:
            path = elad + json_path
        return path





def get_creds():
    path = get_file_path(1)
    yaml_file = open(path)
    parse_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return [parse_yaml["url"], parse_yaml["parameters"], parse_yaml["headers"]]



def get_data():
    url = get_creds()[0]
    parameters = get_creds()[1]
    headers = get_creds()[2]
    session = Session()
    session.headers.update(headers)
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
      path = get_file_path(2)
      with open(path, 'w') as outfile:
          json.dump(data, outfile)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    return data



print(get_file_path(2))
