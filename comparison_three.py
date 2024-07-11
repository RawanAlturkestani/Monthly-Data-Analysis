import mysql.connector 
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import dates as md
import numpy as np


cnx = mysql.connector.connect(
    user='root',
    password='PasWord',
    host='127.0.0.1',
    database='mrtsDB',
    auth_plugin='mysql_native_password'
)

cursor = cnx.cursor()


sql = ("""
SELECT DATE_FORMAT(Date,'%m-%Y') as '%Y',
CAST(sum(Sales) as unsigned) as Total_sales, Buisness, Year
FROM CSales
WHERE Buisness IN ('Book stores') 
GROUP BY 1  ORDER BY DATE_FORMAT(Date, '%Y') ASC""")
 

cursor.execute(sql)

Date=[]
sales=[]
#print all the first cell of all the rows
for row in cursor.fetchall():
    print(row)
    Date.append(row[0])
    sales.append(row[1])


sql1 = ("""
SELECT DATE_FORMAT(Date,'%m-%Y') as '%Y',
CAST(sum(Sales) as unsigned) as Total_sales, Buisness, Year
FROM CSales
WHERE Buisness IN ('Sporting goods stores') 
GROUP BY 1 ORDER BY DATE_FORMAT(Date, '%Y') ASC""")

cursor.execute(sql1)
Date1=[]
sales1=[]
#print all the first cell of all the rows
for row in cursor.fetchall():
    print(row)
    Date1.append(row[0])
    sales1.append(row[1])

sql2 = ("""
SELECT DATE_FORMAT(Date,'%m-%Y'),
CAST(sum(Sales) as unsigned) as Total_sales, Buisness, Year
FROM CSales
WHERE Buisness IN ('Hobby, toy, and game stores') 
GROUP BY 1  ORDER BY DATE_FORMAT(Date, '%Y') ASC""")

cursor.execute(sql2)
Date2=[]
sales2=[]

#print all the first cell of all the rows
for row in cursor.fetchall():
    print(row)
    Date2.append(row[0])
    sales2.append(row[1])

cursor.close()
cnx.close()




plt.ticklabel_format(axis='y', style='plain', scilimits=[0,100000000])
plt.gca().set(title='Three Buisnesses Comparison', xlabel='Months per Year', ylabel='Sales')
plt.plot(Date,sales)
plt.plot(Date1,sales1)
plt.plot(Date2,sales2)
plt.legend(['Book Stores', 'Sporting goods stores', 'Hobby, toy, and game stores'],loc=2)
plt.show()