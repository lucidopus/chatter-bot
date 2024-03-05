import os

import uvicorn
from fastapi import FastAPI, HTTPException, Request, Security, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.security import APIKeyHeader

from utils.config import API_KEY
from utils.constants import API_NAME
from utils.models import MessageRequest
from utils.enums import HttpStatusCode
from pipelines import get_model_response

app = FastAPI(
    title=API_NAME,
    description="AI Powered chat-bot.",
    version="0.1.0",
    openapi_tags=[
        {
            "name": API_NAME,
            "description": f"Endpoints for {API_NAME}",
        },
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="static")


api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header:
        if api_key_header == API_KEY:
            return API_KEY
        else:
            raise HTTPException(
                status_code=HttpStatusCode.UNAUTHORIZED.value, detail="Invalid API Key"
            )
    else:
        raise HTTPException(
            status_code=HttpStatusCode.BAD_REQUEST.value,
            detail="Please enter an API key",
        )


@app.get("/", tags=["Index"], response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/robots.txt", include_in_schema=False)
async def get_robots_txt():
    robots_txt_path = os.path.join("static", "robots.txt")
    return FileResponse(robots_txt_path, media_type="text/plain")


@app.post(
    path="/get_response",
    tags=["Model Interactions"],
    response_model=str,
    response_description="Model Response",
    description="Get smart responses from an LLM.",
    name=API_NAME,
)
async def process(messageRequest: MessageRequest, api_key: str = Depends(get_api_key)):

    response = get_model_response(request=messageRequest)

    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, workers=4)
