from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api import v1_router

origins = [
    "http://localhost:3000",
    "https://front.tcc.com.br",
]

tags_metadata = [
    {
        "name": "V1",
        "description": "Primeira versão da API"
    },
    {
        "name": "Auth",
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/api/v1")