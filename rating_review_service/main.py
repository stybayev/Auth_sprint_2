from fastapi.responses import ORJSONResponse
from fastapi import FastAPI
from contextlib import asynccontextmanager

from rating_review_service.api.v1 import likes, review
from rating_review_service.core.config import settings
from rating_review_service.db.mongo import shard_collections
from rating_review_service.utils.enums import ShardedCollections
from rating_review_service.utils.wait_for_mongo_ready import wait_for_mongo_ready


@asynccontextmanager
async def lifespan(_: FastAPI):
    await wait_for_mongo_ready(settings.db.url)
    await shard_collections(ShardedCollections)

    yield


app = FastAPI(
    title=settings.project_name,
    docs_url="/api/rating/openapi",
    openapi_url="/api/rating/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan
)

app.include_router(likes.router, prefix="/api/v1/likes", tags=["likes"])
app.include_router(review.router, prefix="/api/v1/reviews", tags=["reviews"])
