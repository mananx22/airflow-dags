from airflow.models import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
default_args = {}
with DAG('manan', schedule_interval='@daily',
         start_date=datetime(2020, 1, 1), catchup=False) as dag:
    one = BashOperator(task_id='print_date', bash_command='date')
    two = BashOperator(task_id='sleep', depends_on_past=False,
                       bash_command='sleep 5', retries=3)