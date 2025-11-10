from fastapi import APIRouter
from api.authenticator import token_endpoint


def get_auth_router():
    auth_router = APIRouter(tags=["Autenticação"])
    auth_router.add_api_route("/token", token_endpoint, methods=["POST"])

    return auth_router
