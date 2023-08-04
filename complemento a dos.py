def complemento_a_dos(binario):
    # Invertir bits
    complemento = ''.join('1' if bit == '0' else '0' for bit in binario)
    
    # Sumar 1 al complemento invertido
    carry = 1
    resultado = ''
    for bit in complemento[::-1]:
        if bit == '1':
            if carry == 1:
                resultado = '0' + resultado
            else:
                resultado = '1' + resultado
        else:
            if carry == 1:
                resultado = '1' + resultado
                carry = 0
            else:
                resultado = '0' + resultado
    
    return resultado

binario = input("Ingresa un número binario: ")
complemento = complemento_a_dos(binario)
print("Complemento a dos:", complemento)
