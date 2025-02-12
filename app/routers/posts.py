from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/posts",
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_posts() -> JSONResponse:
    return JSONResponse(
        content={
            "posts": [
                {"title": "First Post", "content": "This is the first post."},
                {"title": "Second Post", "content": "This is the second post."},
            ]
        }
    )