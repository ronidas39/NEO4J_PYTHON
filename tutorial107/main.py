
from fastapi import FastAPI
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
uri=os.getenv("uri")
user=os.getenv("user")
pwd=os.getenv("pwd")

def connection():
    driver=GraphDatabase.driver(uri=uri,auth=(user,pwd))
    return driver

class nodemodel(BaseModel):
    name:str
    emp_id:int

app=FastAPI()
@app.put("/update")
def update(node:nodemodel,inputname):
    driver_neo4j=connection()
    session=driver_neo4j.session()
    q1="""
    match(n:employee{name:$inputname}) set n.name=$name ,n.emp_id=$emp_id return n.name as name
    """
    x={"inputname":inputname,"name":node.name,"emp_id":node.emp_id}
    results=session.run(q1,x)
    data=[{"Name":row["name"]}for row in results]
    if (len(data)>0):
        data=data[0]["Name"]
        return {"response":"node updated with new name: "+data}
    else:
        return {"response":"your input name is not found in the graph!!"}


