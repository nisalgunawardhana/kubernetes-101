# Lesson 07 — Scale Your App: Running Multiple Instances

## 🎯 Learning Objectives
- Scale a Deployment up and down
- Understand why scaling matters
- Use Horizontal Pod Autoscaler (HPA) basics

---

## Why Scale?

- Handle more traffic by running more pod copies
- Improve availability (if one pod crashes, others keep serving)
- Distribute load across multiple nodes

---

## Manual Scaling

```bash
# Scale up to 4 replicas
kubectl scale deployment hello-k8s --replicas=4

# Watch pods being created
kubectl get pods -w

# Scale back down
kubectl scale deployment hello-k8s --replicas=2
```

Or update your YAML:
```yaml
spec:
  replicas: 4    # change this number
```
Then: `kubectl apply -f deployment.yaml`

---

## Verify Load Balancing

With multiple pods running, the Service will distribute traffic.

If your app shows the Pod hostname (like our sample-app does), refresh the browser multiple times — you'll see different pod names!

```bash
# See pods spread across nodes
kubectl get pods -o wide

# Check the endpoints the Service is routing to
kubectl get endpoints my-service
```

---

## Horizontal Pod Autoscaler (HPA)

Automatically scales based on CPU or memory usage.

```bash
# Enable metrics-server addon first
minikube addons enable metrics-server

# Create HPA: scale between 2-10 pods when CPU > 50%
kubectl autoscale deployment hello-k8s --cpu-percent=50 --min=2 --max=10

# Check HPA status
kubectl get hpa
```

---

## ✅ Quick Check
1. What happens to traffic when you scale from 1 to 3 pods?
2. What does HPA stand for and what does it do?
3. If you scale down from 5 to 2 pods, what happens to the 3 removed pods?


## 📚 Further Reading
- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
