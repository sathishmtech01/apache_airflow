import datetime as dt
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
default_args = {
    'owner': 'me'
}
# Define DAG
with DAG('tutorial_test', default_args, start_date=dt.datetime(2022, 3, 16)) as dag:
    print_hello = BashOperator(task_id='print_hello',
        bash_command='echo hello')
    print_world = BashOperator(task_id='print_world',
        bash_command='echo world')
# Construct DAG
print_hello >> print_world
