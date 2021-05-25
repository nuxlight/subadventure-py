from fastapi import APIRouter

router = APIRouter(prefix="/user")


@router.get("/sample")
async def getSample():
    return {
        "test_sample": True
    }
