from PIL import Image
from io import BytesIO
import requests
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os
from google.api_core import retry


is_retriable = lambda e: (isinstance(e, genai.errors.APIError) and e.code in {429, 503})

# Automatically retry generate_content on transient Gemini API errors (rate limiting or downtime)
genai.models.Models.generate_content = retry.Retry(predicate=is_retriable)(
    genai.models.Models.generate_content
)

load_dotenv()  # Automatically loads variables from .env

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise EnvironmentError("Missing GOOGLE_API_KEY in environment variables.")


def get_client():
    client = genai.Client(api_key=GOOGLE_API_KEY)
    return client


def get_image(url):
    """
    Given a url, return the PIL image
    """
    try:
        response = requests.get(url, stream=True, timeout=10)
        if 200 <= response.status_code < 300:
            return Image.open(BytesIO(response.content)).convert("RGB")
        else:
            print(f"Request failed with code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def get_product_description(prompt, image, client):
    """
    Request the client to generate content based on a prompt and an image.
    The output is a structured JSON document.
    """

    class ProductTitles(BaseModel):
        gen_z: str
        millennials: str
        seo_optimized: str

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt, image],
        config={
            "response_mime_type": "application/json",
            "response_schema": list[ProductTitles],
        },
    )
    return response
