import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'zeyan012906'

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmapp")

print("All Done!")
