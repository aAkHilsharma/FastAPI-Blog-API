from fastapi import FastAPI

from .routers.blogs import router as blogs_router

app = FastAPI()

app.include_router(blogs_router.router)
