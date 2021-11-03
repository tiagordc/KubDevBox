
# Bridge for Kubernetes

Example on how to remote debug a python service running on Kubernetes
<br><br>
## Make sure the service can run in the local machine
<br>

```bash
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

<br><p align="center"><img src="/res/Bridge/01.png" /></p><br>
<br><p align="center"><img src="/res/Bridge/02.png" /></p><br>
<br><p align="center"><img src="/res/Bridge/03.png" /></p><br>
<br><p align="center"><img src="/res/Bridge/04.png" /></p><br>
<br><p align="center"><img src="/res/Bridge/05.png" /></p><br>

## Configure Bridge to Kubernetes
<br>

<br><p align="center"><img src="/res/Bridge/06.png" /></p><br>
<br><p align="center"><img src="/res/Bridge/07.png" /></p><br>
<br><p align="center"><img src="/res/Bridge/08.png" /></p><br>
<br><p align="center"><img src="/res/Bridge/09.png" /></p><br>

## Run debugger
<br>

<br><p align="center"><img src="/res/Bridge/10.png" /></p><br>
<br><p align="center"><img src="/res/Bridge/11.png" /></p><br>

# References
 * [Docs](https://docs.dapr.io/developing-applications/debugging/bridge-to-kubernetes/)