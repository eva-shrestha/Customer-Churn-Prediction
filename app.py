from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()
class Employee(BaseModel):
    name: "str"
    salary: "int"=50000

@app.get("/home")
def home():
    print("home")
    return {"response":"200","msg":"Response returned"}

@app.get("/index")
def index():
    return {"msg":"Index Returned!"}

@app.post("/insertdata")
def insertdata(data:Employee):
    print (data.name)
    print (data.salary)
    return {"msg":"Data inserted"}
    

if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port= 8081, reload=True)