import joblib

# Load the model
model = joblib.load('D:\gritfeat\ML OOPS\ML OOPS\model\prediction2.joblib')

#function to print the churn prediction using churn
def prediction(data):
  predictions = model.predict([data])

  if predictions[0] == 1 :
    return "Customer is more likely to churn"
  
  else:
    return "Customer is not likely churn"

data = [107,1,1,3.7,1,161.6,123,82,9.78,13.7]

print(prediction(data))