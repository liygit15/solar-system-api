from flask import abort, Blueprint, make_response, request, Response
from app.models.planet import Planet
from app.models.moon import Moon
from ..db import db
from .routes_utilities import validate_model, create_model, get_models_with_filters


bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()

    return create_model(Planet, request_body)


@bp.post("/<planet_id>/moons")
def create_moon_with_planet_id(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()
    request_body["planet_id"] = planet.id

    return create_model(Moon, request_body)

    # try:
    #     new_moon = Moon.from_dict(request_body)
    # except KeyError as error:
    #     return {"Message": f"Invalid request: missing {error.args[0]}"}, 400
        
    # db.session.add(new_moon)
    # db.session.commit()

    # return new_moon.to_dict(), 201


@bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)


@bp.get("/<id>")
def get_one_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()

@bp.get("/<id>/moons")
def get_all_planet_moons(id):
    planet = validate_model(Planet, id)
    moons = [moon.to_dict() for moon in planet.moons]

    return moons


@bp.put("/<id>")
def replace_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.star = request_body["star"]

    db.session.commit()
    return Response(status=204, mimetype="application/json")



@bp.delete("/<id>")
def delete_planet(id):
    planet = validate_model(Planet, id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")




# @planet_bp.get("")
# def get_all_planet():
#     result = []
    # for planet in planets:
    #     result.append(
    #         {
    #             "id": planet.id,
    #             "name":planet.name,
    #             "description":planet.description,
    #             "star":planet.star
    #         }
    #     )

    # for planet in planets:
    #     result.append(dict(
    #         id=planet.id,
    #         name=planet.name,
    #         description=planet.description,
    #         star=planet.star
    #     ))
    
    # return result