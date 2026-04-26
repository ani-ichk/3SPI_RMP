from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root(name='World'):
    return {
        'message': f'Hello {name}',
        'docs': '/docs'
    }