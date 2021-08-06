from fastapi import FastAPI
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv
load_dotenv()
uri=os.getenv("uri")
user=os.getenv("user")
pwd=os.getenv("pwd")

def connection():
    driver=GraphDatabase.driver(uri=uri,auth=(user,pwd))
    return (driver)

app=FastAPI()
@app.get("/")
def default():
    return {"response":"you are in root path"}

@app.get("/count")
def countnode(label):
    driver_neo4j=connection()
    session=driver_neo4j.session()
    q1="""
    match(n) where labels(n) in [[$a]] return n.Name as name ,count(n) as count
    """
    x={"a":label}
    results=session.run(q1,x)
    return {"response":[{"Name":row["name"],"Count":row["count"]}for row in results]}
   
