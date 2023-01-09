import requests
import os

from django.core.files import File

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

OCR_API_TOKEN_HEADER=os.getenv("OCR_API_TOKEN_HEADER")
OCR_API_ENDPOINT=os.getenv("OCR_API_ENDPOINT")

def extract_text_via_ocr_service(file_obj: File=None):
    data = {}
    if OCR_API_ENDPOINT is None:
        return data
    if OCR_API_TOKEN_HEADER is None:
        return data
    if file_obj is None:
        return data
    # get image
    # send image through HTTP POST
    # return dict {}
    headers={
        "Authorization": f"Bearer {OCR_API_TOKEN_HEADER}"
    }
    with file_obj.open('rb') as f:
        r = requests.post(OCR_API_ENDPOINT, files={"file": f}, headers=headers)
        if r.status_code in range(200, 299):
            if r.headers.get("content-type") == 'application/json':
                data = r.json()
    return data
