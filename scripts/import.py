import json
import mysql.connector

try:
    cnx = mysql.connector.connect(user='', password='',
                                  host='127.0.0.1',
                                  database='prezola')

    with open('products.json') as json_file:
        data = json.load(json_file)
        for p in data:

            sql = 'INSERT INTO prezola.items(name, brand, price, in_stock_quantity) VALUES(%s, %s, %s, %s)'
            args = (p['name'], p['brand'], p['price'], p['in_stock_quantity'])

            cursor = cnx.cursor()

            cursor.execute(sql, args)

            cnx.commit()

except Error as e:
    print('Error writing', e)

finally:
    if (cnx.is_connected()):
        cnx.close()
        cursor.close()
