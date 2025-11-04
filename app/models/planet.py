from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    star: Mapped[str]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")
    
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "star": self.star
        }

    @classmethod
    def from_dict(cls, data):
        return cls(name = data["name"],
                description = data["description"],
                star = data["star"])
        