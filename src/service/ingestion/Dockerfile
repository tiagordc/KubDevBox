FROM python:3.7
WORKDIR /app
COPY requirements.txt . 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY app.py .
ENTRYPOINT ["python"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80", "--no-server-header"]