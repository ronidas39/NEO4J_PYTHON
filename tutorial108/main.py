from fastapi import FastAPI
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()
uri=os.getenv("uri")
user=os.getenv("user")
pwd=os.getenv("pwd")

def connection():
    driver=GraphDatabase.driver(uri=uri,auth=(user,pwd))
    return driver


app=FastAPI()
@app.delete("/delete/{emp_id}")
def delete(emp_id:int):
    driver_neo4j=connection()
    session=driver_neo4j.session()
    q1="""
    match(n:employee{emp_id:$emp_id}) delete n
    """
    x={"emp_id":emp_id}
    results=session.run(q1,x)
    response=results.consume().counters
    deleted_nodes=response.nodes_deleted
    if(deleted_nodes>0):
        return {"Response":response}
    else:
        return {"Response":"Your Entered EMP_ID Is Missing In The Graph"}



