# Lesson 11 — Stateless vs Stateful Applications

## 🎯 Learning Objectives
- Understand the difference between stateless and stateful apps
- Know when to use Deployments vs StatefulSets
- Understand PersistentVolumes

---

## Stateless Applications

A **stateless** app doesn't store data locally between requests.

Examples: web servers, APIs, load balancers

- Any pod can handle any request
- Pods are interchangeable
- Easy to scale up/down
- If a pod dies, no data is lost
- **Use Deployment** for stateless apps

```yaml
kind: Deployment    # ✅ For stateless apps
```

---

## Stateful Applications

A **stateful** app stores data and has a unique identity.

Examples: databases (MySQL, PostgreSQL), message queues (Kafka), caches (Redis with persistence)

- Each pod has a **stable network identity** (pod-0, pod-1...)
- Pods have **persistent storage** that survives restarts
- Pods start and stop in **order**
- **Use StatefulSet** for stateful apps

```yaml
kind: StatefulSet   # ✅ For stateful apps
```

---

## StatefulSet vs Deployment

| Feature | Deployment | StatefulSet |
|---|---|---|
| Pod names | Random (abc123) | Ordered (app-0, app-1) |
| Storage | Ephemeral | Persistent |
| Pod order | Random start/stop | Ordered |
| Use case | Web servers, APIs | Databases, Kafka |
| Identity | No stable identity | Stable network identity |

---

## PersistentVolumes (PV) and PersistentVolumeClaims (PVC)

For stateful apps, you need storage that **outlives the pod**.

### PersistentVolume (PV)
The actual storage resource (created by admin or cloud provider).

### PersistentVolumeClaim (PVC)
A request for storage from a pod.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-data
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Use in a Pod:
```yaml
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: my-data
```

---

## Simple StatefulSet Example (MySQL)

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: "mysql"
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-secret
              key: password
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 5Gi
```

---

## ✅ Quick Check
1. Name two examples of stateless apps and two stateful apps
2. Which Kubernetes resource is used for databases?
3. What's the difference between PV and PVC?


## 📚 Further Reading
- [StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
