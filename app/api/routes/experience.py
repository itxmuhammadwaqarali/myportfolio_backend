from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.experience import Experience
from app.schemas.experience import (
    ExperienceCreate,
    ExperienceResponse,
)


router = APIRouter(
    prefix="/experience",
    tags=["Experience"],
)


@router.get(
    "/",
    response_model=list[ExperienceResponse],
)
def get_experience(
    db: Session = Depends(get_db),
):
    statement = select(Experience).order_by(
        Experience.start_date.desc()
    )

    result = db.execute(statement)

    return result.scalars().all()


@router.post(
    "/",
    response_model=ExperienceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_experience(
    experience_data: ExperienceCreate,
    db: Session = Depends(get_db),
):
    experience = Experience(
        **experience_data.model_dump()
    )

    db.add(experience)
    db.commit()
    db.refresh(experience)

    return experience