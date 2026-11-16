import requests
from airflow.sdk import task, dag
from pendulum import datetime

n8n_webhook_url = "http://172.18.96.1:5678/webhook/455362e0-a625-489d-b327-8f213fd451f1"

@dag(
dag_id = "n8n_trigger_dag",
start_date = datetime(2026,1,1, tz="UTC"),
schedule = None,
catchup = False
)
def trigger_n8n():
    @task
    def send_to_n8n():
        payload = {
        "source" : "airflow",
        "message" : "hey, it's airflow",
        "number" : 24
        }
        response = requests.post(n8n_webhook_url, json = payload, timeout = 5)
        response.raise_for_status()
        print("n8n status :", response.status_code)
        return response.json()
    
    send_to_n8n()
trigger_n8n()