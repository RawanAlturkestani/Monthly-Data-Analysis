# Monthly-Data-Analysis


## Introduction

In this project I worked on Monthly Retail Trade Survey (MRTS) database produced by the US goverement at census.gov of a collection of a monthly sales details of multiple buisnesses from the year 1992 till the first two months of year 2021. I went through performing the full process of ETL, starting with data extraction, through transformartion with python and MySQl and loading the data into MySQL DB as well performing an studied analysis to drive some insights. You will find multiple graphs to visualize the anylsis in the most appropriate and clear way. 

## Content 
* Result: "Final_Project_Template" is a jupytor notebook that should help you get an overview on the work done.
* Cleaning: performed some cleaning on the MRTS dataset and then consolidation in one file after unpivoting the tables "mrts_t2"
   - "MRTS cleaning and consolidating sheets" -> for the cleaning work
   - "unpiviting _python" is to unpivot tables
* Analysis: performed some anylsis to look into time related trends by doing below
   - "SQL_Q" to query the data I am looking for using MySQL on the table built using MySQL
   - "percentage" to calculate the percantage change
   - "rolling_excercise" and "rolling_excercise_2" are both to perform a rolling time windows ustilizing MySQL functions
