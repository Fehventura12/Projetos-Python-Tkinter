import mysql.connector

banco = mysql.connector.connect( 
    host='Localhost',
    user='root',
    passwd='',
    database='usersdata'
)
cursor = banco.cursor()


print('Conectado ao Banco de Dados')