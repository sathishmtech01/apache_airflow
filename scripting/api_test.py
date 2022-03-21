import requests
url = "http://127.0.0.1:5000/save-dag"
data = {"dag_args":{"dag_id": "app_job1", "schedule_interval": "0 8 * * *", "default_args":"{'owner': 'airflow', 'depends_on_past': False, 'start_date': datetime(2020, 12, 18), 'email': ['vipin.chadha@gmail.com'], 'email_on_failure': False, 'email_on_retry': False, 'retries': 1, 'retry_delay': timedelta(minutes=5)}" },
        "task_sequence": [{"operator":"BashOperator","task_id":"task1","bash_command":"echo hello task1","dag":"dag"}],\
        "filename":"sample5.py",
        "filepath":"/home/csk/PycharmProjects/git/apache_airflow/dags/"}
req = requests.post(url,json=data)
print(req.text)
