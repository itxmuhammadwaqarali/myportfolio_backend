from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.repositories.project import ProjectRepository
from app.services.project import ProjectService


def get_project_service(
    db: Session = Depends(get_db),
):
    repository = ProjectRepository(db)

    return ProjectService(repository)