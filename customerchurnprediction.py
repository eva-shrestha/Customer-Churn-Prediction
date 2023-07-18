import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import RandomOverSampler
import mlflow
from datetime import datetime

mlflow.set_tracking_uri('http://127.0.0.1:5000/')
mlflow.set_experiment('Customer Churn Analysis')


df = pd.read_csv("./data/telecom_churn.csv")

X = df.drop('Churn', axis=1)
y = df['Churn']

#Standarization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Classification
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

X_train = np.array(X_train)
y_train = np.array(y_train)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with mlflow.start_run(run_name=f"Logistic Regression for imbalanced data {timestamp}"):

    mlflow.autolog(disable=True)

    model = LogisticRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # Save the trained model 
    joblib.dump(model, './model/prediction1.joblib')

    # Generate the classification report
    report = classification_report(y_test, y_pred, output_dict = True)

    mlflow.log_param('model', "LogisticRegression")

    mlflow.log_metric("accuracy", report['accuracy'])
    mlflow.log_metric("precision", report['1']['precision'])
    mlflow.log_metric("recall", report['1']['recall'])

    mlflow.log_artifact('./model/prediction1.joblib')

    mlflow.end_run()


"""So, here we can see that the recall of the 1 is very less, since the dataset is imbalance.
    Handling Imbalance dataset
"""


with mlflow.start_run(run_name=f"Logistic Regression for resampled data {timestamp}"):

    mlflow.autolog(disable=True)

    # Handling imbalanced data using RandomOverSampler
    oversampler = RandomOverSampler(random_state=42)
    X_train_resampled, y_train_resampled = oversampler.fit_resample(X_train, y_train)

    model1 = LogisticRegression()

    model1.fit(X_train_resampled, y_train_resampled)

    y_pred = model1.predict(X_test)

    # Save the trained model 
    joblib.dump(model1, './model/prediction2.joblib')

    #classification report
    report = classification_report(y_test, y_pred, output_dict = True)

    mlflow.log_param('model', "LogisticRegression")
    mlflow.log_param('over_sampler', "RandomOverSampler")

    mlflow.log_metric("accuracy", report['accuracy'])
    mlflow.log_metric("precision", report['1']['precision'])
    mlflow.log_metric("recall", report['1']['recall'])

    mlflow.log_artifact('./model/prediction2.joblib')

    mlflow.end_run()




