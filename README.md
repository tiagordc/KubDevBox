
# Kub Dev Box

This is a guide to setup a full Kubernetes dev machine with some sample microservices
\
&nbsp;
## Stack

 * [Kubernetes](#kubernetes) on [minikube](#minikube)
 * [Kafka](#kafka) cluster for event streaming with [ksqlDB](#ksqldb)
 * [Keda](#keda) autoscaler
 * [Dapr](#dapr) runtime
 * [Prometheus](#prometheus) and [Grafana](#grafana)
 * [Keycloak](#eycloak) identity server
 
\
&nbsp;
## Steps

 * [Linux](Linux.md)
 * [MacOS](Mac.md)
 * [Debugger](Bridge.md)
\
&nbsp;
\
&nbsp;
# References
## Kubernetes
 * [Tips and Tricks](https://www.ibm.com/cloud/blog/8-kubernetes-tips-and-tricks)

## Minikube
 * [Deep Dive Into Minikube](https://www.youtube.com/watch?v=GHczvbzuVvc)
 * [Ingress](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)
 
## Keda
 * [Install](https://keda.sh/docs/2.4/deploy/#install-2)

## Kafka
 * [Strimzi quickstart](https://strimzi.io/quickstarts/)
 * [Strimzi Video Tutorial](https://www.youtube.com/watch?v=4bKSPrENDQQ)
 * [Strimzi with ksqlDB](https://ludusrusso.space/blog/2020/08/ksql-strimzi-k8s)

## Dapr
 * [Docs](https://docs.dapr.io/)
 * [Setup](https://github.com/dapr/quickstarts/tree/v1.4.0/hello-kubernetes)
 * [Intro](https://www.youtube.com/watch?v=MjyulcRqh20)
 * [Examples](https://github.com/gbaeke/dapr-demo)
 * [Advanced Dapr](https://www.youtube.com/watch?v=QlzbQHGTS6c)
