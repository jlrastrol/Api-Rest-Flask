def suma(a: list, b:list) -> list:

    suma = [x + y for x, y in zip(a, b)]

    return suma

def resta(a: list, b:list) -> list:

    resta = [x - y for x, y in zip(a, b)]

    return resta


def mult(a: list, b:list) -> list:

    mult = [x * y for x, y in zip(a, b)]

    return mult

def divis(a: list, b:list) -> list:

    divis = [x / y for x, y in zip(a, b)]  

    return divis



