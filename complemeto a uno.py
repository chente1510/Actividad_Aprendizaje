def complemento_a_uno(binario):
    complemento = ''
    for bit in binario:
        complemento += '0' if bit == '1' else '1'
    return complemento

def main():
    numero_binario = input("Ingresa el número binario: ")
    complemento = complemento_a_uno(numero_binario)
    print(f"El complemento a uno de {numero_binario} es: {complemento}")

if __name__ == "__main__":
    main()