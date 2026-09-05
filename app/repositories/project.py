from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        statement = (
            select(Project)
            .order_by(Project.created_at.desc())
        )

        return self.db.execute(statement).scalars().all()

    def get_by_id(self, project_id: int):
        statement = select(Project).where(
            Project.id == project_id
        )

        return self.db.execute(statement).scalar_one_or_none()

    def create(self, project: Project):
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def update(self, project: Project):
        self.db.commit()
        self.db.refresh(project)

        return project

    def delete(self, project: Project):
        self.db.delete(project)
        self.db.commit()