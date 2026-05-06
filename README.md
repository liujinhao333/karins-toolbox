# 🧰 Karin's Toolbox

[![GitHub license](https://img.shields.io/github/license/liujinhao333/karins-toolbox)](https://github.com/liujinhao333/karins-toolbox/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/liujinhao333/karins-toolbox)](https://github.com/liujinhao333/karins-toolbox/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/liujinhao333/karins-toolbox)](https://github.com/liujinhao333/karins-toolbox/network)

一个功能丰富的在线工具箱平台，集成多种开发者常用工具、在线简历制作及运维管理面板。

[English](#english) | [中文](#中文)

---

## 中文

### ✨ 功能特性

#### 转换工具
- **JSON/YAML 转换** - JSON 与 YAML 格式互转，支持格式化
- **时间戳转换** - 时间戳与日期时间互转，实时显示当前时间戳
- **Base64 编解码** - 文本编解码、图片转 Base64、Base64 转图片

#### 生成工具
- **UUID 生成器** - 批量生成 UUID v4
- **Hash 生成器** - MD5 / SHA-1 / SHA-256 / SHA-512 哈希计算
- **密码生成器** - 可配置长度、字符类型，强度评估
- **二维码生成器** - 输入文本/URL 生成二维码，支持下载
- **Cron 表达式** - 可视化配置 Cron 表达式，解析最近 5 次执行时间

#### 测试工具
- **正则表达式测试** - 实时匹配高亮，支持 g/i/m 标志

#### 图片工具
- **图片压缩** - 可调压缩质量，实时预览，支持下载

#### 🎯 招牌功能 — 在线简历制作
- 可视化编辑器，支持上下/左右两种布局
- 模块化管理：个人优势、技能特长、工作经历、项目经验、教育背景、自定义模块
- 富文本编辑：加粗、斜体、下划线、删除线、字号、颜色、对齐、缩进、列表
- 拖拽排序模块和内容项
- 数据自动保存至浏览器本地（localStorage）
- 导出 JSON / 导入 JSON
- 导出 PDF（打印方式）
- 通过后端 API 保存简历，支持分享链接和克隆

#### 运维管理面板
- 管理员登录（JWT 认证 + bcrypt 密码哈希）
- 服务器监控：CPU 使用率、内存使用、磁盘使用、运行时间
- 工具使用统计
- 容器管理（Docker API）
- 服务状态检测
- 日志查看
- 告警通知：Prometheus 告警规则 → Alertmanager 分级路由 → 钉钉 Webhook 推送

### 🛠️ 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | Vue 3 + Vue Router + Pinia + Element Plus + Vite |
| 后端 | FastAPI + Uvicorn + Pydantic + aiosqlite |
| 数据库 | SQLite |
| 部署 | Docker + Docker Compose + Kubernetes (K3s) + Helm |
| 监控 | Prometheus + Grafana + Loki + Alertmanager |
| CI/CD | GitHub Actions |

### 🚀 快速开始

#### Docker Compose 一键启动

```bash
# 克隆项目
git clone https://github.com/liujinhao333/karins-toolbox.git
cd karins-toolbox/toolbox

# 设置环境变量
export SECRET_KEY="your-secret-key"
export ADMIN_PASSWORD_HASH="$(python -c "import bcrypt; print(bcrypt.hashpw(b'your-password', bcrypt.gensalt()).decode())")"

# 启动
docker-compose up -d
```

访问 http://localhost:3000

#### 本地开发

**启动后端：**
```bash
cd toolbox/backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
export SECRET_KEY="your-secret-key"
export ADMIN_PASSWORD_HASH="..."
uvicorn main:app --reload --port 8000
```

**启动前端：**
```bash
cd toolbox/web
npm install
npm run dev
```

### 📖 文档

- [部署指南](toolbox/DEPLOY.md)
- [启动文档](toolbox/STARTUP.md)

### 🔒 安全特性

- JWT 认证 + bcrypt 密码哈希
- XSS 防护
- ReDoS 防护（正则表达式 3 秒超时）
- CORS 限制
- 简历 edit_token 访问控制

---

## English

### ✨ Features

#### Conversion Tools
- **JSON/YAML Converter** - Bidirectional conversion with formatting
- **Timestamp Converter** - Timestamp to datetime conversion with real-time display
- **Base64 Encoder/Decoder** - Text encoding/decoding, image to Base64, Base64 to image

#### Generation Tools
- **UUID Generator** - Batch generate UUID v4
- **Hash Generator** - MD5 / SHA-1 / SHA-256 / SHA-512 hash calculation
- **Password Generator** - Configurable length, character types, strength evaluation
- **QR Code Generator** - Generate QR codes from text/URL with download support
- **Cron Expression Parser** - Visual Cron configuration, parse next 5 execution times

#### Testing Tools
- **Regex Tester** - Real-time matching highlight with g/i/m flags

#### Image Tools
- **Image Compressor** - Adjustable compression quality, real-time preview, download support

#### 🎯 Highlight Feature — Online Resume Builder
- Visual editor with top/bottom and left/right layouts
- Modular management: Summary, Skills, Experience, Projects, Education, Custom modules
- Rich text editing: Bold, italic, underline, strikethrough, font size, color, alignment, indentation, lists
- Drag-and-drop sorting for modules and items
- Auto-save to browser localStorage
- Export/Import JSON
- Export PDF (print mode)
- Backend API for resume saving, sharing links, and cloning

#### Admin Panel
- Admin login (JWT + bcrypt password hashing)
- Server monitoring: CPU, memory, disk usage, uptime
- Tool usage statistics
- Container management (Docker API)
- Service status detection
- Log viewing
- Alert notifications: Prometheus → Alertmanager → DingTalk Webhook

### 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Vue 3 + Vue Router + Pinia + Element Plus + Vite |
| Backend | FastAPI + Uvicorn + Pydantic + aiosqlite |
| Database | SQLite |
| Deployment | Docker + Docker Compose + Kubernetes (K3s) + Helm |
| Monitoring | Prometheus + Grafana + Loki + Alertmanager |
| CI/CD | GitHub Actions |

### 🚀 Quick Start

#### Docker Compose

```bash
# Clone
git clone https://github.com/liujinhao333/karins-toolbox.git
cd karins-toolbox/toolbox

# Set environment variables
export SECRET_KEY="your-secret-key"
export ADMIN_PASSWORD_HASH="$(python -c "import bcrypt; print(bcrypt.hashpw(b'your-password', bcrypt.gensalt()).decode())")"

# Start
docker-compose up -d
```

Visit http://localhost:3000

#### Local Development

**Backend:**
```bash
cd toolbox/backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
export SECRET_KEY="your-secret-key"
export ADMIN_PASSWORD_HASH="..."
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd toolbox/web
npm install
npm run dev
```

### 📖 Documentation

- [Deployment Guide](toolbox/DEPLOY.md)
- [Startup Guide](toolbox/STARTUP.md)

### 🔒 Security Features

- JWT authentication + bcrypt password hashing
- XSS protection
- ReDoS protection (3-second regex timeout)
- CORS restrictions
- Resume edit_token access control

---

## 📄 License

[MIT](LICENSE)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⭐ Star History

If you find this project useful, please give it a star! ⭐

---

<p align="center">Made with ❤️ by <a href="https://github.com/liujinhao333">liujinhao333</a></p>
