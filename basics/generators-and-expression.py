
# : Los generadores son una forma eficiente de crear secuencias de valores en Python. Se utilizan para generar valores de uno en uno en lugar de crear una lista completa en la memoria.
def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, b + a


print(list(fibonacci_generator(10)))


def get_squares(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

print(get_squares(10))