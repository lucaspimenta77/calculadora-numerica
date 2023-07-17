def to_decimal(numero, base):
    try:
        decimal = int(numero, base)
    except ValueError:
        print('O número informado é inválido')
        return None
    return decimal

def to_base(decimal, base):
    digitos = '0123456789ABCDEF'
    resultado = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        resultado = digitos[decimal % base] + resultado
        decimal = decimal // base
    return resultado

def primeiro():
    try:
        numero = input('Digite um número: ')
        base_entrada = int(input('Digite a base de entrada (2 para binário, 8 para octal, 10 para decimal, 16 para hexadecimal): '))
        base_saida = int(input('Digite a base de saída (2 para binário, 8 para octal, 10 para decimal, 16 para hexadecimal): '))
    except ValueError:
        print("Entrada inválida")
        return
    
    decimal = to_decimal(numero, base_entrada)
    if decimal is None:
        return
    if base_saida == 10:
        print(f'Número convertido para base decimal: {decimal}')
    else:
        numero_convertido = to_base(decimal, base_saida)
        print(f'Número convertido para base {base_saida}: {numero_convertido}')

primeiro()
