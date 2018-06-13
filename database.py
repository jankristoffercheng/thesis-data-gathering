import pymysql

class ConnectionFactory:
    def getConnectionThesis(self):
        return pymysql.connect(host='localhost', user='root', password='1234', db='thesis_data', cursorclass=pymysql.cursors.DictCursor, autocommit=True)

