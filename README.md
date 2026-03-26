# Analisis Sintactico

Proyecto con tres puntos sobre analisis sintactico, comparacion de algoritmos y comportamiento de expresiones aritmeticas.

---

## Punto 1

Archivo:
punto1.py

Se implementa un analizador sintactico para expresiones aritmeticas basado en la gramatica:

E -> E opsuma T  
E -> T  
T -> T opmul F  
T -> F  
F -> id | num | (E)

Se usa una forma equivalente para poder programarlo y construir el arbol sintactico.

Cadena utilizada:
2+3*(4-5)

Ejecucion:
python3 punto1.py

El programa muestra el arbol en consola.

Ejemplo de salida:

└── +
    ├── 2
    └── *
        ├── 3
        └── -
            ├── 4
            └── 5

Visualizacion opcional:
Se puede generar una grafica del arbol usando Graphviz.

Instalacion en macOS:
brew install graphviz
pip install graphviz

Si no se instala, el programa funciona igual mostrando el arbol en texto.

---

## Punto 2

Archivo:
punto2.py

Se compara el algoritmo CYK con un analizador lineal usando cadenas tipo:

int id , id , id ;

Ejecucion:
python3 punto2.py

Salida obtenida:

5 ids
cadena: int id , id , id , id , id ;
CYK: 6.699562072753906e-05
Lineal: 2.384185791015625e-06

10 ids
cadena: int id , id , id , id , id , id , id , id , id , id ;
CYK: 0.00026226043701171875
Lineal: 1.9073486328125e-06

20 ids
cadena: int id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id ;
CYK: 0.0014071464538574219
Lineal: 2.384185791015625e-06

40 ids
cadena: int id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id , id ;
CYK: 0.011382341384887695
Lineal: 5.4836273193359375e-06

Analisis:
El tiempo de CYK crece mucho mas rapido conforme aumenta el tamaño de la entrada, mientras que el analizador lineal se mantiene muy bajo. Esto muestra que CYK es mas costoso y el analisis lineal es mas eficiente para esta gramatica.

---

## Punto 3

Archivo:
punto3.py

Se comparan resultados de una expresion segun:

- asociatividad izquierda
- asociatividad derecha
- precedencia normal
- precedencia inversa

Pruebas:
4 - 3 - 2
2 + 3 * 4

Ejecucion:
python3 punto3.py

El programa muestra como cambian los resultados segun cada caso.

---

## Ejecucion general

python3 punto1.py
python3 punto2.py
python3 punto3.py

---

## Archivos

punto1.py
punto2.py
punto3.py
