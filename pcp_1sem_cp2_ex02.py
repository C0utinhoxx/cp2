def ex2():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if a > b:
        print("Maior:", a)
    elif b > a:
        print("Maior:", b)
    else:
        print("São iguais")