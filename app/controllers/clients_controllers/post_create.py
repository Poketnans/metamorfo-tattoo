from http import HTTPStatus

from flask import jsonify
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import werkzeug.exceptions
from app.classes.app_with_db import current_app
from app.models.clients_model import Client
from app.decorators import verify_payload, validator
from app.services import get_files, generate_image_default


@validator(password="password", birthdate="birth_date", phone="phone", email="email")
@verify_payload(
    fields_and_types={
        'name': str,
        'email': str,
        'password': str,
        'birth_date': str,
        'phone': str,
        "general_information": str,
        'street': str,
        'number': int,
        'city': str
    },
    optional=["general_information"]
)
def post_create(payload):
    session: Session = current_app.db.session

    try:
        new_client = Client(**payload)

        files = get_files()
        if files:
            for file in files:
                new_client.image_bin = file.file_bin
                new_client.image_hash = file.filename
                new_client.image_mimetype = file.mimetype
        else:
            image = generate_image_default()
            new_client.image_mimetype = image.mimetype
            new_client.image_hash = image.filename
            new_client.image_bin = image.file_bin

        session.add(new_client)
        session.commit()

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            message = str(error.orig).split("Key")[1].split("=")[0]
            msg = {"msg": f"{message[2:-1]} already registered"}
            return jsonify(msg), HTTPStatus.CONFLICT
    except werkzeug.exceptions.UnsupportedMediaType as e:
        return e.description, HTTPStatus.UNSUPPORTED_MEDIA_TYPE

    return jsonify(new_client), HTTPStatus.CREATED
