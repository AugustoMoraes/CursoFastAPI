from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/cursos')
async def get_usuarios():
    return {"info": "Todos os usuários"}