from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, ForeignKey, LargeBinary
from sqlalchemy.dialects.postgresql import UUID

from app.configs.database import db


@dataclass
class TattooImage(db.Model):

    id: str
    id_tattoo: str

    __tablename__ = "tattoo_images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    image = Column(LargeBinary)
    id_tattoo = Column(UUID(as_uuid=True), ForeignKey("tattoos.id"))
