from tracemalloc import start
from airflow import DAG
from datetime import datetime
from airflow.providers.neo4j.hooks.neo4j import Neo4jHook
from airflow.operators.python_operator import PythonOperator
from h11 import Data


default_args={"owner":"airflow"}

def runhook():
    neo4j_hook=Neo4jHook(conn_id="neo4j_conn_id")
    Data=neo4j_hook.run("Match(n) return n")
    print(Data)

with DAG(dag_id="neo4j_workflow_tutorial_hook",start_date=datetime(2022,2,14),schedule_interval="@daily",default_args=default_args)as dag:
    runhook=PythonOperator(
        task_id="runhook",
        python_callable=runhook
    )
   