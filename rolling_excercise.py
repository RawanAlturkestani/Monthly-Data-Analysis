import mysql.connector 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


cnx = mysql.connector.connect(
    user='root',
    password='PassWord',
    host='127.0.0.1',
    database='mrtsDB',
    auth_plugin='mysql_native_password'
)

cursor = cnx.cursor()
sql = ("""SELECT DATE_FORMAT(Date,'%m-%Y') , Sum(Sales) OVER (PARTITION BY Buisness ORDER BY Sales) 
       As Sales_total From CSales WHERE Buisness in ('Grocery stores') and DATE_FORMAT(Date,'%Y') in (2008,2009);
       """)

cursor.execute(sql)

date=[]
sales=[]
#print all the first cell of all the rows
for row in cursor.fetchall():
    date.append(row[0])
    sales.append(row[1])

dic={'Date':date, 'Sales':sales}

#create dataframe
df=pd.DataFrame(dic)
print(df)

#rolling_w = df['Sales'].rolling(2, min_periods=1).sum()
#print('RW:',rolling_w)
cursor.close()
cnx.close()

plt.style.use('_mpl-gallery') 
fig, ax = plt.subplots()

 
# Adjust the figure size as needed
#plt.plot(, df['Sales'])
ax.errorbar(x=df['Date'] , y=df['Sales'], yerr=df['Sales'], fmt='o', linewidth=2, capsize=4, color='green')
plt.ticklabel_format(axis='y', style='plain', scilimits=[0,100000000])
#sns.lineplot(data=rolling_w, label='Python')
plt.plot(df['Date'] , df['Sales'], color='maroon')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Time Series Plot with Rolling Window for Grocery stores-')
#plt.legend()
plt.grid(False)
plt.show()