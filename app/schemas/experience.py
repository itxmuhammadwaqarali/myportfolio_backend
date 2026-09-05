from datetime import date

from pydantic import BaseModel, ConfigDict


class ExperienceBase(BaseModel):
    company: str
    position: str
    location: str | None = None
    start_date: date
    end_date: date | None = None
    is_current: bool = False
    description: str


class ExperienceCreate(ExperienceBase):
    pass


class ExperienceResponse(ExperienceBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )