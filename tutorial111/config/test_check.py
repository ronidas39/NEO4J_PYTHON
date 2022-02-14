from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://127.0.0.1:7687",auth=("neo4j","Rambo@1234"))
print(driver)
