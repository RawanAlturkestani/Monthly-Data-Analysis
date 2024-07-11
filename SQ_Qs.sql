SELECT * FROM mrtsdb.csales;
SELECT Date, Sales, Buisness FROM mrtsdb.csales WHERE Date Between '2019-01-01' and '2019-07-01'; 
SELECT Sales, Buisness FROM mrtsdb.csales WHERE Buisness LIKE '%Book%'; 

SELECT DATE_FORMAT(Date, '%Y'),
CAST(sum(Sales) as unsigned) as Total_sales, Buisness
FROM CSales
WHERE Buisness = 'Retail and food services sales, total' and Month(Date) = '1' 
GROUP BY 1 ORDER BY DATE_FORMAT(Date, '%Y') ASC;

SELECT Month,
CAST(sum(Sales) as unsigned) as Total_sales, Buisness
FROM CSales
WHERE Buisness IN ('Sporting goods stores') 
GROUP BY 1;

SELECT DATE_FORMAT(Date, '%m-%Y'), CAST(sum(Sales) as unsigned) as Total_sales, Buisness FROM CSales
WHERE Buisness IN ('Women\'s clothing stores') Group By 1;

SELECT DATE_FORMAT(Date, '%m-%Y'), CAST(sum(Sales) as unsigned) as Total_sales, Buisness FROM CSales
WHERE Buisness IN ('Men\'s clothing stores') Group By 1;

SELECT DATE_FORMAT(Date,'%m-%Y') , Sum(Sales) OVER (PARTITION BY Buisness ORDER BY Sales) 
As Sales_total From CSales WHERE Buisness in ('Grocery stores') and DATE_FORMAT(Date,'%Y') in (2008,2009);
       
SELECT DATE_FORMAT(Date,'%m-%Y') , Sum(Sales) OVER (PARTITION BY Buisness ORDER BY Sales) 
As Sales_total From CSales WHERE Buisness in ('Clothing stores') and DATE_FORMAT(Date,'%Y') in (2008,2009);

SELECT DATE_FORMAT(Date, '%m-%Y'),
CAST(sum(Sales) as unsigned) as Total_sales, Buisness
FROM CSales
WHERE Buisness = 'Retail and food services sales, total' and Month(Date) = '1' and DATE_FORMAT(Date,'%Y') in (2020,2021)
GROUP BY 1 ORDER BY DATE_FORMAT(Date, '%Y') ASC;
