from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime


with DAG(
        'finance_dag44',
        description='schema_creation_1',
        start_date=datetime(2024, 12, 31),
        schedule_interval=None,
        catchup=False,

) as dag33:

    creation = BashOperator(
        task_id = "schema_creation",
        bash_command = 'cd /opt/airflow/scripts/ && python schema.py'
    )





