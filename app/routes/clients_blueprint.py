from flask import Blueprint

from app.controllers.clients_controllers import post_login, post_create, get_all, get_specific, delete

bp_clients = Blueprint("clients", __name__)
bp_clients.post("/clients/login")(post_login)
bp_clients.post("/clients")(post_create)
bp_clients.get("/client")(get_specific)
bp_clients.get("/clients")(get_all)
bp_clients.delete("/clients")(delete)
