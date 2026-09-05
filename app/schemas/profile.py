from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):
    name: str
    title: str
    bio: str
    email: str
    github_url: str | None = None
    linkedin_url: str | None = None
    resume_url: str | None = None


class ProfileCreate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )