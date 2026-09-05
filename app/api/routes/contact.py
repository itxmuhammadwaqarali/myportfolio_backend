from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.contact import ContactMessage
from app.schemas.contact import (
    ContactCreate,
    ContactResponse,
)


router = APIRouter(
    prefix="/contact",
    tags=["Contact"],
)


@router.post(
    "/",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_contact_message(
    contact_data: ContactCreate,
    db: Session = Depends(get_db),
):
    contact_message = ContactMessage(
        **contact_data.model_dump()
    )

    db.add(contact_message)
    db.commit()
    db.refresh(contact_message)

    return contact_message


@router.get(
    "/",
    response_model=list[ContactResponse],
)
def get_contact_messages(
    db: Session = Depends(get_db),
):
    statement = select(ContactMessage).order_by(
        ContactMessage.created_at.desc()
    )

    result = db.execute(statement)

    return result.scalars().all()