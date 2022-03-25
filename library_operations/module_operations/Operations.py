def suma(a: list, b:list) -> list:

    if(len(a) == len(b)):
        suma = [x + y for x, y in zip(a, b)]
    else:
        raise OverflowError

    return suma

def resta(a: list, b:list) -> list:
    if(len(a) == len(b)):
        resta = [x - y for x, y in zip(a, b)]
    else:
        raise OverflowError

    return resta


def mult(a: list, b:list) -> list:

    if(len(a) == len(b)):
        mult = [x * y for x, y in zip(a, b)]
    else:
        raise OverflowError

    return mult

def divis(a: list, b:list) -> list:

    if(len(a) == len(b)):
        divis = [x / y for x, y in zip(a, b)]  
    else:
        raise OverflowError

    return divis



