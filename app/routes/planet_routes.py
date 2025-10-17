from flask import Blueprint
from app.models.planet import planets


planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planet():
    result = []
    for planet in planets:
        result.append(
            {
                "id": planet.id,
                "name":planet.name,
                "description":planet.description,
                "moon":planet.moon
            }
        )
    
    return result