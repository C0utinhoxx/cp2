def ex5():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    print("Operações: +  -  *  /")
    op = input("Escolha a operação: ")

    if op == "+":
        print("Resultado:", a + b)
    elif op == "-":
        print("Resultado:", a - b)
    elif op == "*":
        print("Resultado:", a * b)
    elif op == "/":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Erro: divisão por zero")
    else:
        print("Operação inválida")