from fastapi import Request
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

        return await call_next(request)