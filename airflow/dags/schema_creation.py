from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta 

dag_owner = 'admin'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
        }

with DAG(dag_id='schema_creation_1',
        default_args=default_args,
        description='schema_creation_1',
        start_date=datetime(),
        schedule_interval='',
        catchup=False,
        tags=['']
):

    start = EmptyOperator(task_id='start')

    creation = BashOperator(
        task_id = "schema_creation"
        bash_command = 'cd /opt/airflow/scripts/ && python schema.py'
    )

    end = EmptyOperator(task_id='end')

    start >> creation >> end 

