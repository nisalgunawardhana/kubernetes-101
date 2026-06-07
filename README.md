# ☸️ Kubernetes-101

Welcome! This repo is a **free, hands-on Kubernetes course** built for developers who want to go from zero to confidently managing real clusters — no paid tools, no cloud account required.

You'll learn Kubernetes by actually doing it: every lesson has a task, every concept is backed by a working example, and the course wraps up with a full end-to-end deployment challenge you can submit for a **completion badge**.

> **What this repo is:** A structured, 12-lesson guided course covering Kubernetes architecture, deployments, scaling, updates, configuration, security, and cluster management — all running locally on your machine with Minikube.
>
> **Who it's for:** Backend engineers, DevOps beginners, or anyone who has heard of Kubernetes and wants to actually understand it by building things.
>
> **What you'll walk away with:** A working local cluster, a deployed sample app, and the confidence to read and write Kubernetes manifests from scratch.

---
[![Follow me on GitHub](https://img.shields.io/badge/Follow-nisalgunawardhana-blue?logo=github&style=social)](https://github.com/nisalgunawardhana)
[![Star this repo](https://img.shields.io/github/stars/nisalgunawardhana/Kubernetes-101?style=social)](https://github.com/nisalgunawardhana/kubernetes-101/stargazers)

---

## 🎯 What You'll Learn

By completing this course you will be able to:
- Explain Kubernetes architecture and all its components
- Create and manage a local Kubernetes cluster using Minikube
- Deploy, scale, update, and expose applications
- Configure apps with ConfigMaps and Secrets
- Apply basic security practices
- Work with stateless and stateful applications
- Manage namespaces, quotas, and cluster resources

---

## 🛠️ Prerequisites

Before starting, install these free tools:

| Tool | Purpose | Install |
|---|---|---|
| **Docker** | Container runtime | [docker.com](https://docs.docker.com/get-docker/) |
| **Minikube** | Local Kubernetes cluster | [minikube.sigs.k8s.io](https://minikube.sigs.k8s.io/docs/start/) |
| **kubectl** | Kubernetes CLI | [kubernetes.io/docs/tasks/tools](https://kubernetes.io/docs/tasks/tools/) |
| **Git** | Version control | [git-scm.com](https://git-scm.com/) |

> 💡 All tools are **100% free** and run **locally** — no cloud account required!

---

## 📚 Table of Contents

| # | Lesson | Topics |
|---|---|---|
| 01 | [What is Kubernetes?](./lessons/01-what-is-kubernetes/) | Overview, why it exists, containers vs K8s |
| 02 | [Kubernetes Components A-Z](./lessons/02-kubernetes-components/) | Control plane, worker nodes, all K8s objects |
| 03 | [Create a Cluster with Minikube](./lessons/03-minikube-create-cluster/) | Install, start cluster, dashboard |
| 04 | [Deployments with kubectl](./lessons/04-kubectl-deployments/) | kubectl basics, YAML manifests, apply |
| 05 | [Pods and Nodes](./lessons/05-pods-and-nodes/) | Inspect, logs, exec, lifecycle |
| 06 | [Expose with Services](./lessons/06-expose-with-service/) | ClusterIP, NodePort, LoadBalancer |
| 07 | [Scaling Your App](./lessons/07-scaling-app/) | Manual scale, HPA, replicas |
| 08 | [Rolling Updates](./lessons/08-rolling-update/) | Zero-downtime updates, rollback |
| 09 | [Configuration](./lessons/09-configuration/) | ConfigMaps, Secrets, env injection |
| 10 | [Security](./lessons/10-security/) | RBAC, SecurityContext, Network Policies |
| 11 | [Stateless vs Stateful](./lessons/11-stateless-vs-stateful/) | Deployments, StatefulSets, PVCs |
| 12 | [Cluster Management](./lessons/12-cluster-management/) | Namespaces, quotas, node management |

---

## 🚀 Main Task: Deploy the Sample App

After completing the lessons (or right now if you want a challenge!), complete this main task:

### 📋 Task: Deploy Kubernetes-101 Sample App Locally (100% Free)

Get the sample app → build it → create a cluster → deploy → access it publicly on your local machine.

The full sample app and its manifests live in [`sample-app/`](./sample-app/). See the [sample-app README](./sample-app/README.md) for the complete reference.

---

### Step 0 — Fork & Clone This Repo
```bash
# Fork the repo on GitHub first, then:
git clone https://github.com/YOUR-USERNAME/Kubernetes-101.git
cd Kubernetes-101
```

### Step 1 — Start Minikube
```bash
minikube start
minikube status
```
✅ You should see: `host: Running`, `kubelet: Running`, `apiserver: Running`

### Step 2 — Point Docker to Minikube
```bash
# macOS/Linux
eval $(minikube docker-env)

# Windows PowerShell
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

### Step 3 — Build the Docker Image
```bash
cd sample-app
docker build -t k8s101-app:latest .
```

### Step 4 — Deploy to Kubernetes
```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Step 5 — Verify Everything Is Running
```bash
kubectl get pods
kubectl get services
kubectl get deployments
```
Wait until all pods show `Running`.

### Step 6 — Open the App
```bash
minikube service k8s101-service
```
Your browser opens showing the pod name, version, and environment. 🎉

### Step 7 — Scale and Watch Load Balancing
```bash
kubectl scale deployment k8s101-app --replicas=4
kubectl get pods
```
Refresh the browser — watch the **pod name** change between requests!

### Step 8 — Try a Rolling Update
```bash
# Edit the ConfigMap APP_VERSION to 2.0.0, then:
kubectl apply -f k8s/configmap.yaml
kubectl rollout restart deployment k8s101-app
kubectl rollout status deployment k8s101-app
```

### Step 9 — Cleanup
```bash
kubectl delete -f k8s/
minikube stop
```

---

## 🏅 Submit & Earn Your Badge

Once you finish the **Main Task**, submit it to earn your official completion badge:

<p align="center">
  <img src="images/badge.png" alt="Kubernetes-101 Completion Badge" width="160">
</p>

**Quick version:**
1. Fork this repo and create a branch: `submission/<your-username>`
2. Take a screenshot at **each step** of the Main Task
3. Add all screenshots to `submissions/<your-username>/`
4. Push and open a **Pull Request** targeting **this repo's `main` branch**
5. Copy your PR link, then open a [**🏅 Badge Submission issue**](../../issues/new?template=submission.yml) with your details + PR link
6. After the maintainer reviews and closes your issue → your **badge is awarded automatically** 🎉

> 📖 **Full step-by-step instructions:** [SUBMISSION.md](./SUBMISSION.md)
>
> ⚠️ You only need to submit the **Main Task** — the smaller lesson tasks are optional practice and do not need to be submitted.

---

## 🗂️ Repository Structure

```
Kubernetes-101/
├── README.md                  ← You are here
├── lessons/                   ← 12 hands-on lessons
│   ├── 01-what-is-kubernetes/
│   ├── 02-kubernetes-components/
│   ├── 03-minikube-create-cluster/
│   ├── 04-kubectl-deployments/
│   ├── 05-pods-and-nodes/
│   ├── 06-expose-with-service/
│   ├── 07-scaling-app/
│   ├── 08-rolling-update/
│   ├── 09-configuration/
│   ├── 10-security/
│   ├── 11-stateless-vs-stateful/
│   └── 12-cluster-management/
├── sample-app/                ← Flask app + Docker + K8s manifests
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── k8s/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── configmap.yaml
│   └── README.md
├── submissions/               ← Put YOUR Main Task screenshots here
│   └── <your-username>/
├── SUBMISSION.md              ← How to submit & earn your badge
└── .github/                   ← Issue form + badge automation
    ├── ISSUE_TEMPLATE/
    └── workflows/
```

---

## 🤝 How to Use This Course

1. **Read** each lesson README in order
2. **Do** the hands-on task at the end of each lesson
3. **Screenshot** your results as proof
4. **Push** your work to your forked repo
5. **Complete** the main task to tie it all together

---

## 📚 Additional Resources

- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)

---

## 🌐 Connect with Me

Follow me on social media for updates and more learning resources:

[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter&logoColor=white&style=for-the-badge)](https://twitter.com/thenisals)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white&style=for-the-badge)](https://linkedin.com/in/nisalgunawardhana)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?logo=instagram&logoColor=white&style=for-the-badge)](https://instagram.com/thenisals)

**Happy Learning! 🎉**

Remember: Making mistakes is part of learning. Don't be afraid to experiment and try new things!

