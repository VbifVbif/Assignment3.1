from flask import Flask
from flask import render_template
from flask import request
import psycopg2
import requests

connection = psycopg2.connect(database="nftaggregator",
                              user="postgres",
                              # пароль, который указали при установке PostgreSQL
                              password="12345",
                              host="127.0.0.1",
                              port="5432")

cur = connection.cursor()



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form.get('address')
        # address = '4Jb9EzcUd6k1gC7GSH2iu6H7UcL2ez3NgvAF8n6a1QDs'

        url = 'https://solana-gateway.moralis.io/nft/mainnet/' + address + '/metadata'

        headers = {

            "accept": "application/json",
            "X-API-Key": "z1SWBbYXT9C5u4QlvAAqxr6q2WIgJWbClpY9o2ESQfdSKOA4VRxTm9WoZmH2Zrnj"

        }

        response = requests.get(url, headers=headers)

        # print(response.text)

        return "<h1>{}</h1>".format(response.text)

    return render_template('index.html')

if __name__ == '__main__':
   app.run()
