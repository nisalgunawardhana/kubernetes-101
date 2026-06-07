# Lesson 10 — Security in Kubernetes

## 🎯 Learning Objectives
- Understand the 4Cs of cloud-native security
- Know about RBAC (Role-Based Access Control)
- Understand SecurityContext and Pod Security
- Know basic network policies

---

## The 4Cs of Cloud Native Security

```
Cloud → Cluster → Container → Code
```

Each layer must be secured. Kubernetes focuses on **Cluster** and **Container** security.

---

## 1. RBAC — Role-Based Access Control

Controls **who can do what** in your cluster.

### Key RBAC Resources

| Resource | Description |
|---|---|
| `Role` | Permissions within a namespace |
| `ClusterRole` | Permissions cluster-wide |
| `RoleBinding` | Binds a Role to a user/group |
| `ClusterRoleBinding` | Binds ClusterRole to user/group |

### Example: Read-only Role
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: default
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods-binding
  namespace: default
subjects:
- kind: User
  name: jane
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

### Check permissions:
```bash
kubectl auth can-i create pods
kubectl auth can-i delete deployments --as=jane
```

---

## 2. SecurityContext

Controls security settings **at the Pod or Container level**.

```yaml
spec:
  securityContext:
    runAsNonRoot: true       # Don't run as root
    runAsUser: 1000          # Run as user ID 1000
  containers:
  - name: my-app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true    # Read-only filesystem
      capabilities:
        drop:
        - ALL                # Drop all Linux capabilities
```

**Best practices**:
- Never run containers as `root`
- Use `readOnlyRootFilesystem: true` when possible
- Drop all capabilities and add only what's needed

---

## 3. Network Policies

Control **which pods can talk to which pods**.

By default, all pods can communicate with all other pods. Network Policies restrict this.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
  namespace: default
spec:
  podSelector: {}           # Applies to all pods
  policyTypes:
  - Ingress
  - Egress
```

This denies ALL traffic. Then explicitly allow what you need.

---

## 4. Secrets Management Best Practices

❌ Never commit secrets to Git  
❌ Never hard-code passwords in Docker images  
✅ Use Kubernetes Secrets  
✅ Enable encryption at rest for etcd  
✅ Use tools like HashiCorp Vault or Sealed Secrets  
✅ Rotate secrets regularly  

---

## 5. Image Security

```bash
# Scan images for vulnerabilities
docker scout cves my-image:latest

# Use specific image versions (not :latest in production)
image: nginx:1.21.6          # ✅ Pinned version
image: nginx:latest          # ❌ Unpredictable
```

---

## 6. Admission Controllers

Intercept requests to the API server and can **validate or mutate** them.

Common built-in admission controllers:
- `LimitRanger` — enforce resource limits
- `PodSecurity` — enforce security standards
- `ResourceQuota` — enforce namespace quotas

---

## ✅ Quick Check
1. What does RBAC stand for?
2. What's the difference between a Role and a ClusterRole?
3. Why should containers not run as root?
4. What does a Network Policy do?


## 📚 Further Reading
- [RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
