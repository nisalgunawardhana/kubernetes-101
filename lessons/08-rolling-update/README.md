# Lesson 08 — Performing a Rolling Update

## 🎯 Learning Objectives
- Update a Deployment with zero downtime
- Understand rolling update strategy
- Roll back a bad deployment

---

## What is a Rolling Update?

Instead of stopping all pods and starting new ones (downtime!), Kubernetes updates pods **gradually**:

```
Before:  [v1] [v1] [v1] [v1]
Step 1:  [v2] [v1] [v1] [v1]
Step 2:  [v2] [v2] [v1] [v1]
Step 3:  [v2] [v2] [v2] [v1]
After:   [v2] [v2] [v2] [v2]
```

Traffic keeps flowing during the whole update. Zero downtime! ✅

---

## Performing a Rolling Update

### Update the image version:
```bash
kubectl set image deployment/hello-k8s nginx=nginx:1.21

# Watch the rollout
kubectl rollout status deployment/hello-k8s

# See the rollout history
kubectl rollout history deployment/hello-k8s
```

---

## Rolling Update Strategy in YAML

```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1         # Max extra pods during update
      maxUnavailable: 0   # No pods can be unavailable
```

---

## Rolling Back

If the new version is broken:

```bash
# Roll back to previous version
kubectl rollout undo deployment/hello-k8s

# Roll back to a specific revision
kubectl rollout undo deployment/hello-k8s --to-revision=2

# Check history
kubectl rollout history deployment/hello-k8s
```

---

## ✅ Quick Check
1. Why is rolling update better than stopping all pods at once?
2. What does `maxUnavailable: 0` mean?
3. How do you undo a bad deployment?


## 📚 Further Reading
- [Performing Rolling Updates](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/)
