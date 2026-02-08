import base64
import logging
from openai import OpenAI
from core.config import settings

logger = logging.getLogger("ocr_logger")
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def run_ocr(file_bytes: bytes):

    try:
        image_base64 = base64.b64encode(file_bytes).decode()

        prompt = """
        Extract all readable text from this image.
        Preserve original language.
        Return plain text only.
        """

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=800
        )

        logger.info("OCR extraction successful")

        return response.choices[0].message.content

    except Exception as e:
        logger.error(f"OCR failed: {e}")
        raise
