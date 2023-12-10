suma = 0
for i in range(1, 10):
    if i % 3 == 0 or i % 5 == 0:
        suma += i
print("La suma de todos los múltiplos de 3 o 5 por debajo de 1000 da:", suma)