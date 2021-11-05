
# Producer demo application

This app is available as a container image on tiagorcdocker/dapr-demo-producer-py

```bash
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# docker login
# docker build -t tiagorcdocker/dapr-demo-producer-py:latest ~/KubDevBox/src/service/producer
# docker push tiagorcdocker/dapr-demo-producer-py
```
