import psycopg2

# Подключение к существующей базе данных
connection = psycopg2.connect(database="nftaggregator",
                              user="postgres",
                              # пароль, который указали при установке PostgreSQL
                              password="12345",
                              host="127.0.0.1",
                              port="5432")

cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS nft_test (name text, count integer)")

connection.commit()
