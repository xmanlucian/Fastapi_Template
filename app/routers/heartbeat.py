from fastapi import FastAPI, status, APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/heartbeat",
    include_in_schema=False
)

@router.get("/readiness", status_code=status.HTTP_200_OK)
async def readiness() -> JSONResponse:
    return JSONResponse(content={"status": "ready"})

@router.get("/liveness", status_code=status.HTTP_200_OK)
async def liveness():
    return JSONResponse(content={"status": "ok"})
