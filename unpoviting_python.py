import pandas as pd 
import mysql.connector 

mrts = pd.read_csv('C:/Users/Rawan/Desktop/MITCN/M8/mrts_t2.csv', index_col = False, delimiter = ',')

cnx = mysql.connector.connect(
        user='root',
        password= 'PassWord',
        host= '127.0.0.1',
        database = 'mrtsDB',
        auth_plugin='mysql_native_password')


#create cursor 
cursor = cnx.cursor()

#create table
cursor.execute('Use mrtsDB;')
record = cursor.fetchone()
print("You're connected to database: ", record)
cursor.execute('DROP TABLE IF EXISTS CSales;')
cursor.execute('SET GLOBAL sql_mode = "";')

sql =("""
      CREATE TABLE CSales (BuisnessID int(10) null, Code VARCHAR(200) NULL, Buisness VARCHAR(300) not NULL,
      Date DATE null, Sales varchar(200) null, Month int(25) null, Year int(25) null
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
      """)
cursor.execute(sql)

#insert values in rows 
for i,row in mrts.iterrows():
    insrt = """INSERT INTO CSales VALUES (%s,%s,%s,%s,%s,%s,%s) """
    cursor.execute(insrt, tuple(row))
    print("Record inserted")
    cnx.commit()

              
cursor.close()
cnx.close()