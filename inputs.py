def potencia(base, expoente):
    i = 0
    acumulador = 1
    while i < expoente:
        acumulador = acumulador * base
        i += 1
    return acumulador

input_base = int(input("coloque a base:"))
input_expoente = int(input("coloque o expoente:"))
result = potencia(input_base, input_expoente)
print(result)
