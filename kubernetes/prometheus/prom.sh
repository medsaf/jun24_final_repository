#! /bin/bash

alias k="microk8s kubectl"

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm install kube-prometheus-stack \
  --create-namespace \
  --namespace kube-prometheus-stack \
  prometheus-community/kube-prometheus-stack

kubectl port-forward -n kube-prometheus-stack svc/kube-prometheus-stack-prometheus 9090:9090
