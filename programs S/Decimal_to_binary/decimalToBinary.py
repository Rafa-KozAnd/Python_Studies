def decimal_para_binario(decimal):
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    return binario

def main():
    # Solicita ao usuário que entre com um número decimal
    decimal = int(input("Digite um número decimal: "))

    # Converte o número decimal para binário
    binario = decimal_para_binario(decimal)

    # Imprime o resultado
    print(f'O número binário correspondente a {decimal} é: {binario}')

if __name__ == "__main__":
    main()
