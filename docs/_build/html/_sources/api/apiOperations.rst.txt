API Operations
==============

.. http:post:: /suma
   :noindex:
   
   Sum of two lists of numbers.
	 
   :form list(number): v1 (*required*) -- The name the of the author of the book
   :form list(number): v2 (*required*) -- The name the of the author of the book

**Example Request**

.. sourcecode:: bash
  
   curl -X GET http://127.0.0.1:5000/suma -d '{"v1": [1,2,3],"v2": [2,3,4]}' 

**Example Response**

.. sourcecode:: bash

   [3, 5, 7]

.. http:post:: /resta
   :noindex:
   
   Subtraction of two lists of numbers.
	 
   :form list(number): v1 (*required*) -- The name the of the author of the book
   :form list(number): v2 (*required*) -- The name the of the author of the book

**Example Request**

.. sourcecode:: bash
  
   curl -X GET http://127.0.0.1:5000/resta -d '{"v1": [1,2,3],"v2": [2,3,4]}' 

**Example Response**

.. sourcecode:: bash

   [3, 5, 7]

:statuscode 200: no error
:statuscode 500: The parameters are not valid.
:statuscode 500: Variables should be of type list of numbers.
:statuscode 500: The lists should have the same size.

.. http:post:: /mult
   :noindex:
   
   Multiplication of two lists of numbers.
	 
   :form list(number): v1 (*required*) -- The name the of the author of the book
   :form list(number): v2 (*required*) -- The name the of the author of the book

**Example Request**

.. sourcecode:: bash
  
   curl -X GET http://127.0.0.1:5000/mult -d '{"v1": [1,2,3],"v2": [2,3,4]}' 

**Example Response**

.. sourcecode:: bash

   [2, 6, 12]

:statuscode 200: no error
:statuscode 500: The parameters are not valid.
:statuscode 500: Variables should be of type list of numbers.
:statuscode 500: The lists should have the same size.

.. http:post:: /divis
   :noindex:
   
   Division of two lists of numbers.
	 
   :form list(number): v1 (*required*) -- The name the of the author of the book
   :form list(number): v2 (*required*) -- The name the of the author of the book

**Example Request**

.. sourcecode:: bash
  
   curl -X GET http://127.0.0.1:5000/divis -d '{"v1": [1,2,3],"v2": [2,3,4]}' 

**Example Response**

.. sourcecode:: bash

   [0.5, 0.6666, 0.75]

:statuscode 200: no error
:statuscode 500: The parameters are not valid.
:statuscode 500: Variables should be of type list of numbers.
:statuscode 500: The lists should have the same size.
:statuscode 500: Division by 0 is not possible.