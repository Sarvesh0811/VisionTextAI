from fastapi import APIRouter, File, UploadFile
from schemas.ocr import OCRResponse
from services.pipeline import process_ocr_pipeline

ocr_router = APIRouter()

@ocr_router.post("/ocr", response_model=OCRResponse, tags=["OCR"])
async def run_ocr(file: UploadFile = File(...)):
    file_bytes = await file.read()
    return process_ocr_pipeline(file_bytes)
