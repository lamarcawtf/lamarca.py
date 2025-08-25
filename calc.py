# estou usando a def para definir tudo que eu quero chamar depois no meu codigo
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

while True:
    print("\n=== Calculadora Jurubeba ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Exit")

    opcao = input("Escolha a opção desejada: ")

    if opcao == "5":
        print("saindo")
        break

    try:
        num1 = float(input("primeiro numero: "))   # aqui podemos usar float ou int. int para numeros inteiros ou float para numeros quebrados
        num2 = float(input("segundo número: "))    # aqui podemos usar float ou int. int para numeros inteiros ou float para numeros quebrados
    except ValueError:
        print("letras nao sao permitidas! Use somente numeros")
        continue

    if opcao == "1":
        print(f"Resultado: {soma(num1, num2)}")
    elif opcao == "2":
        print(f"Resultado: {subtracao(num1, num2)}")
    elif opcao == "3":
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif opcao == "4":
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Opção inválida! Escolha de 1 a 5.")
