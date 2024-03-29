#Steps for installing and running Airflow 2.8.4 on Ubuntu EC2 using Python 3.10
sudo apt-get update
sudo apt install python3-pip
sudo apt install sqlite3
PATH=$PATH:~/.local/bin
pip install "apache-airflow==2.8.4" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.4/constraints-no-providers-3.10.txt"


airflow db init
airflow users create --username admin --password admin --firstname John --lastname Doe --role Admin --email admin@domain.com
airflow webserver -D
airflow scheduler -D

#View airflow PIDs
lsof -t tcp:8080