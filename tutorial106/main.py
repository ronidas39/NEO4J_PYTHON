from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()
uri=os.getenv("uri")
user=os.getenv("user")
pwd=os.getenv("pwd")

class nodemodel(BaseModel):
    name:str
    emp_id:int

def connection():
    driver=GraphDatabase.driver(uri=uri,auth=(user,pwd))
    return driver

app=FastAPI()
@app.post("/create")
def createnode(node:nodemodel):
    driver_neo4j=connection()
    session=driver_neo4j.session()
    q1="""
    create(n:employee{name:$name,emp_id:$emp_id}) return n.name as name
    """
    x={"name":node.name,"emp_id":node.emp_id}
    results=session.run(q1,x)
    data=[{"Name":row["name"]}for row in results][0]["Name"]
    return {"response":"node created with employee name as: "+data}





