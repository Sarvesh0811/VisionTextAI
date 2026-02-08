import logging
from openai import OpenAI
from core.config import settings

logger = logging.getLogger("ocr_logger")
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def translate_text(text: str):

    try:
        prompt = f"""
        Translate the following text into English.
        Preserve meaning.
        Return plain English only.

        Text:
        {text}
        """

        result = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400
        ).choices[0].message.content

        logger.info("Translation successful")
        return result

    except Exception as e:
        logger.error(f"Translation failed: {e}")
        raise
