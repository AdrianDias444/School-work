# Conversor Hexadecimal
def int_para_hex():
    numero = int(input("Número decimal: "))

    # Conversão manual decimal → hexadecimal
    hex_digits = "0123456789ABCDEF"
    resultado = ""

    if numero == 0:
        resultado = "0"
    else:
        while numero > 0:
            resto = numero % 16
            resultado = hex_digits[resto] + resultadonumero
            numero = numero // 16

    print(f"Hexadecimal: 0x{resultado}")


def hex_para_int():
    hex_num = input("Número hexadecimal: ")
    print(f"Decimal: {int(hex_num, 16)}")


opcao = input("1 - Decimal → Hexadecimal\n2 - Hexadecimal → Decimal\nOpção: ")

if opcao == "1":
    int_para_hex()
elif opcao == "2":
    hex_para_int()
else:
    print("Opção inválida")
