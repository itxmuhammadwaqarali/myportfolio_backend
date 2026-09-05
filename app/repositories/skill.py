from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.skill import Skill


class SkillRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        statement = (
            select(Skill)
            .order_by(Skill.category, Skill.name)
        )

        return self.db.execute(statement).scalars().all()

    def get_by_id(self, skill_id: int):
        statement = select(Skill).where(
            Skill.id == skill_id
        )

        return self.db.execute(statement).scalar_one_or_none()

    def create(self, skill: Skill):
        self.db.add(skill)
        self.db.commit()
        self.db.refresh(skill)

        return skill

    def update(self, skill: Skill):
        self.db.commit()
        self.db.refresh(skill)

        return skill

    def delete(self, skill: Skill):
        self.db.delete(skill)
        self.db.commit()