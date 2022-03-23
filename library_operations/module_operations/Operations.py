def suma(a: list, b:list):

    suma = [x + y for x, y in zip(a, b)]

    return suma

def resta(a: list, b:list):

    resta = [x - y for x, y in zip(a, b)]

    return resta


def mult(a: list, b:list):

    mult = [x * y for x, y in zip(a, b)]

    return mult

def divis(a: list, b:list):

    divis = [x / y for x, y in zip(a, b)]

    return divis

print(suma([1,3,4,5], [3,5,6,7]))
print(resta([1,3,4,5], [3,5,6,7]))
print(mult([1,3,4,5], [3,5,6,7]))
print(divis([1,3,4,5], [3,5,6,7]))
