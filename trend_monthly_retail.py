import mysql.connector 
import matplotlib.pyplot as plt
import pandas as pd


cnx = mysql.connector.connect(
    user='root',
    password='PassWord',
    host='127.0.0.1',
    database='mrtsDB',
    auth_plugin='mysql_native_password'
)

cursor = cnx.cursor()
sql = ("""
SELECT DATE_FORMAT(Date, '%m-%y'),
CAST(sum(Sales) as unsigned) as Total_sales, Buisness
FROM CSales
WHERE Buisness = 'Retail and food services sales, total' 
GROUP BY 1 ORDER BY Date ASC
       """)

cursor.execute(sql)

month=[]
sales=[]
#print all the first cell of all the rows
for row in cursor.fetchall():
    print(row)
    month.append(row[0])
    sales.append(row[1])

cursor.close()
cnx.close()



plt.ticklabel_format(axis='y', style='plain', scilimits=[0,100000000])
plt.ticklabel_format(axis='x', style='plain', scilimits=[0,2021])
plt.gca().set(title='Retail and food services sales, total from 1992 to 2021.', xlabel='timeline', ylabel='Sales')
plt.plot(month,sales)
plt.show()