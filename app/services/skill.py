from fastapi import HTTPException, status

from app.models.skill import Skill
from app.repositories.skill import SkillRepository
from app.schemas.skill import SkillCreate


class SkillService:
    def __init__(self, repository: SkillRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, skill_id: int):
        skill = self.repository.get_by_id(skill_id)

        if skill is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Skill not found",
            )

        return skill

    def create(self, skill_data: SkillCreate):
        skill = Skill(
            **skill_data.model_dump()
        )

        return self.repository.create(skill)

    def update(
        self,
        skill_id: int,
        skill_data: SkillCreate,
    ):
        skill = self.get_by_id(skill_id)

        for field, value in skill_data.model_dump().items():
            setattr(skill, field, value)

        return self.repository.update(skill)

    def delete(self, skill_id: int):
        skill = self.get_by_id(skill_id)

        self.repository.delete(skill)