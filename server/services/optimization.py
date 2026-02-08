import logging
from openai import OpenAI
from core.config import settings

logger = logging.getLogger("ocr_logger")
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def optimize_text(text: str):

    try:
        correction_prompt = f"""
        You are correcting OCR text.

        Rules:
        - Do NOT add new words.
        - Do NOT remove words.
        - Do NOT reorder words.
        - ONLY fix spelling and character mistakes.
        - Keep word count identical.

        Return corrected text only.

        Text:
        {text}
        """

        corrected = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": correction_prompt}],
            max_tokens=500
        ).choices[0].message.content

        cleanup_prompt = f"""
        Format the following text with proper line breaks and spacing.
        Do NOT change any words.
        Return plain text only.

        Text:
        {corrected}
        """

        final_text = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": cleanup_prompt}],
            max_tokens=300
        ).choices[0].message.content

        logger.info("Text optimization successful")
        return final_text

    except Exception as e:
        logger.error(f"Optimization failed: {e}")
        raise
