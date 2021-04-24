import yaml
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import os
import mysql.connector
#


# This function will create the relative path for the server execute it
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
    elif file_id == 2:
        if "DavidYafe" in os.getcwd():
            path =  david + json_path
        else:
            path = elad + json_path
        return path

# Get All relevant credentials from the YAML file


def get_creds():
    path = get_file_path(1)
    yaml_file = open(path)
    parse_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return [parse_yaml["url"], parse_yaml["parameters"], parse_yaml["headers"],parse_yaml["dbServer"],
            parse_yaml["dbUser"],parse_yaml["dbPass"],parse_yaml["db"]]



def get_data():
    url = get_creds()[0]
    parameters = get_creds()[1]
    headers = get_creds()[2]
    session = Session()
    session.headers.update(headers)
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      path = get_file_path(2)
      with open(path, 'w') as outfile:
          json.dump(data, outfile)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    return data


def execute_sql(sql1, sql2):
    cnx = mysql.connector.connect(user=get_creds()[4], password=get_creds()[5], host=get_creds()[3], database=get_creds()[6])
    cursor = cnx.cursor()
    try:
        if sql2 is not None:
            cursor.execute(sql1, sql2)
            print("Succesfully executed both queries : \n" + sql1 + '\n' + sql2)
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            cursor.execute(sql1)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("Succesfully executed 1 query" + sql1)
    except Exception as e:
        print(e)





def insert_data_to_sql():
    data_array = get_data()["data"]
    row_number = 0
    sql = """INSERT INTO Rater.Mrr_Crypto_stats 
        (Coin_Id, Coin_Name, Coin_Symbol, Coin_age, Cmc_Rank, Usd_Price, Vol_24h, Percent_Change_1h, Percent_Change_24h,
         Percent_Change_07d, Percent_Change_30d, Percent_Change_60d, Percent_Change_90d, Market_Cap) VALUES\n """
    for i in data_array:
        sql += "(" + str(i["id"]) + "," + "'" + i["name"]+"'" + "," + "'"+ i["symbol"]+"'" + "," + "'" + \
        str(i["date_added"][:10]) +"'" + "," + str(i["cmc_rank"]) + "," + str(i["quote"]["USD"]["price"])+ \
        "," + str(int(i["quote"]["USD"]["volume_24h"])) + "," + str(i["quote"]["USD"]["percent_change_1h"]) + "," + \
        str(i["quote"]["USD"]["percent_change_24h"]) + "," + str(i["quote"]["USD"]["percent_change_7d"]) + "," + \
        str(i["quote"]["USD"]["percent_change_30d"]) + "," + str(i["quote"]["USD"]["percent_change_60d"]) + "," + \
        str(i["quote"]["USD"]["percent_change_90d"]) + "," + str(i["quote"]["USD"]["market_cap"])+")"
        row_number += 1
        if len(data_array) != row_number:
            sql += ',' + '\n'
        truncate = "Truncate table Mrr_Crypto_stats"
        execute_sql(sql1=truncate, sql2=sql)
