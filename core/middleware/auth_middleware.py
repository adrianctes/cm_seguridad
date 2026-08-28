""" from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        path = request.url.path

        # 🔓 RUTAS PÚBLICAS (NO bloquear)
        public_routes = [
            "/api/v1/auth/login",
            "/docs",
            "/openapi.json",
            "/redoc"
        ]

        if path in public_routes:
            return await call_next(request)

        # 🔐 validar token
        auth = request.headers.get("authorization")

        if not auth:
            return JSONResponse(
                status_code=401,
                content={"detail": "Falta token de autenticación"}
            )

        return await call_next(request) """
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        path = request.url.path

        # 🔓 RUTAS PÚBLICAS
        public_routes = [
            "/api/v1/auth/login",
            "/docs",
            "/openapi.json",
            "/redoc",
        ]

        # 🔓 PDF TEMPORAL
        # La autenticación se realiza mediante el token
        # incluido en la URL.
        if path.startswith(
            "/api/v1/liquidaciones/pdf-temporal/"
        ):
            return await call_next(request)

        # 🔓 otras rutas públicas
        if path in public_routes:
            return await call_next(request)

        # 🔐 validar JWT
        auth = request.headers.get("authorization")

        if not auth:
            return JSONResponse(
                status_code=401,
                content={
                    "detail": "Falta token de autenticación"
                }
            )

        return await call_next(request)