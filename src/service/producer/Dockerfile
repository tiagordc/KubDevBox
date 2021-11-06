FROM python:3.7
WORKDIR /app
COPY . . 
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]