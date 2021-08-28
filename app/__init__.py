from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

load_dotenv()

app_config = {
    "title": "GenshinAPI",
    "description": "Unofficial API for Genshin Impact",
    "version": "0.0.1",
    "redoc_url": "/v1/docs"
}

app = FastAPI(**app_config)

@app.get("/")
async def route_root():
    return RedirectResponse(url="/v1/docs")

# app.include_router(api_router, prefix="/v1")