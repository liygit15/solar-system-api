from flask import abort, Blueprint, make_response, request, Response
from app.models.planet import Planet
from ..db import db
from .routes_utilities import validate_model


bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()
    # name = request_body["name"]
    # description = request_body["description"]
    # moon = request_body["moon"]

    # new_planet = Planet(
    #     name=name,
    #     description=description,
    #     moon=moon
    # )
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    # planet_response = dict(
    #     id=new_planet.id,
    #     name=new_planet.name,
    #     description=new_planet.description,
    #     moon=new_planet.moon
    # )

    return make_response(new_planet.to_dict(), 201)

@bp.get("")
def get_all_planets():
    query = db.select(Planet)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    moon_param = request.args.get("moon")
    if moon_param:
        query = query.where(Planet.moon.ilike(f"%{moon_param}%"))


    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)
    result_list = []

    for planet in planets:
        result_list.append(planet.to_dict())

    return result_list


@bp.get("/<id>")
def get_one_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()




@bp.put("/<id>")
def replace_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moon = request_body["moon"]

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