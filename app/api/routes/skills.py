from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillResponse


router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
)


@router.get(
    "/",
    response_model=list[SkillResponse],
)
def get_skills(
    db: Session = Depends(get_db),
):
    statement = select(Skill).order_by(
        Skill.category,
        Skill.name,
    )

    result = db.execute(statement)

    return result.scalars().all()


@router.post(
    "/",
    response_model=SkillResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_skill(
    skill_data: SkillCreate,
    db: Session = Depends(get_db),
):
    skill = Skill(
        **skill_data.model_dump()
    )

    db.add(skill)
    db.commit()
    db.refresh(skill)

    return skill