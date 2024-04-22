# def sum(value):
#     return value * (value + 1)/2

# def sum(value):
#     result = 0
#     while value != 0:
#         result = result + value
#         value = value -1
#     return result

# def sum(value):
#     #Condición de corte
#     if value == 1:
#         return 1
#     #Proceso recursivo
#     return value + sumatoria(value -1)

#En la recursividad, la condición de corte se coloca siempre al inicio.

# def factorial(value):
#     result = value
#     while value > 2:
#         result = result * (value - 1)
#         value = value - 1
#     return result

# def factorial(value):
#     #Condición de corte
#     if value in (0, 1):
#         return 1
#     #Llamada recursiva
#     return value * factorial(value -1)

# def fibonacci(value):
#     if value < 2:
#         return value
#     values = [0, 1]
#     for i in range(value -1):
#         values.append(values[-1] + values[-2])
#     return values[value]

# def fibonacci(value):
#     if value == 0:
#         return value
#     previous, result = 0, 1
#     for i in range(value - 1):
#         previous, result = result, previous + result
#     return result

# def fibonacci(value):
#     #Condición de corte
#     if value in (0, 1):
#         return value
#     return fibonacci(value - 1) + fibonacci(value - 2)