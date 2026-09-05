from fastapi import FastAPI

from app.api.routes.projects import router as project_router
from app.api.routes.skills import router as skill_router
from app.api.routes.experience import router as experience_router

from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)


app.include_router(
    project_router,
    prefix="/api",
)

app.include_router(
    skill_router,
    prefix="/api",
)

app.include_router(
    experience_router,
    prefix="/api",
)


@app.get("/")
def root():
    return {
        "message": "Waqar Portfolio API"
    }