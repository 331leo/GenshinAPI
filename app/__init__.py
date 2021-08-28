from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.v1 import v1_router

load_dotenv()

app_config = {
    "title": "GenshinAPI",
    "description": "Unofficial API for Genshin Impact",
    "version": "0.0.1",
    "redoc_url": "/docs/redoc",
    "docs_url": "/docs/swagger",
}

app = FastAPI(**app_config)


@app.get("/", include_in_schema=False)
async def route_root():
    return RedirectResponse(url="/docs/redoc")


app.include_router(v1_router, prefix="/v1")
