from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.profile import Profile
from app.schemas.profile import (
    ProfileCreate,
    ProfileResponse,
)


router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


@router.get(
    "/",
    response_model=ProfileResponse,
)
def get_profile(
    db: Session = Depends(get_db),
):
    statement = select(Profile).limit(1)

    profile = db.execute(
        statement
    ).scalar_one_or_none()

    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found",
        )

    return profile


@router.post(
    "/",
    response_model=ProfileResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_db),
):
    existing_profile = db.execute(
        select(Profile)
    ).scalar_one_or_none()

    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Profile already exists",
        )

    profile = Profile(
        **profile_data.model_dump()
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile