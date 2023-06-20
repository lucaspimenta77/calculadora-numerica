def convert_number(numero, base_entrada, base_saida):
    try:
        numero_decimal = int(numero, base_entrada)

        if base_saida == 2:
            numero_convertido = bin(numero_decimal)[2:]
            nome_base = "binário"
        elif base_saida == 10:
            numero_convertido = str(numero_decimal)
            nome_base = "decimal"
        elif base_saida == 16:
            numero_convertido = hex(numero_decimal)[2:].upper()
            nome_base = "hexadecimal"
        elif base_saida == 8:
            numero_convertido = oct(numero_decimal)[2:]
            nome_base = "octal"
        else:
            print("Erro: Base de saída inválida.")
            return

        print(
            f"O número {numero} na base {base_entrada} foi convertido para a base {base_saida} ({nome_base}): {numero_convertido}"
        )

    except ValueError:
        print("Erro: O número fornecido não está de acordo com a base de entrada.")


base_entrada = int(input("Digite a base de entrada (2, 8, 10 ou 16): "))
base_saida = int(input("Digite a base de saída (2, 8, 10 ou 16): "))

bases_validas = [2, 8, 10, 16]
if base_entrada not in bases_validas or base_saida not in bases_validas:
    print("Erro: As bases devem ser 2, 8, 10 ou 16.")
else:
    numero = input(f"Digite o número na base {base_entrada}: ")

    convert_number(numero, base_entrada, base_saida)
