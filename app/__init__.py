from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routes.v1 import v1_router

load_dotenv()

app_description = """
Unofficial User API for Genshin Impact

API for in-game user status, characters information, and more.

[GitHub](https://github.com/331leo/GenshinAPI)
[Swagger Docs](/docs/swagger)
[ReDoc Docs](/docs/redoc)
"""

app_config = {
    "title": "GenshinAPI",
    "description": app_description,
    "version": "0.0.1",
    "redoc_url": "/docs/redoc",
    "docs_url": "/docs/swagger",
}

app = FastAPI(**app_config)


@app.get("/", include_in_schema=False)
async def route_root():
    return RedirectResponse(url="/docs/redoc")


app.include_router(v1_router, prefix="/v1")
