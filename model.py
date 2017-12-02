from ProjetoParticipante.Participante import *
from datetime import date
import json


jsonObjs = []

def listarParticipante():
            try:
                participantes = []

                # Leitura do Arquivo.
                f = open("cadastro.txt", 'r', encoding="utf8")

                # Parser do JSON em Objeto.
                jsonObjs = json.loads(f.read())

                # Iteração dos elementos do JSON.
                for jsonObj in jsonObjs:
                    nome = jsonObj["nome"]
                    data = jsonObj["nascimento"].split("-")
                    email = jsonObj["email"]
                    nascimento = date(int(data[0]), int(data[1]), int(data[2]))
                    participante = Participante(nome, nascimento, email)
                    participantes.append(participante)

                #Imprime os participantes
                for i in participantes:
                    print("\n %s \n" %(i))

                f.close()
            except IndexError:
                print("Sem cadastros")

            except FileNotFoundError:
                print("Diretorio não encontrado")

def adicionaParticipante():
    try:
        # Dados do participante
        nome = input("\nDigite seu nome: ")
        nascimento = input("Digite sua data de nascimento: ")
        email = input("Digite seu e-mail: ")

        participante = Participante(nome, nascimento, email)

        participanteJson = {}
        participanteJson['nome'] = participante.nome
        participanteJson['nascimento'] = participante.nascimento
        participanteJson['email'] = participante.email
        jsonObjs.append(participanteJson)

        with open('Cadastro.txt', 'w', encoding='utf-8') as f:
            json.dump(jsonObjs, f, ensure_ascii=False, indent=4)

        f.close()


    except FileNotFoundError:
        print("Diretorio não encontrado")
