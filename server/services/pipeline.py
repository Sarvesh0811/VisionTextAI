from services.ocr import run_ocr
from services.optimization import optimize_text
from services.translation import translate_text


def process_ocr_pipeline(file_bytes):

    raw = run_ocr(file_bytes)
    optimized = optimize_text(raw)
    english = translate_text(optimized)

    return {
        "raw_ocr": raw,
        "final_ocr": optimized,
        "english_translation": english
    }
