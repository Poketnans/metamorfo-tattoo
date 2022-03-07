from http import HTTPStatus

import werkzeug.exceptions
from flask import request
from flask_jwt_extended import create_access_token

from app.errors import FieldMissingError
from app.models.clients_model import Client
from app.decorators.verify_payload import verify_payload


@verify_payload(
    fields_and_types = {
        "email":str,
        "password":str
        },
    optional=[])
def post_login(payload):
    data = request.get_json()
    try:
        if data == None:
            raise FieldMissingError(description={"msg": "the body was empty"})

        user = Client.query.filter_by(email=data["email"]).first_or_404(
            description={"msg": "user not found"})

        if not user.verify_password(data["password"]):
            return {"msg": "wrong password"}, HTTPStatus.FORBIDDEN

        token = create_access_token(
            identity={"id": user.id})

        return {"access token": token}
    except werkzeug.exceptions.NotFound as e:
        return e.description, HTTPStatus.NOT_FOUND
    except FieldMissingError as e:
        return e.description, HTTPStatus.BAD_REQUEST
