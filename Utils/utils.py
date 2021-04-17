import yaml
import json

path = "../Auth/conf.yaml"

yaml_file = open(path)


parse_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)

def getCmcApiKey():
    return parse_yaml["cmcApiKey"]


print(getCmcApiKey())
