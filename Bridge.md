
# Bridge for Kubernetes

Example on how to remote debug a python service running on Kubernetes
\
&nbsp;
1) Make sure the service can run in the local machine
\
&nbsp;
```bash
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

<p align="center">
  <img src="/res/Bridge/01.png" />
</p>

# References
 * [Docs](https://docs.dapr.io/developing-applications/debugging/bridge-to-kubernetes/)