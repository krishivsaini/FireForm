from pydantic import BaseModel

class TemplateCreate(BaseModel):
    pdf_path: str
    fields: list