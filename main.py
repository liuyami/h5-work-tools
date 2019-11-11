from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI(
    title="语铄内部工具箱",
    description="持续更新中...",
    version="0.1",
)

# 静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")


