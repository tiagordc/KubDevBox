
# Linux

Guide for Ubuntu Desktop
\
&nbsp;
1) Download and install Ubuntu Desktop (tested on a virtual machine)
\
&nbsp;
2) Install prerequisites:

```bash
sudo apt update
sudo apt upgrade

# on VMWare:
# sudo apt install open-vm-tools-desktop

sudo apt install net-tools htop cpu-checker python3-venv docker.io \
                 libvirt-clients libvirt-daemon-system qemu-kvm

sudo setfacl -m user:$USER:rw /var/run/docker.sock
sudo usermod -aG libvirt $USER
newgrp libvirt

sudo kvm-ok
sudo virt-host-validate

sudo reboot now
```
\
&nbsp;
3) Install Kubernetes

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    && rm kubectl

curl -LO https://storage.googleapis.com/minikube/releases/latest/docker-machine-driver-kvm2 \
    && sudo install docker-machine-driver-kvm2 /usr/local/bin/ && rm docker-machine-driver-kvm2
    
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
    && sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```
\
&nbsp;
4) Extras

```bash
# Resources
git clone https://github.com/tiagordc/KubDevBox.git

# Dapr
wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash

# Utils
sudo git clone https://github.com/ahmetb/kubectx /opt/kubectx
sudo ln -s /opt/kubectx/kubectx /usr/local/bin/kubectx
sudo ln -s /opt/kubectx/kubens /usr/local/bin/kubens

# Alias
cat >> ~/.bash_aliases << EOT
alias c='clear'
alias m='minikube'
alias k='kubectl'
alias l='ls -la'
alias watch='watch '
alias python='python3 '
alias kc='k config view --minify | grep name'
alias kdp='kubectl describe pod'
alias krh='kubectl run --help | more'
alias ugh='kubectl get --help | more'
alias kd='kubectl describe pod'
alias ke='kubectl explain'
alias kf='kubectl create -f'
alias kg='kubectl get pods --show-labels'
alias kr='kubectl replace -f'
alias kh='kubectl --help | more'
alias krh='kubectl run --help | more'
alias ks='kubectl get namespaces'
alias kga='k get pod --all-namespaces'
alias kgaa='kubectl get all --show-labels'
EOT

cat >> ~/.bashrc << EOT
if [ -f ~/.bash_aliases ]; then
  . ~/.bash_aliases
fi
EOT

source ~/.bashrc
```

\
&nbsp;
5) Start cluster

```bash
m profile list
m start --cpus=max --memory=max --driver=kvm2 -p dev
# m tunnel -p dev
# m dashboard -p dev
```
\
&nbsp;
6) Install Kafka (using strimzi):

```bash
k create namespace kafka
kubens kafka
k apply -f "https://strimzi.io/install/latest?namespace=kafka"
k apply -f ~/KubDevBox/src/deploy/kafka.yaml
k wait kafka/main --for=condition=Ready --timeout=300s
```
\
&nbsp;
7) Test Kafka (optional)

```bash
k get kafka -o yaml

k run kafka-producer -ti \
                     --image=quay.io/strimzi/kafka:0.26.0-kafka-3.0.0 \
                     --rm=true --restart=Never -- bin/kafka-console-producer.sh \
                     --broker-list main-kafka-bootstrap.kafka.svc.cluster.local:9092 \
                     --topic my-topic

k run kafka-consumer -ti \
                     --image=quay.io/strimzi/kafka:0.26.0-kafka-3.0.0 \
                     --rm=true --restart=Never -- bin/kafka-console-consumer.sh \
                     --bootstrap-server main-kafka-bootstrap.kafka.svc.cluster.local:9092 \
                     --topic my-topic --from-beginning

k delete pod kafka-consumer
k delete pod kafka-producer
k delete kafkatopic my-topic
```
\
&nbsp;
8) Install ksqlDB

```bash

```
\
&nbsp;
9) Install Keda

```bash
k apply -f https://github.com/kedacore/keda/releases/download/v2.4.0/keda-2.4.0.yaml
```
\
&nbsp;
10) Initialize Dapr:

```bash
kubens default
dapr init -k --wait
dapr status -k
# dapr dashboard -k -p 9999
```
\
&nbsp;
11) Test Kafka with a Dapr connector and [VSCode debugging](Bridge.md) (optional)

```bash
cat << EOF | k create -f -
apiVersion: kafka.strimzi.io/v1beta2
kind: KafkaTopic
metadata:
  name: request-topic
  labels:
    strimzi.io/cluster: "main"
spec:
  partitions: 3
  replicas: 2
EOF

cat << EOF | k create -f -
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: request-pubsub
spec:
  type: pubsub.kafka
  version: v1
  metadata:
    - name: brokers
      value: "main-kafka-bootstrap.kafka.svc.cluster.local:9092"
    - name: authRequired
      value: "false"
    - name: initialOffset
      value: "oldest"
    - name: maxMessageBytes
      value: 8192
EOF

cat << EOF | k create -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: producer
  labels:
    app: producer
spec:
  replicas: 1
  selector:
    matchLabels:
      app: producer
  template:
    metadata:
      labels:
        app: producer
      annotations:
        dapr.io/enabled: "true"
        dapr.io/app-id: "producer"
    spec:
      containers:
      - name: node
        image: tiagorcdocker/dapr-demo-producer-py
        imagePullPolicy: Always
        env:
        - name: TOPIC
          value: "request-topic"
        - name: PUBSUB
          value: "request-pubsub"
EOF

k expose deployment producer --type ClusterIP --port 9876

# In VSCode using Bridge to Kubernetes you should now be able to debug the producer app

k create -f ~/KubDevBox/src/service/ingestion/k8s.yaml

k run kafka-consumer -ti \
                     --image=quay.io/strimzi/kafka:0.26.0-kafka-3.0.0 \
                     --rm=true --restart=Never -- bin/kafka-console-consumer.sh \
                     --bootstrap-server main-kafka-bootstrap.kafka.svc.cluster.local:9092 \
                     --topic request-topic --from-beginning

# cleanup
k delete pod kafka-consumer
k delete service producer
k delete deployment producer
k delete component request-pubsub
k delete kafkatopic request-topic
```
