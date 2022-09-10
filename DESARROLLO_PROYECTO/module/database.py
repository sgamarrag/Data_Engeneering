import pymysql
import mysql.connector

class Database:
    def connect(self):
        return mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="sgamarrag",
            database="sgamarrag",
            charset="latin1",
            auth_plugin='mysql_native_password')
    
    def readPreguta1(self,nombre_dep):
        con = self.connect() #mydb
        #cursor = con.cursor()
        cursor = con.cursor(pymysql.cursors.DictCursor)
        print(nombre_dep)
        try:
            cursor.execute(f"SELECT * FROM income_department where department_name = {nombre_dep}")
            return cursor.fetchall()
        except Exception as e:
            return ()
        finally:
            con.close            

    def readPreguta2(self):
        con = self.connect() #mydb
        cursor = con.cursor()
        #cursor = con.cursor(pymysql.cursors.DictCursor)
        print(id)
        try:
            cursor.execute("SELECT * FROM category_total")
            return cursor.fetchall()
        except Exception as e:
            return ()
        finally:
            con.close

    def readPreguta3(self):
        con = self.connect() #mydb
        cursor = con.cursor()
        #cursor = con.cursor(pymysql.cursors.DictCursor)
        print(id)
        try:
            cursor.execute("SELECT * FROM buy_customer")
            return cursor.fetchall()
        except Exception as e:
            return ()
        finally:
            con.close
            
    def readPreguta4(self,id):
        con = self.connect() #mydb
        cursor = con.cursor()
        #cursor = con.cursor(pymysql.cursors.DictCursor)
        print(id)
        try:
            cursor.execute("SELECT * FROM mount_customer WHERE customer_id = {id}")
            return cursor.fetchall()
        except Exception as e:
            return ()
        finally:
            con.close            