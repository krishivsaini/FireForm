from pydantic import BaseModel

class FormFill(BaseModel):
    template_id: str
    input_text: str