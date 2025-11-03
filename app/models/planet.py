from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    moon: Mapped[str]
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "moon": self.moon
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name = data["name"],
                description = data["description"],
                moon = data["moon"])
        