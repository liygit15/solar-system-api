from flask import abort, Blueprint, make_response, request, Response
from app.models.moon import Moon
from ..db import db
from .routes_utilities import validate_model, create_model, get_models_with_filters


bp = Blueprint("moons", __name__, url_prefix="/moons")

@bp.post("")
def create_moon():
    request_body = request.get_json()
    
    return create_model(Moon, request_body)

@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moon, request.args)
    # query = db.select(Moon)

    # description_param = request.args.get("description")
    # if description_param:
    #     query = query.where(Moon.description.ilike(f"%{description_param}%"))
    
    # name_param = request.args.get("name")
    # if name_param:
    #     query = query.where(Moon.name.ilike(f"%{name_param}%"))

    # size_param = request.args.get("size")
    # if size_param:
    #     query = query.where(Moon.name.ilike(f"%{size_param}%"))

    # query = query.order_by(Moon.id)
    # moons = db.session.scalars(query)
    # result_list = []

    # for moon in moons:
    #     result_list.append(moon.to_dict())

    # return result_list


@bp.get("/<id>")
def get_one_moon(id):
    moon = validate_model(Moon, id)

    return moon.to_dict()




@bp.put("/<id>")
def replace_planet(id):
    moon = validate_model(Moon, id)
    request_body = request.get_json()

    moon.name = request_body["name"]
    moon.description = request_body["description"]
    moon.size = request_body["size"]

    db.session.commit()
    return Response(status=204, mimetype="application/json")



@bp.delete("/<id>")
def delete_moon(id):
    moon = validate_model(Moon, id)
    db.session.delete(moon)
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