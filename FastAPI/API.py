# pip install fastapi[all]

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "API para cálculos matemáticos. Informe dois números inteiros e a operação no formato string (somar, subtrair, dividir, multiplicar)"}

class Resp(BaseModel):
    valor1: int
    valor2: int
    operacao: str


@app.post("/rota")
async def rota(resp: Resp):
    if resp.operacao == "somar":
        operacao = resp.valor1 + resp.valor2
        return f"O resultado da operação é {operacao}"
    elif resp.operacao == "subtrair":
        operacao = resp.valor1 - resp.valor2
        return f"O resultado da operação é {operacao}"
    elif resp.operacao == "dividir":
        operacao = int(resp.valor1 / resp.valor2)
        return f"O resultado da operação é {operacao}"
    if resp.operacao == "multiplicar":
        operacao = resp.valor1 * resp.valor2
        return f"O resultado da operação é {operacao}"
    else:
        return "Os dados informados são inválidos. Informe dois números inteiros e na operação uma das opções (somar, subtrair, dividir, multiplicar)"