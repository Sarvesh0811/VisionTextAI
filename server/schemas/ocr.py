from pydantic import BaseModel

class OCRResponse(BaseModel):
    raw_ocr: str
    english_translation: str
