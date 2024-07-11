from sqlalchemy import text
from sqlalchemy import create_engine
import mysql.connector 
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import dates as md


cnx = mysql.connector.connect(
    user='root',
    password='Ma345690xa.@',
    host='127.0.0.1',
    database='mrtsDB',
    auth_plugin='mysql_native_password'
)

#engine = create_engine("mysql+mysqlconnector://root:Ma345690xa.@@127.0.0.1/mrtsdb")

# Load DataFrame from SQL database
#data = pd.read_sql("""SELECT DATE_FORMAT(Date, '%m-%Y'), CAST(sum(Sales) as unsigned) as Total_sales, Buisness FROM CSales WHERE Buisness IN ('Women''s clothing stores') Group By 1""", con=engine ) 

cursor = cnx.cursor()


sql = ("""SELECT DATE_FORMAT(Date, '%Y'), CAST(sum(Sales) as unsigned) as Total_sales, Buisness FROM CSales WHERE Buisness IN ('Women''s clothing stores') Group By 1 ORDER BY DATE_FORMAT(Date, '%Y') ASC""")
 

cursor.execute(sql)

Date=[]
sales=[]
#print all the first cell of all the rows
for row in cursor.fetchall():
    Date.append(row[0])
    sales.append(row[1])

#create dictionary
dic={'Date':Date, 'Sales':sales}

#create dataframe
women_df=pd.DataFrame(dic)
#drop nulls
women_df = women_df.dropna(axis=0)
#calculate percantage change
women_df['change'] = women_df['Sales'].pct_change()*100

print('Women''s clothing stores\n', women_df)


sql1 = ("""SELECT DATE_FORMAT(Date, '%Y'), CAST(sum(Sales) as unsigned) as Total_sales, Buisness FROM CSales WHERE Buisness IN ('Men''s clothing stores') Group By 1 ORDER BY DATE_FORMAT(Date, '%Y') ASC""")
 

cursor.execute(sql1)

Date1=[]
sales1=[]
#print all the first cell of all the rows
for row in cursor.fetchall():
    #print(row)
    Date1.append(row[0])
    sales1.append(row[1])

#create dictionary 
dic1={'Date':Date1, 'Sales':sales1}

#create dataframe
men_df=pd.DataFrame(dic1)
#drop nulls
men_df = men_df.dropna(axis=0)
#calculate percantage change
men_df['change'] = men_df['Sales'].pct_change()*100

print('men''s clothing stores\n', men_df)
#calculate percantage of change



cursor.close()
cnx.close()

val = men_df['change']
plt.gca().set(title='Women''s vs Men''s clothing stores', xlabel='Years', ylabel='Change')
plt.plot(women_df['Date'] , women_df['change'], '-x')
plt.plot(men_df['Date'] , men_df['change'],'-o')
plt.legend(['Women''s clothing stores','Men''s clothing stores'], loc=2)
plt.show()