import os

import redis.asyncio as redis
import uvicorn
from fastapi import Depends, FastAPI

from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

app = FastAPI()


@app.on_event("startup")
async def startup():
    redis_connection = redis.from_url(os.environ.get("REDIS_URL"), encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_connection)


@app.get("/", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def index() -> dict:
    return {"msg": "Hello Worlds"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
