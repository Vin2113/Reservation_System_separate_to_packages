import mysql.connector
connection = mysql.connector.connect(host='localhost',
                             user='root',
                             password='Vl1021996499.',
                            database = 'reservation_system'
                           )
my_cursor = connection.cursor()