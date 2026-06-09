import os
import time
import json
from datetime import datetime


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def aguarde(segundos):
    time.sleep(segundos)


def inicializarBancoDeDados():
    try:
        with open("log.dat", "r"):
            pass
    except FileNotFoundError:
        with open("log.dat", "w") as f:
            f.write("[]")


def escreverDados(nome, pontos):
    with open("log.dat", "r") as f:
        dados = f.read()

    logList = json.loads(dados) if dados.strip() else []

    agora   = datetime.now()
    data_br = agora.strftime("%d/%m/%Y")
    hora_br = agora.strftime("%H:%M:%S")

    logList.append({
        "nome":   nome,
        "pontos": pontos,
        "data":   data_br,
        "hora":   hora_br
    })

    with open("log.dat", "w") as f:
        f.write(json.dumps(logList, ensure_ascii=False, indent=2))


def maior_pontuador():
    with open("log.dat", "r") as f:
        dados = f.read()

    logList = json.loads(dados) if dados.strip() else []

    nome_maior   = "---"
    dataJogada   = "---"
    horaJogada   = "---"
    maior_pontos = 0

    for registro in logList:
        if registro["pontos"] > maior_pontos:
            maior_pontos = registro["pontos"]
            nome_maior   = registro["nome"]
            dataJogada   = registro["data"]
            horaJogada   = registro["hora"]

    return nome_maior, maior_pontos, dataJogada, horaJogada  # ← 4 valores