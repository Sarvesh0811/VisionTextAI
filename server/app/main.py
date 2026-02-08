import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.v1.ocr import ocr_router
from app.exception_handlers import global_exception_handler

app = FastAPI(title="OCR System", version="1.0")

# LOGGING
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# EXCEPTION HANDLER
app.add_exception_handler(Exception, global_exception_handler)

# ROUTERS 
app.include_router(ocr_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"status": "Running"}
