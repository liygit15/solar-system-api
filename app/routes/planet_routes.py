from flask import abort, Blueprint, make_response
from app.models.planet import planets


planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planet():
    result = []
    # for planet in planets:
    #     result.append(
    #         {
    #             "id": planet.id,
    #             "name":planet.name,
    #             "description":planet.description,
    #             "moon":planet.moon
    #         }
    #     )

    for planet in planets:
        result.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            moon=planet.moon
        ))
    
    return result


@planet_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_planet(id)
    planet_dict = dict(
        id=planet.id,
        name=planet.name,
        description=planet.description,
        moon=planet.moon
    )

    return planet_dict


def validate_planet(id):
    try:
        id = int(id)
    except ValueError:
        invalid_planet = {"message": f"The id ({id}) is invalid."}
        abort(make_response(invalid_planet, 400))
    
    for planet in planets:
        if planet.id == id:
            return planet
    
    not_found = {"message": f"Planet with id ({id}) is not found"}    
    abort(make_response(not_found, 404))
        