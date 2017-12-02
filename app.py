from ProjetoParticipante.Participante import *
import model
import  sys

def main(args=[]):
    # Variáveis
    agenda =  None


    continuar = True

    while continuar:
            Participante.menu()
            #try:
            # Continuar a execução do programa.
            opcao = int(input("Digite a opção: "))

            if (opcao == 1):
                model.listarParticipante()

            elif (opcao == 2):
                model.adicionaParticipante()
            elif (opcao == 3):
                print("Seção encerada !!")
                continuar = False
            else:
                print("Ops! Opção inválida!")
            # except:
            #    print("!!! Opção errada !!!")



if (__name__ == "__main__"):
    main()