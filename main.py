from fastapi import FastAPI

api = FastAPI()

@api.get("/hello")
def hello_world():
    return{
        "menssagem": "Ola seja bem-vido ao seu novo mundo ",
        "status": 200,
        "nome": "William Monteiro dos Santos",
        "cor": "amarelo",
        "fala": "nada de mais"
    }