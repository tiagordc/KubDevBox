
# Kub Dev Box

This is a guide to setup a Kubernetes dev playground with some sample services
\
&nbsp;
## Stack

 * [Kubernetes](#kubernetes) on [minikube](#minikube)
 * [Keycloak](#keycloak) identity server
 * [Dapr](#dapr) service runtime
 * [Kafka](#kafka) or [TimescaleDB](#timescaledb) for data ingestion
 * [Prometheus](#prometheus) and [Grafana](#grafana)
 
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
 
## Keycloak
 * [Deployment](https://www.keycloak.org/getting-started/getting-started-operator-kubernetes)
 * [Yaml Examples](https://github.com/keycloak/keycloak-operator/tree/main/deploy/examples)

## Dapr
 * [Docs](https://docs.dapr.io/)
 * [Setup](https://github.com/dapr/quickstarts/tree/v1.4.0/hello-kubernetes)
 * [Intro](https://www.youtube.com/watch?v=MjyulcRqh20)
 * [Examples](https://github.com/gbaeke/dapr-demo)
 * [Advanced Dapr](https://www.youtube.com/watch?v=QlzbQHGTS6c)

## Kafka
 * [Strimzi quickstart](https://strimzi.io/quickstarts/)
 * [Strimzi Video Tutorial](https://www.youtube.com/watch?v=4bKSPrENDQQ)
 * [Strimzi with ksqlDB](https://ludusrusso.space/blog/2020/08/ksql-strimzi-k8s)

## TimescaleDB
