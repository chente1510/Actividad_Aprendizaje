# Función para codificar un número decimal en código Gray
def codificar_gray(numero_decimal):
    return numero_decimal ^ (numero_decimal >> 1)
# Función para decodificar un número en código Gray al decimal original
def decodificar_gray(gray_numero):
    numero_decimal = gray_numero
    while gray_numero > 0:
        gray_numero >>= 1
        numero_decimal ^= gray_numero
    return numero_decimal
# Ejemplo de uso
numero_decimal_original = 66
# Codificación
codigo_gray = codificar_gray(numero_decimal_original)
print("Número decimal original:", numero_decimal_original)
print("Código Gray:", codigo_gray)
# Decodificación
numero_decimal_decodificado = decodificar_gray(codigo_gray)
print("Número decimal decodificado:", numero_decimal_decodificado)