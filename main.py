from fastapi import FastAPI

api = FastAPI()

@api.get("/main")
def hello_world():
    return{
        "menssagem": "Ola seja bem-vido ao seu novo mundo ",
        "status": 200,
        "nome": "William Monteiro dos Santos",
        "cor": "amarelo",
        "william": "filho de Nidia Maria",
         "cor_3": "#523cac",
    }

nome: str = "william"
idade: int = 20
compra: str = "Bolo"
valor_da_compra: float = 250.99

nome: str = "Nidia"
idade: int = 47
compra: str = "laranja"
valor_da_compra: float = 8.99

nome: str = "Clademiro"
idade: int = 59
compra: str = "carro"
valor_da_compra: float = 6.00000

print(type(nome))
print(type(idade))
print(type(compra))
print(type(valor_da_compra))


