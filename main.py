import os
import logging

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.security.api_key import APIKeyHeader
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
api_key_header = APIKeyHeader(name="X-API-Key")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


import h3
from fastapi import Query, HTTPException

from pydantic import BaseModel

class GeoIndexRequest(BaseModel):
    longitude: float
    latitude: float
    resolution: int

@app.post("/geoindex")
def geoindex(request: GeoIndexRequest, api_key: str = Depends(api_key_header)):
    # Validate API key
    if api_key != os.environ.get("API_KEY"):
        raise HTTPException(status_code=403, detail="Invalid API Key")
    # Validate resolution
    if not (0 <= request.resolution <= 15):
        raise HTTPException(status_code=400, detail="Resolution must be between 0 and 15")
    # Calculate H3 cell index
    h3_index = h3.geo_to_h3(request.latitude, request.longitude, request.resolution)
    return {"h3Index": h3_index}


# Do not remove the main function while updating the app.
if __name__ == "__main__":
    import uvicorn

    # This initialization is essential and must not be removed.
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
