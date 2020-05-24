# Data Modeling with Cassandra

## **Introduction**
    
A startup called **Sparkify** wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. There is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app. My role is to create an Apache Cassandra database which can create queries on song play data to answer the questions.

## Project Overview

In this project, I would be applying Data Modeling with Apache Cassandra and complete an ETL pipeline using Python. I am provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

## **Datasets**

For this project, I'll be working with one dataset: event_data. The directory of CSV files partitioned by date. Here are examples of filepaths to two files in the dataset:
event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv

## **Project Template**

The project template includes one Jupyter Notebook file, in which:
•	I will process the event_datafile_new.csv dataset to create a denormalized dataset
•	I will model the data tables keeping in mind the queries you need to run
•	I have been provided queries that you will need to model your data tables for
•	I will load the data into tables you create in Apache Cassandra and run your queries

## **Project Steps**

Below are steps I followed to complete each component of this project.

**Modelling NoSQL Database or Apache Cassandra Database**
    
1.	Design tables to answer the queries outlined in the project template
2.	Write Apache Cassandra CREATE KEYSPACE and SET KEYSPACE statements
3.	Develop CREATE statement for each of the tables to address each question
4.	Load the data with INSERT statement for each of the tables
5.	Include IF NOT EXISTS clauses in CREATE statements to create tables only if the tables do not already exist. Included DROP TABLE statement for each table, this way I can run drop and create tables whenever I want to reset database and test ETL pipeline
6.	Test by running the proper select statements with the correct WHERE clause

** Build ETL Pipeline**
1.	Implement the logic in section Part I of the notebook template to iterate through each event file in event_data to process and create a new CSV file in Python
2.	Make necessary edits to Part II of the notebook template to include Apache Cassandra CREATE and INSERT three statements to load processed records into relevant tables in data model
3.	Test by running three SELECT statements after running the queries on database
4.	Finally, drop the tables and shutdown the cluster

## **Files**

**Project_1B_Project_Template.ipynb** This was template file provided to fill in the details and write the python script

**Project_1B.ipynb** This is the final file provided in which all the queries have been written with importing the files, generating a new csv file and loading all csv files into one. All verifying the results whether all tables had been loaded accordingly as per requirement

**Event_datafile_new.csv** This is the final combination of all the files which are in the folder event_data

**Event_Data Folder** Each event file is present separately, so all the files would be combined into one into event_datafile_new.csv

