from fastapi import APIRouter
from api.schemas.templates import TemplateCreate

router = APIRouter(prefix="/templates", tags=["templates"])

@router.post("/create")
def create(template: TemplateCreate):
    return
    # return create_template(template)