from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
from datetime import datetime, timezone
import logging
import os
import uvicorn

# --------------------------
# Basic logging setup
# --------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hng-stage0")

# --------------------------
# FastAPI app
# --------------------------
app = FastAPI(title="HNG Stage 0 - Profile Endpoint")

# Allow CORS (for public API calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use specific domains in production
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# --------------------------
# Configuration
# --------------------------
USER_EMAIL = os.getenv("HNG_EMAIL", "stdave001@gmail.com")
USER_NAME = os.getenv("HNG_NAME", "Ibukun Babatunde")
USER_STACK = os.getenv("HNG_STACK", "Python/FastAPI")

CATFACT_URL = "https://catfact.ninja/fact"
CATFACT_TIMEOUT = 5  # seconds
FALLBACK_FACT = "Could not fetch cat fact right now."

# --------------------------
# Endpoint: /me
# --------------------------
@app.get("/me", tags=["Profile"])
def get_profile():
    """Return profile info + dynamic cat fact + current UTC timestamp."""
    cat_fact = FALLBACK_FACT

    try:
        logger.info("Fetching cat fact from %s", CATFACT_URL)
        resp = requests.get(CATFACT_URL, timeout=CATFACT_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        cat_fact = data.get("fact") or FALLBACK_FACT
    except requests.RequestException as e:
        logger.warning("Cat fact fetch failed: %s", e)

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

    return JSONResponse(status_code=status.HTTP_200_OK, content=payload)

# --------------------------
# Local / Railway entrypoint
# --------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Railway provides PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port)
