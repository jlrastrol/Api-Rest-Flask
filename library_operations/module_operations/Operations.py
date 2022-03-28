class operations:

    def suma(self, a: list, b:list) -> list:
        '''This function returns the sum of two lists of numbers.'''
        if(self.__onlyNumber(a) != True or self.__onlyNumber(b) != True ): #Check that all values in both lists are numbers.
            raise TypeError

        if(len(a) == len(b)): # Check that the two lists are the same size.
            suma = [x + y for x, y in zip(a, b)]
        else:
            raise OverflowError

        return suma

    def resta(self, a: list, b:list) -> list:
        '''This function returns the subtraction of two list of numbers.'''
        if(self.__onlyNumber(a) != True or self.__onlyNumber(b) != True ): #Check that all values in both lists are numbers.
            raise TypeError

        if(len(a) == len(b)): # Check that the two lists are the same size.
            resta = [x - y for x, y in zip(a, b)]
        else:
            raise OverflowError

        return resta


    def mult(self, a: list, b:list) -> list:
        '''This function returns the multiplication of two lists of numbers.'''
        if(self.__onlyNumber(a) != True or self.__onlyNumber(b) != True ): #Check that all values in both lists are numbers.
            raise TypeError

        if(len(a) == len(b)): # Check that the two lists are the same size.
            mult = [x * y for x, y in zip(a, b)]
        else:
            raise OverflowError

        return mult

    def divis(self, a: list, b:list) -> list:
        '''This function returns the division of two lists of numbers.'''
        if(self.__onlyNumber(a) != True or self.__onlyNumber(b) != True ): #Check that all values in both lists are numbers.
            raise TypeError

        if(len(a) == len(b)): # Check that the two lists are the same size.
            divis = [x / y for x, y in zip(a, b)]  
        else:
            raise OverflowError

        return divis


    def __onlyNumber(self , a: list) -> bool:
        '''This function checks that all values in a list are numbers.'''
        onlyInteger = True
        types = (float, int)

        for element in a: # Loop through the list of values.
            if(isinstance(element, types) != True ): # Check if the value is an int or a float.
                onlyInteger = False
                break

        return onlyInteger

