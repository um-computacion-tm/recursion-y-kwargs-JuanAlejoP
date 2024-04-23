def sum_series(value):
    return value * (value + 1)/2

def sum_while(value):
    result = 0
    while value != 0:
        result = result + value
        value = value -1
    return result

def sum_recursive(value):
    #Condición de corte
    if value == 1:
        return 1
    #Proceso recursivo
    return value + sum_recursive(value -1)

# En la recursividad, la condición de corte se coloca siempre al inicio.

def factorial_while(value):
    result = value
    while value > 2:
        result = result * (value - 1)
        value = value - 1
    return result

def factorial_recursive(value):
    #Condición de corte
    if value in (0, 1):
        return 1
    #Llamada recursiva
    return value * factorial_recursive(value -1)

def fibonacci_iterative(value):
    if value < 2:
        return value
    values = [0, 1]
    for i in range(value -1):
        values.append(values[-1] + values[-2])
    return values[value]

def fibonacci_iterative_optimized(value):
    if value == 0:
        return value
    previous, result = 0, 1
    for i in range(value - 1):
        previous, result = result, previous + result
    return result

def fibonacci_recursive(value):
    #Condición de corte
    if value in (0, 1):
        return value
    return fibonacci_recursive(value - 1) + fibonacci_recursive(value - 2)