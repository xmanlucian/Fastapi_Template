from app.config import config
from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from app.config.config import config

__all__ = ["create_app"]

try:
    from app.routers import routers
except ImportError:
    routers = []

def create_app() -> FastAPI:

    async def app_startup(application: FastAPI) -> None:
        print("App starting up")

    async def app_shutdown(application: FastAPI) -> None:
        print("App shutting down")

    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncGenerator:
        await app_startup(application)
        yield
        await app_shutdown(application)

    app: FastAPI = FastAPI(
        title=config.app.title,
        description=config.app.description,
        version=config.app.version,
        lifespan=lifespan,
    )

    for router in routers:
        app.include_router(router)

    return app