from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

    
with DAG(dag_id='currency_update',
            start_date=datetime(2025, 1, 1),
            schedule_interval='*/10 8-16 * * *',
            catchup=False,
    ) as dag:
    
        update = BashOperator(
            task_id = "currency_update_1",
            bash_command = 'cd /opt/airflow/scripts/ && python currency_update.py'
            )
        