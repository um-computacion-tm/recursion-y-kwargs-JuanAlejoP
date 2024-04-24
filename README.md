# Juan Alejo Patiño - Recursión y Kwargs

##### La recursión en programación implica que una función se llama a sí misma para resolver un problema dividiéndolo en partes más pequeñas hasta alcanzar una solución.

##### En Python, los kwargs son argumentos de función que permiten pasar pares clave-valor arbitrarios, lo que añade flexibilidad a la función al permitir el paso de cualquier cantidad de argumentos de palabras clave.

### El archivo `personDB_search.py` contiene la función homónima:

#### `personDB_search`
##### Busca nombres coincidentes en una base de datos de personas, utilizando kwargs como argumentos de búsqueda. La función espera recibir cualquier número de argumentos posicionales y palabras clave, que se comparan con los datos de cada persona en la base de datos. Si encuentra personas que coincidan con todos los criterios proporcionados, devuelve una lista de sus identificadores. Si no se encuentra ninguna coincidencia, devuelve None.

### El archivo `recursion.py` contiene varias funciones para calcular series y secuencias utilizando diferentes enfoques:

#### `sum_series`
##### Calcula la suma de una serie utilizando una fórmula matemática directa.

#### `sum_while`
##### Calcula la suma de una serie utilizando un bucle while.

#### `sum_recursive`
##### Calcula la suma de una serie utilizando recursión. Aplica una condición de corte para terminar la recursión.

#### `factorial_while`
##### Calcula el factorial de un número utilizando un bucle while.

#### `factorial_recursive`
##### Calcula el factorial de un número utilizando recursión. Aplica una condición de corte para terminar la recursión.

#### `fibonacci_iterative`
##### Calcula el valor de la secuencia de Fibonacci de forma iterativa utilizando un bucle for.

#### `fibonacci_iterative_optimized`
##### Calcula el valor de la secuencia de Fibonacci de forma iterativa optimizada, evitando almacenar todos los valores previos.

#### `fibonacci_recursive`
##### Calcula el valor de la secuencia de Fibonacci utilizando recursión. Aplica una condición de corte para terminar la recursión.

### Los tests de `personDB_search` y `recursion.py` se encuentran en sus respectivos archivos.