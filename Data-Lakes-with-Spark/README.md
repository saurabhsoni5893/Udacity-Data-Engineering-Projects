# Data Lake with Apache Spark

## **Introduction**

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, The task is to build an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

## **Project Description**

Application of Spark and data lakes to build an ETL pipeline for a data lake hosted on S3. Will need to load data from S3, process the data into analytics tables using Spark, and load them back into S3. Then deploy this Spark process on a cluster using AWS.

## **Project Datasets**

Song Data Path     -->     s3://udacity-dend/song_data
Log Data Path      -->     s3://udacity-dend/log_data

#### **Song Dataset**

The first dataset is a subset of real data from the Million Song Dataset(https://labrosa.ee.columbia.edu/millionsong/). Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. 
For example:

song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

#### **Log Dataset**

The second dataset consists of log files in JSON format. The log files in the dataset with are partitioned by year and month.
For example:

log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json

And below is an example of what a single log file, 2018-11-13-events.json, looks like.

{"artist":"Pavement", "auth":"Logged In", "firstName":"Sylvie", "gender", "F", "itemInSession":0, "lastName":"Cruz", "length":99.16036, "level":"free", "location":"Klamath Falls, OR", "method":"PUT", "page":"NextSong", "registration":"1.541078e+12", "sessionId":345, "song":"Mercy:The Laundromat", "status":200, "ts":1541990258796, "userAgent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10_9_4...)", "userId":10}

## **Schema for Song Play Analysis**

A Star Schema would be required for optimized queries on song play queries

#### **Fact Table**

**songplays** - records in event data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

#### **Dimension Tables**

**users** - users in the app
user_id, first_name, last_name, gender, level

**songs** - songs in music database
song_id, title, artist_id, year, duration

**artists** - artists in music database
artist_id, name, location, lattitude, longitude

**time** - timestamps of records in songplays broken down into specific units
start_time, hour, day, week, month, year, weekday

## **Project Files**

Project include three files:

**1. etl.py** reads data from S3, processes that data using Spark, and writes them back to S3

**2. dl.cfg** contains AWS credentials

**3. README.md** provides discussion on process and decisions

## **Create Table Schema**

## **Build ETL Pipeline**

1. Implement the logic in etl.py to load data from S3 to EMR Cluster tables.
2. Implement the logic in etl.py to load data from EMR Cluster tables to S3 again.
3. Test by running etl.py and afterwards running the queries on jupyter notebook running on EMR cluster to compare your results with the expected results.
4. Delete EMR cluster when finished.

## **Final Instructions**

1. Import all the necessary libraries
2. Write the configuration of AWS Cluster, store the important parameter in some other file
3. Configuration of boto3 which is an AWS SDK for Python
4. Using the bucket, can check whether files log files and song data files are present
5. Create an IAM User Role, Assign appropriate permissions and create the EMR Cluster
6. Get the Value of Endpoint and Role for put into main configuration file
7. Authorize Security Access Group to Default TCP/IP Address
8. Launch database connectivity configuration
9. Go to Terminal write the command "python etl.py"
10. Should take around 4-10 minutes in total
11. Then go back to jupyter notebook to test everything is working fine
12. count all the records in the tables
13. Now can delete the cluster, roles and assigned permission