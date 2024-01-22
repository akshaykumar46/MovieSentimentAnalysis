
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt  requirements.txt
RUN pip install -r requirements.txt
COPY ["models/sentiment_model_pipeline.pkl", "main.py","test.py", "./"] 
# CMD ["python3", "test.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
