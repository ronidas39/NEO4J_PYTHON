from tracemalloc import start
from airflow import DAG
from datetime import datetime
from airflow.providers.neo4j.operators.neo4j import Neo4jOperator


default_args={"owner":"airflow"}

with DAG(dag_id="nep4j_workflow_tutorial",start_date=datetime(2022,2,14),schedule_interval="@daily",default_args=default_args)as dag:
    neo4j_operator_task=Neo4jOperator(
        neo4j_conn_id="neo4j_conn_id",
        task_id="neo4j_operator_task",
        sql='Create(m:Student{Name:"Rahul"})'
    )
    