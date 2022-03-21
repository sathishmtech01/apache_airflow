import os
import urllib.request
import json
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/save-dag', methods=['POST'])
def save_dag():
	record = json.loads(request.data)
	# Input arguments
	# dag_initialize_args = {'dag_id': 'app_job1', 'schedule_interval': '0 8 * * *',
	# 					   'default_args': "{'owner': 'airflow', 'depends_on_past': False, 'start_date': datetime(2020, 12, 18), 'email': ['vipin.chadha@gmail.com'], 'email_on_failure': False, 'email_on_retry': False, 'retries': 1, 'retry_delay': timedelta(minutes=5)}"}
	# task_sequence = [{'operator': 'BashOperator', 'task_id': 'task1', 'bash_command': 'echo hello task1', 'dag': 'dag'}]
	# file_name = "sample_3.py"
	dag_initialize_args = record["dag_args"]
	task_sequence =  record["task_sequence"]
	file_name = record["filepath"]+record["filename"]
	f = open(file_name, "w")
	# Initialize libraries
	f.write('\nfrom airflow import DAG')
	f.write('\nfrom airflow.operators.bash_operator import BashOperator')
	f.write('\nfrom airflow.operators.dummy_operator import DummyOperator')
	f.write('\nfrom datetime import datetime, timedelta')
	f.write('\nfrom airflow.utils.dates import days_ago')
	f.write('\ndag = DAG("{}",schedule_interval="{}",start_date=days_ago(2),default_args={},catchup={})'.format(dag_initialize_args['dag_id'],
																					   dag_initialize_args[
																						   "schedule_interval"],
																					   dag_initialize_args[
																						   "default_args"], "False"))
	f.write('\ntask_sequence = {} '.format(task_sequence))
	f.write('\n')
	f.write('\ntask_list=[]')
	f.write('\n# iterate')
	f.write('\nfor i in range(0, len(task_sequence)):')
	f.write('\n    if task_sequence[i]["operator"] == "BashOperator":')
	f.write('\n        task_list.append(BashOperator(task_id=task_sequence[i]["task_id"],bash_command=task_sequence[i]["bash_command"],dag=dag))')
	f.write('\n        # Step 4b - Define the sequence of execution of tasks')
	f.write('\n        if i not in [0]:')
	f.write('\n            task_list[i-1] >> task_list[i]')
	f.close()

	return record

if __name__ == "__main__":
    app.run()