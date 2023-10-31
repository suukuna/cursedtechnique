from fastapi import APIRouter
router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/register')
async def register(auth_details: AuthDetails) -> dict:
    return
