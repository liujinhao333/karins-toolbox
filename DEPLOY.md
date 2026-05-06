# Karin的百宝箱 - 部署指南

## 服务器要求

- **配置**: 2核 2GB RAM
- **系统**: Ubuntu 20.04+ / Debian 11+
- **已安装**: Docker

## 部署步骤

### 1. 安装 K3s

```bash
curl -sfL https://get.k3s.io | sh -s - \
  --disable traefik \
  --disable servicelb \
  --write-kubeconfig-mode 644

# 验证安装
kubectl get nodes
```

### 2. 安装 Nginx Ingress Controller

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.4/deploy/static/provider/cloud/deploy.yaml

# 等待就绪
kubectl wait --for=condition=ready pod -l app.kubernetes.io/component=controller -n ingress-nginx --timeout=120s
```

### 3. 配置存储

```bash
# 创建数据目录
mkdir -p /var/data/toolbox

# 或者使用 NFS/云存储进行持久化
```

### 4. 部署应用

```bash
cd /opt/toolbox

# 设置 Docker Hub 用户名
export DOCKER_USERNAME="your-username"

# 部署
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/backend/
kubectl apply -f k8s/frontend/
kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/networkpolicy.yaml
kubectl apply -f k8s/monitoring/
```

### 5. 验证部署

```bash
# 检查 pods
kubectl get pods -n toolbox

# 检查 services
kubectl get svc -n toolbox

# 运行健康检查
./deploy/health_check.sh
```

### 6. 配置域名解析

在 DNS 服务商添加记录:
- `tools.yoursite.com` → 服务器 IP
- `api.tools.yoursite.com` → 服务器 IP

### 7. 配置 SSL (可选)

使用 Let's Encrypt:

```bash
kubectl apply -f https://raw.githubusercontent.com/cert-manager/cert-manager/master/deploy/manifests/issuers.yaml

# 创建 ClusterIssuer
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: your-email@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      - http01:
          ingressClass: nginx
EOF
```

## 监控访问

- **Prometheus**: http://服务器IP:30090
- **Grafana**: http://服务器IP:30300 (admin/admin)
- **Loki**: http://服务器IP:30310

## 维护

### 更新应用

```bash
# 重新部署
./deploy/deploy.sh

# 或手动滚动更新
kubectl rollout restart deployment toolbox-backend -n toolbox
kubectl rollout restart deployment toolbox-frontend -n toolbox
```

### 备份数据

```bash
./deploy/backup.sh
```

### 查看日志

```bash
# 后端日志
kubectl logs -n toolbox -l app=toolbox-backend -f

# 前端日志
kubectl logs -n toolbox -l app=toolbox-frontend -f
```

## 故障排查

### Pod 无法启动

```bash
kubectl describe pod <pod-name> -n toolbox
kubectl logs <pod-name> -n toolbox
```

### Service 无法访问

```bash
kubectl get endpoints -n toolbox
kubectl describe svc <svc-name> -n toolbox
```

### 资源不足

```bash
kubectl top nodes
kubectl top pods -n toolbox
```

## 资源规划 (2C2G)

| 组件 | CPU Request | Memory Limit |
|------|-------------|--------------|
| K3s | - | 400MB |
| Nginx Ingress | 50m | 150MB |
| Backend x2 | 100m | 512MB |
| Frontend x2 | 100m | 128MB |
| Prometheus | 100m | 512MB |
| Grafana | 50m | 256MB |
| Loki | 50m | 256MB |
| **总计** | ~550m | ~2214MB |
