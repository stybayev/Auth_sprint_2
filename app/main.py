from contextlib import asynccontextmanager

from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from redis.asyncio import Redis

from app.api.v1 import films, genres, persons
from app.core.config import settings
from app.core.middleware import before_request
from app.core.tracer import configure_tracer, init_tracer
from app.db import elastic, redis
from app.dependencies.main import setup_dependencies

from auth.core.jwt import JWTSettings
from fastapi_jwt_auth import AuthJWT

from auth.core.middleware import check_blacklist


@asynccontextmanager
async def lifespan(app: FastAPI):
    AuthJWT.load_config(lambda: JWTSettings())
    redis.redis = Redis(host=settings.redis_host, port=settings.redis_port)
    elastic.es = AsyncElasticsearch(
        hosts=[f'http://{settings.elastic_host}:{settings.elastic_port}']
    )

    yield

    await redis.redis.close()
    await elastic.es.close()


app = FastAPI(
    title=settings.project_name,
    docs_url="/api/films/openapi",
    openapi_url="/api/films/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan
)

init_tracer(app)
FastAPIInstrumentor.instrument_app(app)

app.middleware("http")(before_request)
app.middleware("http")(check_blacklist)

app.include_router(films.router, prefix="/api/v1/films", tags=["films"])
app.include_router(genres.router, prefix="/api/v1/genres", tags=["genres"])
app.include_router(persons.router, prefix="/api/v1/persons", tags=["persons"])

setup_dependencies(app)
