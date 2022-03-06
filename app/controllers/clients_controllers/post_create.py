from http import HTTPStatus

from flask import jsonify
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from app.classes.app_with_db import current_app
from app.models.clients_model import Client
from app.decorators import verify_payload


@verify_payload(
    optional=[
        "general_information",
        "image_name",
        "image_bin",
        "image_mimetype",
        "tattoos"],
    **{
        'name': str,
        'email': str,
        'birth_date': str,
        'phone': str,
        'password': str,
        'street': str,
        'number': int,
        'city': str
    })
def post_create(payload):
    session = current_app.db.session

    try:
        new_client = Client(**payload)

        session.add(new_client)
        session.commit()

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            msg = {"error_message": "key value already registered"}
            return jsonify(msg), HTTPStatus.CONFLICT

    return jsonify(new_client), HTTPStatus.CREATED
