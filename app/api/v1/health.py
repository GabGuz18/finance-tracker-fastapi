from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(prefix='/health')


@router.get('/')
async def healthcheck():
    return {
        'status': 'ok',
        'app_name': settings.app_name,
        'environment': settings.environment,
    }
