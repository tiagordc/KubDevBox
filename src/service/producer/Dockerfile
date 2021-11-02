FROM python:3.7.1-alpine3.8
WORKDIR /app
COPY . . 
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]