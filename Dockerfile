FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python","customerchurnprediction.py"]

# RUN python customerchurnprediction.py
# CMD ["mlflow","ui"]

# docker run -p 5000