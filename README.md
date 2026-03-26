# Analisis Sintactico

Tarea con tres puntos sobre analisis sintactico, comparacion de algoritmos y comportamiento de expresiones aritmeticas.

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

### Cadena utilizada
2+3*(4-5)

### Ejecucion
python3 punto1.py

El programa muestra el arbol en consola.

### Ejemplo de salida

```
        +
      /   \
     2     *
          / \
         3   -
            / \
           4   5
```

### Visualizacion opcional
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

### Ejecucion
python3 punto2.py

### Analisis

Se observa que el algoritmo CYK incrementa su tiempo de ejecucion a medida que crece el tamaño de la cadena, ya que evalua combinaciones de subcadenas. Por otro lado, el analizador lineal recorre la entrada una sola vez, por lo que su tiempo se mantiene bajo incluso cuando aumenta la cantidad de identificadores.

Esto evidencia que CYK tiene un mayor costo computacional, mientras que el analisis lineal resulta mas eficiente cuando la gramatica es adecuada para este tipo de procesamiento.

---

## Punto 3

Archivo:
punto3.py

Se comparan resultados de una expresion segun:

- asociatividad izquierda
- asociatividad derecha
- precedencia normal
- precedencia inversa

### Pruebas

1. 4 - 3 - 2  
2. 2 + 3 * 4  

### Ejecucion
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
