# Lesson 09 — Configuration: ConfigMaps and Secrets

## 🎯 Learning Objectives
- Create and use ConfigMaps
- Create and use Secrets
- Inject config into Pods as environment variables or files

---

## Why Separate Config from Code?

Hard-coding config in your Docker image is bad:
- Can't change config without rebuilding image
- Secrets end up in your image (security risk!)
- Different environments need different values

Kubernetes solves this with **ConfigMaps** and **Secrets**.

---

## ConfigMaps

Store non-sensitive config as key-value pairs.

### Create a ConfigMap
```bash
# From literal values
kubectl create configmap app-config \
  --from-literal=APP_ENV=production \
  --from-literal=APP_VERSION=2.0.0

# From a file
kubectl create configmap nginx-conf --from-file=nginx.conf
```

### ConfigMap YAML
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: "production"
  APP_VERSION: "2.0.0"
  LOG_LEVEL: "info"
```

### Use ConfigMap in a Pod
```yaml
spec:
  containers:
  - name: my-app
    image: my-app:latest
    envFrom:
    - configMapRef:
        name: app-config    # inject ALL keys as env vars
```

Or pick specific keys:
```yaml
    env:
    - name: MY_ENV
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: APP_ENV
```

---

## Secrets

For sensitive data: passwords, API keys, certificates.

### Create a Secret
```bash
kubectl create secret generic db-secret \
  --from-literal=DB_PASSWORD=supersecret123 \
  --from-literal=DB_USER=admin
```

### Secret YAML
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  DB_PASSWORD: c3VwZXJzZWNyZXQxMjM=    # base64 encoded!
  DB_USER: YWRtaW4=
```

Encode values: `echo -n "mysecret" | base64`

### Use Secret in a Pod
```yaml
    envFrom:
    - secretRef:
        name: db-secret
```

> ⚠️ **Note**: Secrets are only base64 encoded by default, NOT encrypted. Use [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets) or KMS for real encryption.

---

## Mount as Files (not env vars)

```yaml
    volumeMounts:
    - name: config-vol
      mountPath: /etc/config
  volumes:
  - name: config-vol
    configMap:
      name: app-config
```

This creates files in `/etc/config/` — one file per key.

---

## ✅ Quick Check
1. What's the difference between ConfigMap and Secret?
2. Are Secrets encrypted by default?
3. Name two ways to inject ConfigMap data into a Pod.


## 📚 Further Reading
- [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
