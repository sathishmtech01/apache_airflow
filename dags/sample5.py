
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
dag = DAG("app_job1",schedule_interval="0 8 * * *",default_args={'owner': 'airflow', 'depends_on_past': False, 'start_date': datetime(2020, 12, 18), 'email': ['vipin.chadha@gmail.com'], 'email_on_failure': False, 'email_on_retry': False, 'retries': 1, 'retry_delay': timedelta(minutes=5)},catchup=False)
task_sequence = [{'operator': 'BashOperator', 'task_id': 'task1', 'bash_command': 'echo hello task1', 'dag': 'dag'}] 

task_list=[]
# iterate
for i in range(0, len(task_sequence)):
    if task_sequence[i]["operator"] == "BashOperator":
        task_list.append(BashOperator(task_id=task_sequence[i]["task_id"],bash_command=task_sequence[i]["bash_command"],dag=dag))
        # Step 4b - Define the sequence of execution of tasks
        if i not in [0]:
            task_list[i-1] >> task_list[i]