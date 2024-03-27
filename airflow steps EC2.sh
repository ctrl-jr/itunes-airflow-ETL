#Steps for installing Airflow 2.8.3 on Ubuntu EC2 using Python 3.10
sudo apt-get update
sudo apt install python3-pip
pip install "apache-airflow==2.8.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.3/constraints-no-providers-3.10.txt"
PATH=$PATH:~/.local/bin

airflow db init
airflow users create --username admin --password admin --firstname John --lastname Doe --role Admin --email admin@domain.com
airflow webserver -D
airflow scheduler -D

