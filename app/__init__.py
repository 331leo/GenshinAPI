from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.v1 import v1_router, rate_limiter
load_dotenv()

app_config = {
    "title": "GenshinAPI",
    "description": "Unofficial API for Genshin Impact",
    "version": "0.0.1",
    "redoc_url": "/v1/docs",
}

app = FastAPI(**app_config)

app.state.limiter = rate_limiter

@app.get("/")
async def route_root():
    return RedirectResponse(url="/v1/docs")


app.include_router(v1_router, prefix="/v1")
