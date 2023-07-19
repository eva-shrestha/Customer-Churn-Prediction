# Customer-Churn-Prediction
Customer churn prediction project with experiment tracking using ML flow and docker implementation

## Overview
The main focus of this project is to predict customer churn, which means determining whether a customer is likely to stop using a service or product. To achieve this, we'll be creating a machine learning model that analyzes historical data and customer behavior patterns. This model will help businesses identify potential churn indicators, allowing them to take proactive measures to retain customers.

## Tags
Python <br><br>
scikit-learn (sklearn) <br><br>
MLflow <br><br>
Docker <br><br>
fastAPI <br><br>

## Steps to run the project:

### Running the project on your local machine:

1. First, clone the project repository from GitHub using the command: git clone <repository_url> <br><br>
2. Navigate to the project directory using the command: cd <project_directory> <br><br>
3. Install the necessary dependencies using pip: pip install -r requirements.txt <br><br>
4. Finally, run the code by executing: python customerchurnprediction.py <br><br>

### Running the project using Docker:

1. Make sure you have Docker installed on your system. <br><br>
2. Clone the project repository from GitHub using the command: git clone <repository_url> <br><br>
3. Navigate to the project directory: cd <project_directory> <br><br>
4. Build the Docker image: docker build -t <image_name> . <br><br>
5. Run the Docker container with the created image and create port mapping with MLflow: <br>
   docker run -d -p “5000:5000” —name <containername> <imagename> <br><br>

### To install fastAPI:

  pip install fastapi[all]
