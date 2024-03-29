# ETL pipeline with Airflow - from iTunes to AWS S3
## Overview
This was a very simple project to learn airflow and storing files in a AWS S3 bucket. 
In this case the extracted data are movies from the iTunes search API, then we extract some fields and create a CSV then upload it an Amazon S3 bucket. Everything was run on a Ubuntu EC2.

## Architecture
![image](https://github.com/ctrl-jr/itunes-airflow-ETL/assets/36134747/b0ae1270-df1a-4b9a-875a-fc35541a0a35)


## Tools Used
### Dataset/source
-iTunes API

### Language
-Python

### AWS
-EC2  
-S3 bucket

## Project structure
**ETL.py** which contains the main function that does the extraction, transforming and upload of the CSV.  
**itunes_dag.py** contains the orchestration code that airflow uses to call the ETL function.
