import requests

# Rest method
url = "http://127.0.0.1:5000/save-dag"
data = {"dag_args":{"dag_id": "data_processing6", "schedule_interval": "0 0 * * *", "default_args":"{'owner': 'airflow'}" },
        "task_sequence": [{"operator":"BashOperator","task_id":"t1","bash_command":"echo hello task1"},{"operator":"BashOperator","task_id":"t2","bash_command":"echo hello task2"},{"operator":"BashOperator","task_id":"t3","bash_command":"echo hello task3"}],
        "filename":"data_processing6.py",
        "filepath":"/home/csk/PycharmProjects/git/apache_airflow/dags/"}
req = requests.post(url,json=data)
print(req.text)

