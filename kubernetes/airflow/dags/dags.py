from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import random
from FranceTravailDataExtractor2 import *
#from Final_model import *


with DAG(
    dag_id='Extract_and_load_data',
    schedule_interval=None,
    start_date=days_ago(0)
) as my_dag:

    load_and_extract = PythonOperator(
        task_id='python_task',
        python_callable=Extract_and_load_data
    )

    load_and_extract

""" with DAG(
    dag_id='train_model',
    schedule_interval=None,
    start_date=days_ago(0)
) as my_dag:

    train_model = PythonOperator(
        task_id='python_task',
        python_callable=update_model
    )
    train_model """

