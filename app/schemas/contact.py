from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict


class ContactCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=150,
    )

    email: EmailStr

    subject: str = Field(
        min_length=3,
        max_length=255,
    )

    message: str = Field(
        min_length=10,
        max_length=5000,
    )


class ContactResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    subject: str
    message: str
    is_read: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )