from flask import abort, Blueprint, make_response, request, Response
from app.models.planet import Planet
from ..db import db


planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    moon = request_body["moon"]

    new_planet = Planet(
        name=name,
        description=description,
        moon=moon
    )

    db.session.add(new_planet)
    db.session.commit()

    planet_response = dict(
        id=new_planet.id,
        name=new_planet.name,
        description=new_planet.description,
        moon=new_planet.moon
    )

    return planet_response, 201

@planet_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    result_list = []

    for planet in planets:
        result_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            moon=planet.moon
        ))

    return result_list


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
    
    query = db.select(Planet).where(Planet.id == id)
    planet = db.session.scalar(query)

    if not planet:
        not_found = {"message": f"Planet with id ({id}) is not found"}    
        abort(make_response(not_found, 404))
        
    return planet



@planet_bp.put("/<id>")
def replace_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moon = request_body["moon"]
    db.session.commit()
    return Response(status=204, mimetype="application/json")



@planet_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_planet(id)
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
    #             "moon":planet.moon
    #         }
    #     )

    # for planet in planets:
    #     result.append(dict(
    #         id=planet.id,
    #         name=planet.name,
    #         description=planet.description,
    #         moon=planet.moon
    #     ))
    
    # return result