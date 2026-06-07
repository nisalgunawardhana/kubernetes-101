# Lesson 06 — Using a Service to Expose Your App

## 🎯 Learning Objectives
- Understand what a Kubernetes Service is
- Know the 4 Service types
- Expose a Deployment using a NodePort Service

---

## The Problem

Pods have IP addresses, but:
- Pod IPs change every time a pod is recreated
- You might have 5 pods — how do you load balance between them?
- How do you access pods from outside the cluster?

**Services** solve all of this.

---

## What is a Service?

A **Service** is a stable network endpoint that:
- Has a fixed IP and DNS name
- Load balances traffic across matching Pods
- Tracks Pods using **label selectors**

---

## Service Types

### 1. ClusterIP (default)
- Only accessible **inside** the cluster
- Used for internal service-to-service communication

```yaml
spec:
  type: ClusterIP
```

### 2. NodePort
- Exposes the service on each **Node's IP at a static port** (30000-32767)
- Accessible from outside the cluster
- Best for **local development** (Minikube)

```yaml
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080
```

### 3. LoadBalancer
- Creates a **cloud load balancer** (AWS ELB, GCP LB, etc.)
- Only works on cloud providers
- NOT available on Minikube (without addons)

### 4. ExternalName
- Maps a service to a DNS name
- Rarely used

---

## Creating a Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  selector:
    app: hello-k8s          # Matches pods with this label
  ports:
  - protocol: TCP
    port: 80                # Service port
    targetPort: 80          # Pod port
    nodePort: 30080         # External port (optional)
```

Apply it:
```bash
kubectl apply -f service.yaml
kubectl get services
```

### Access via Minikube:
```bash
minikube service my-service
# OR
minikube service my-service --url
```

---

## How Labels Connect Services to Pods

```
Service  (selector: app=hello-k8s)
    │
    ├──→ Pod 1  (label: app=hello-k8s)
    ├──→ Pod 2  (label: app=hello-k8s)
    └──→ Pod 3  (label: app=hello-k8s)
```

---

## ✅ Quick Check
1. Why do we need Services if Pods have IP addresses?
2. What's the difference between NodePort and LoadBalancer?
3. How does a Service know which Pods to send traffic to?


## 📚 Further Reading
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
