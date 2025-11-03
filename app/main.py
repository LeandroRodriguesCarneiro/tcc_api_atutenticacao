from fastapi import FastAPI
from app.controllers import AuthController, UserController

tags_metadata = [
    {
        "name": "auth",
        "description": "Operações de autenticação: login, verificação de token, etc.",
    },
    {
        "name": "User",
        "description": "Gerenciamento de usuários: criação, listagem, etc.",
    },
]

app = FastAPI(
        title="Auth API",
        description="API para autenticação de usuários",
        version="alpha 0.0",
        openapi_tags=tags_metadata      
              )
app.include_router(AuthController.router)
app.include_router(UserController.router)
