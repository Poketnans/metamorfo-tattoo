from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, Date, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class Storage(db.Model):

    id: str
    name: str
    quantity: int
    description: str
    validity: str

    __tablename__ = "storage"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    description = Column(Text, default="no description")
    validity = Column(Date)
