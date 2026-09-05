from fastapi import HTTPException, status

from app.models.project import Project
from app.repositories.project import ProjectRepository
from app.schemas.project import ProjectCreate


class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, project_id: int):
        project = self.repository.get_by_id(project_id)

        if project is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found",
            )

        return project

    def create(self, project_data: ProjectCreate):
        project = Project(
            **project_data.model_dump()
        )

        return self.repository.create(project)

    def update(
        self,
        project_id: int,
        project_data: ProjectCreate,
    ):
        project = self.get_by_id(project_id)

        for field, value in project_data.model_dump().items():
            setattr(project, field, value)

        return self.repository.update(project)

    def delete(self, project_id: int):
        project = self.get_by_id(project_id)

        self.repository.delete(project)