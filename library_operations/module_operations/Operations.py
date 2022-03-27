class operations:

    def suma(self, a: list, b:list) -> list:

        if(self.__onlyNumber(a) != True or self.__onlyNumber(b) != True ):
            raise TypeError

        if(len(a) == len(b)):
            suma = [x + y for x, y in zip(a, b)]
        else:
            raise OverflowError

        return suma

    def resta(self, a: list, b:list) -> list:

        if(self.__onlyNumber(a) != True or self.__onlyNumber(b) != True ):
            raise TypeError

        if(len(a) == len(b)):
            resta = [x - y for x, y in zip(a, b)]
        else:
            raise OverflowError

        return resta


    def mult(self, a: list, b:list) -> list:

        if(self.__onlyNumber(a) != True or self.__onlyNumber(b) != True ):
            raise TypeError

        if(len(a) == len(b)):
            mult = [x * y for x, y in zip(a, b)]
        else:
            raise OverflowError

        return mult

    def divis(self, a: list, b:list) -> list:

        if(self.__onlyNumber(a) != True or self.__onlyNumber(b) != True ):
            raise TypeError

        if(len(a) == len(b)):
            divis = [x / y for x, y in zip(a, b)]  
        else:
            raise OverflowError

        return divis


    def __onlyNumber(self , a: list) -> bool:

        onlyInteger = True
        types = (float, int)

        for element in a:
            if(isinstance(element, types) != True ):
                onlyInteger = False
                break

        return onlyInteger

