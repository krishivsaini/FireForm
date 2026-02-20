from fastapi import APIRouter
from api.schemas.forms import FormFill
# from src.fill_document import name_of_function_that_fills_document

router = APIRouter(prefix="/forms", tags=["forms"])


@router.post("/fill")
def fill_form(form_fill: FormFill):
    return
    # return name_of_function_that_fills_document()