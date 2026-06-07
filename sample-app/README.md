# 📦 Sample App — Kubernetes 101

A simple Python Flask web app built to be deployed on Kubernetes using Minikube (100% free, local).

## What it does

- Serves a web page showing which **pod** it's running on
- Has a `/health` endpoint (used by Kubernetes health checks)
- Has an `/info` endpoint returning JSON app info
- Reads config from a **ConfigMap** (version, environment)

## Tech Stack

- Python 3.11 + Flask
- Docker
- Kubernetes (via Minikube)

## Quick Deploy (Step-by-Step)

### Prerequisites
Install these free tools:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or Docker Engine
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

### Step 1 — Start Minikube
```bash
minikube start
```

### Step 2 — Point Docker to Minikube's registry
```bash
# macOS/Linux
eval $(minikube docker-env)

# Windows PowerShell
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

### Step 3 — Build the Docker image
```bash
# Run this from the sample-app/ folder
docker build -t k8s101-app:latest .
```

### Step 4 — Deploy to Kubernetes
```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Step 5 — Check everything is running
```bash
kubectl get pods
kubectl get services
kubectl get deployments
```

Wait until pods show `Running` status.

### Step 6 — Open the app in your browser
```bash
minikube service k8s101-service
```

This automatically opens your browser. 🎉

### Step 7 — See it on multiple pods (scale up)
```bash
kubectl scale deployment k8s101-app --replicas=4
kubectl get pods
```

Refresh the browser a few times — watch the **pod name** change!

### Step 8 — Cleanup
```bash
kubectl delete -f k8s/
minikube stop
```

## Useful Commands

| Command | What it does |
|---|---|
| `kubectl get pods` | List all pods |
| `kubectl describe pod <name>` | Detailed info on a pod |
| `kubectl logs <pod-name>` | View pod logs |
| `kubectl exec -it <pod-name> -- bash` | Shell into a pod |
| `minikube dashboard` | Open Kubernetes web UI |
