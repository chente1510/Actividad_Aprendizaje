def alu(a, b, op):
    if op == "000":  # Suma
        return bin(int(a, 2) + int(b, 2))[2:].zfill(4)
    elif op == "001":  # Resta
        return bin(int(a, 2) - int(b, 2))[2:].zfill(4)
    elif op == "010":  # AND lógico
        return bin(int(a, 2) & int(b, 2))[2:].zfill(4)
    elif op == "011":  # OR lógico
        return bin(int(a, 2) | int(b, 2))[2:].zfill(4)
    else:
        raise ValueError("Operación no válida.")

# Ejemplo de uso
resultado_suma = alu("1111100111", "1100001001", "000")  # A = 6, B = 3, OP = 000 (Suma)
resultado_resta = alu("1111100111", "1100001001", "001")  # A = 6, B = 3, OP = 001 (Resta)
resultado_and = alu("1111100111", "1100001001", "010")  # A = 6, B = 3, OP = 010 (AND)
resultado_or = alu("1111100111", "1100001001", "011")  # A = 6, B = 3, OP = 011 (OR)

print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)
print("Resultado del AND:", resultado_and)
print("Resultado del OR:", resultado_or)