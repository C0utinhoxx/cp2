from exercicio1 import exercicio1
from exercicio2 import exercicio2
from exercicio3 import exercicio3
from exercicio4 import exercicio4
from exercicio5 import exercicio5

def main():
    print(" MENU DE EXERCÍCIOS ")
    print("1 - Par ou Ímpar")
    print("2 - Maior número")
    print("3 - Nota do aluno")
    print("4 - Faixa etária")
    print("5 - Calculadora")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        exercicio1()
    elif opcao == 2:
        exercicio2()
    elif opcao == 3:
        exercicio3()
    elif opcao == 4:
        exercicio4()
    elif opcao == 5:
        exercicio5()
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()