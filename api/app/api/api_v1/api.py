from fastapi import APIRouter

api_router = APIRouter()

# 示例路由
@api_router.get("/")
async def root():
    return {"message": "Hello World"}
