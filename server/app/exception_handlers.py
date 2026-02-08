import logging
from fastapi import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger("ocr_logger")

async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled Error: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
            "details": str(exc)
        }
    )
