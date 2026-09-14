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

class Instrumentos:
    def __init__(self, nome, familia, voz):
        self.nome = nome
        self.familia = familia
        self.voz = voz

    def apresentar(self):
        return f" meu istrumento e {self.nome}, ele pertence a familia do(a)s {self.familia} e pertence a voz do {self.voz}"

Instrumento1 = Instrumentos("violino", "cortas", "Soprado")
print(Instrumento1.apresentar())


