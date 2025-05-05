import pymysql

connection = pymysql.connect( host = 'localhost', user = 'root', \
    passwd = 'hallo1234', db = 'sakila')

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM sakila.actor LIMIT 5"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()


