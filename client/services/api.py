import os
import requests
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")


def send_image(file):

    try:
        files = {"file": file}
        response = requests.post(BACKEND_URL, files=files, timeout=120)

        if response.status_code == 200:
            return {"success": True, "data": response.json()}
        else:
            return {
                "success": False,
                "error": response.text
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
