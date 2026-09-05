from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_project_service
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project import ProjectService


router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get(
    "/",
    response_model=list[ProjectResponse],
)
def get_projects(
    service: ProjectService = Depends(get_project_service),
):
    return service.get_all()


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_project(
    project_id: int,
    service: ProjectService = Depends(get_project_service),
):
    return service.get_by_id(project_id)


@router.post(
    "/",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_project(
    project_data: ProjectCreate,
    service: ProjectService = Depends(get_project_service),
):
    return service.create(project_data)


@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
)
def update_project(
    project_id: int,
    project_data: ProjectCreate,
    service: ProjectService = Depends(get_project_service),
):
    return service.update(
        project_id,
        project_data,
    )


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_project(
    project_id: int,
    service: ProjectService = Depends(get_project_service),
):
    service.delete(project_id)