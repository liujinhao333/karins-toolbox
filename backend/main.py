import os
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api import tools, admin, resume
from app.core.database import init_db, close_connection
from app.core.logging_config import setup_logging, get_access_logger

# 初始化日志配置
setup_logging()
logger = get_access_logger()

CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_connection()

app = FastAPI(title="Karin的百宝箱 API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tools.router, prefix="/api/tools", tags=["工具"])
app.include_router(resume.router, prefix="/api", tags=["简历"])
app.include_router(admin.router, prefix="/api/admin", tags=["管理"])


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """记录所有HTTP请求"""
    start_time = time.time()
    
    # 获取客户端IP
    client_ip = request.client.host if request.client else "unknown"
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        client_ip = forwarded.split(",")[0].strip()
    
    # 处理请求
    response = await call_next(request)
    
    # 计算处理时间
    process_time = time.time() - start_time
    
    # 记录访问日志
    logger.info(
        f"{client_ip} | {request.method} {request.url.path} | "
        f"{response.status_code} | {process_time:.3f}s"
    )
    
    return response


@app.get("/api/health")
async def health():
    return {"status": "ok"}
