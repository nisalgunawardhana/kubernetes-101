# Lesson 03 — Using Minikube to Create a Cluster

## 🎯 Learning Objectives
- Install Minikube and kubectl
- Start a local Kubernetes cluster
- Understand what Minikube is and how it works

---

## What is Minikube?

**Minikube** runs a single-node Kubernetes cluster inside a VM or container on your local machine. It's the easiest way to learn and develop with Kubernetes locally — and it's completely free.

> Minikube is NOT for production. It's for learning and local development.

---

## Installation

### macOS
```bash
# Install Minikube
brew install minikube

# Install kubectl
brew install kubectl
```

### Windows
```powershell
# Using winget
winget install Kubernetes.minikube
winget install Kubernetes.kubectl
```

### Linux (Ubuntu/Debian)
```bash
# kubectl
curl -LO "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

**Also install Docker**: [docker.com/get-docker](https://docs.docker.com/get-docker/)

---

## Starting Your First Cluster

```bash
# Start minikube (uses Docker driver by default)
minikube start

# Check the cluster is running
kubectl cluster-info

# See your node
kubectl get nodes
```

Expected output:
```
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   1m    v1.28.0
```

---

## Useful Minikube Commands

```bash
minikube status          # Is cluster running?
minikube stop            # Stop the cluster (saves state)
minikube delete          # Delete the cluster completely
minikube dashboard       # Open web UI in browser
minikube ssh             # SSH into the minikube node
minikube addons list     # See available addons
minikube addons enable metrics-server  # Enable metrics
```

---

## The Kubernetes Dashboard

```bash
minikube dashboard
```

This opens a web UI where you can see everything in your cluster visually!

---

## ✅ Quick Check
1. What is Minikube used for?
2. What command starts a cluster?
3. How is Minikube different from a production cluster?


## 📚 Further Reading
- [Minikube Official Docs](https://minikube.sigs.k8s.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
