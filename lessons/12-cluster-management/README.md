# Lesson 12 — Cluster Management

## 🎯 Learning Objectives
- Manage namespaces and resource quotas
- Understand node management (taints, labels)
- Monitor cluster health
- Know basic maintenance operations

---

## Namespaces

Namespaces divide a cluster into **virtual sub-clusters**.

```bash
# List namespaces
kubectl get namespaces

# Create a namespace
kubectl create namespace staging

# Run commands in a namespace
kubectl get pods -n staging

# Set default namespace
kubectl config set-context --current --namespace=staging
```

Built-in namespaces:
- `default` — where your resources go by default
- `kube-system` — Kubernetes internal components
- `kube-public` — publicly readable resources

---

## Resource Quotas

Limit resource usage **per namespace**.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: dev-quota
  namespace: development
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 4Gi
    limits.cpu: "8"
    limits.memory: 8Gi
    pods: "20"
```

---

## LimitRange

Set **default** resource requests/limits for pods in a namespace.

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
  namespace: development
spec:
  limits:
  - default:
      cpu: 200m
      memory: 256Mi
    defaultRequest:
      cpu: 100m
      memory: 128Mi
    type: Container
```

---

## Node Management

### Labels and Selectors
```bash
# Add label to a node
kubectl label node minikube disk=ssd

# Schedule pods on specific nodes
# In deployment YAML:
spec:
  template:
    spec:
      nodeSelector:
        disk: ssd
```

### Taints and Tolerations
Taints **prevent** pods from being scheduled on a node unless they tolerate it.

```bash
# Taint a node (no pods without toleration)
kubectl taint nodes minikube key=value:NoSchedule

# Remove taint
kubectl taint nodes minikube key=value:NoSchedule-
```

---

## Monitoring Cluster Health

```bash
# Node status
kubectl get nodes

# Component status
kubectl get componentstatuses

# Events (recent cluster events)
kubectl get events --sort-by=.metadata.creationTimestamp

# Resource usage (needs metrics-server)
kubectl top nodes
kubectl top pods

# Minikube dashboard
minikube dashboard
```

---

## Draining a Node (for maintenance)

```bash
# Evict all pods from a node safely
kubectl drain minikube --ignore-daemonsets

# Mark node as unschedulable (no drain)
kubectl cordon minikube

# Re-enable scheduling
kubectl uncordon minikube
```

---

## Context and kubeconfig

Manage **multiple clusters** with contexts.

```bash
# See all contexts
kubectl config get-contexts

# Switch context
kubectl config use-context my-other-cluster

# View current context
kubectl config current-context
```

---

## ✅ Quick Check
1. What is a namespace used for?
2. What's the difference between `drain` and `cordon`?
3. What does a ResourceQuota limit?


## 📚 Further Reading
- [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
- [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
- [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
