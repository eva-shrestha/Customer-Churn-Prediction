from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib 

app = FastAPI()

# class Employee(BaseModel):
#     name: "str"
#     salary: "int"=50000

# @app.get("/home")
# def home():
#     print("home")
#     return {"response":"200","msg":"Response returned"}

# @app.get("/index")
# def index():
#     return {"msg":"Index Returned!"}

# @app.post("/insertdata")
# def insertdata(data:Employee):
#     print (data.name)
#     print (data.salary)
#     return {"msg":"Data inserted"}
    

# Loading the model
model = joblib.load('D:\gritfeat\ML OOPS\ML OOPS\model\prediction2.joblib')
   
class Customer(BaseModel):
    AccountWeeks: "float"
    ContractRenewal: "int"
    DataPlan: "int"
    DataUsage: "float"
    CustServCalls: "int"
    DayMins: "float"
    DayCalls: "int"
    MonthlyCharge: "float"
    OverageFee: "float"
    RoamMins: "float"


@app.get("/home")
def home():
    print("Home")
    return {"message": "This is the home page"}


@app.post("/infer")
def infer(data:Customer):
    
    # Converting data to a 2D array
    input = [[
        data.AccountWeeks, data.ContractRenewal, data.DataPlan,
        data.DataUsage, data.CustServCalls, data.DayMins,
        data.DayCalls, data.MonthlyCharge, data.OverageFee,
        data.RoamMins
    ]]
    
    # making prediction using model
    prediction = model.predict(input)
    
    if prediction[0]==1:
        return {"Prediction":"Customer is more likely to churn"}
    else:
        return {"Predictions":"Customer is not likely to churn"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port= 8081, reload=True)