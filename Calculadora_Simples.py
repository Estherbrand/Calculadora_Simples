# Entrada dos valores
while True:
    Valor1 = float(input("Digite o primeiro valor: "))
    Valor2 = float(input("Digite o segundo valor: "))

    # Entrada da operação
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    operacao = input("Digite o número da operação que deseja realizar: ")

    # Processo de acordo com a operação escolhida
    if operacao == "1":
        resultado = Valor1 + Valor2
        operacao = "adição"
    elif operacao == "2":
        resultado = Valor1 - Valor2
        operacao = "subtração"
    elif operacao == "3":
        resultado = Valor1 * Valor2
        operacao = "multiplicação"
    elif operacao == "4":
        if Valor2 != 0:  # Irá verificar se o divisor é diferente de zero
            resultado = Valor1 / Valor2
            operacao = "divisão"
        else:
            resultado = "Erro: Divisão por zero!"
            operacao = "divisão"
    else:
        resultado = "Operação inválida!"
        operacao = "desconhecida"

    #Saída das informações
    print(f"O resultado da {operacao} entre {Valor1} e {Valor2} é: {resultado}")

    # Caso queria realizar outra operação, o programa irá perguntar
    repetir = input("Deseja realizar outra operação? (s/n): ")
    if repetir.lower() != 's':
        print("Saindo do programa. Até logo!")
        break
