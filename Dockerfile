FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask boto3

EXPOSE 5000

CMD ["python", "app.py"]
