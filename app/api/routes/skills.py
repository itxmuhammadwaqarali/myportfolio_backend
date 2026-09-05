from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_skill_service
from app.schemas.skill import SkillCreate, SkillResponse
from app.services.skill import SkillService


router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
)


@router.get(
    "/",
    response_model=list[SkillResponse],
)
def get_skills(
    service: SkillService = Depends(get_skill_service),
):
    return service.get_all()


@router.get(
    "/{skill_id}",
    response_model=SkillResponse,
)
def get_skill(
    skill_id: int,
    service: SkillService = Depends(get_skill_service),
):
    return service.get_by_id(skill_id)


@router.post(
    "/",
    response_model=SkillResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_skill(
    skill_data: SkillCreate,
    service: SkillService = Depends(get_skill_service),
):
    return service.create(skill_data)


@router.put(
    "/{skill_id}",
    response_model=SkillResponse,
)
def update_skill(
    skill_id: int,
    skill_data: SkillCreate,
    service: SkillService = Depends(get_skill_service),
):
    return service.update(
        skill_id,
        skill_data,
    )


@router.delete(
    "/{skill_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_skill(
    skill_id: int,
    service: SkillService = Depends(get_skill_service),
):
    service.delete(skill_id)