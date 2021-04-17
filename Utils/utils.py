import yaml
import json

yaml_file = open("C:\\Users\DavidYafe\Desktop\MyCryptoAPI\Auth\conf.yaml")


parse_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)

def getCmcApiKey():
    return parse_yaml["cmcApiKey"]

