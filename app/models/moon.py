from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .planet import Planet

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    size: Mapped[str]
    description: Mapped[str]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size,
            "planet":self.planet.name if self.planet_id else None
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name = data["name"],
                description = data["description"],
                size = data["size"],
                planet_id = data.get("planet_id", None))