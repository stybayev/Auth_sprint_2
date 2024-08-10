from flask_jwt_extended import verify_jwt_in_request, get_jwt
from redis import Redis
from flask import request, jsonify

from core.config import settings

redis_client = Redis(host=settings.redis_host, port=settings.redis_port)


def check_blacklist() -> jsonify:
    """
    Функция для проверки токена в Redis
    """
    if (request.path.startswith('/apidocs')
            or request.path.startswith('/apispec')
            or request.path.startswith('/flasgger_static')):
        return None

    try:
        verify_jwt_in_request()
        jti = get_jwt().get("jti")
        if redis_client.get(f"invalid_token:{jti}"):
            return jsonify({"detail": "Token is blacklisted"}), 401
    except Exception as e:
        return jsonify({"detail": str(e)}), 401
