from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime, timezone
import logging
import os

# Basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hng-stage0")

app = FastAPI(title="HNG Stage0 - Profile Endpoint")

# Add CORS if you plan to call from a browser (adjust allowed origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to specific domains in production
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Config (use env var for email/name/stack if you like)
USER_EMAIL = os.getenv("HNG_EMAIL", "stdave001@gmail.com")
USER_NAME = os.getenv("HNG_NAME", "Ibukun Babatunde")
USER_STACK = os.getenv("HNG_STACK", "Python/FastAPI")
CATFACT_URL = "https://catfact.ninja/fact"
CATFACT_TIMEOUT = 5  # seconds
FALLBACK_FACT = "Could not fetch cat fact right now."

@app.get("/me")
def get_profile():
    """Return profile info + dynamic cat fact + current UTC timestamp."""
    cat_fact = FALLBACK_FACT
    try:
        logger.info("Requesting cat fact from %s", CATFACT_URL)
        resp = requests.get(CATFACT_URL, timeout=CATFACT_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        # Cat fact API returns {"fact": "...", "length": N}
        cat_fact = data.get("fact") or FALLBACK_FACT
    except requests.RequestException as e:
        logger.warning("Failed to fetch cat fact: %s", e)

    # Current UTC timestamp in ISO 8601 format with Z
    timestamp = datetime.now(timezone.utc).isoformat()

    payload = {
        "status": "success",
        "user": {
            "email": USER_EMAIL,
            "name": USER_NAME,
            "stack": USER_STACK
        },
        "timestamp": timestamp,
        "fact": cat_fact
    }

    # Return JSON with application/json content-type
    return JSONResponse(status_code=status.HTTP_200_OK, content=payload)
