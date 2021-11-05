FROM python:3.7
WORKDIR /app
COPY . . 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ENTRYPOINT ["python"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]