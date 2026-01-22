from fastapi import FastAPI
from hypercorn import Config
from hypercorn.asyncio import serve
import asyncio

from fastapi.middleware.cors import CORSMiddleware
from movie_explorer.api.v1.api_v1_router import api_v1_router

app = FastAPI()

# CORS middleware: allow all origins for development. Adjust in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1_router)

if __name__ == "__main__":
    config = Config()
    config.bind = ["0.0.0.0:8085"]
    asyncio.run(serve(app, config))