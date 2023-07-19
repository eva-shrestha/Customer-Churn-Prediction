FROM python:3.9-buster
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt
ENTRYPOINT mlflow ui --host="0.0.0.0" --port="5000"
CMD ["python","customerchurnprediction.py"]
#RUN python customerchurnprediction.py
#CMD ["mlflow","ui"]