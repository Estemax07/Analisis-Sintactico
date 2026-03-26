# Analisis Sintactico

Tarea con tres puntos sobre analisis sintactico, comparacion de algoritmos y comportamiento de expresiones aritmeticas.

---

## Estructura del proyecto

punto1/  
punto2/  
punto3/  
README.md  

---

## Punto 1

Archivo:
punto1/punto1.py

Se implementa un analizador sintactico para expresiones aritmeticas basado en la gramatica:

E -> E opsuma T  
E -> T  
T -> T opmul F  
T -> F  
F -> id | num | (E)

Se usa una forma equivalente para poder programarlo y construir el arbol sintactico.

### Cadenas utilizadas

1. 2+3*4  
2. 2+3-4  
3. 2+3*(4-5)  

### Ejecucion

cd punto1  
python3 punto1.py  

El programa muestra el arbol en consola para cada cadena.

### Visualizacion opcional

Se puede generar una grafica del arbol usando Graphviz.

Instalacion en macOS:

brew install graphviz  
pip install graphviz  

Si no se instala, el programa funciona igual mostrando el arbol en texto.

---

## Punto 2

Archivos:
punto2/punto2.py  
punto2/Expr.g4  
punto2/antlr_parser.py  

En este punto se compara el algoritmo CYK con un parser generado usando ANTLR con lenguaje objetivo Python.

La entrada consiste en expresiones aritmeticas como:

```
2+3*4
2+3-4
2+3*(4-5)
```  

### Ejecucion

cd punto2  
python3 punto2.py  

### Analisis

Se comparan ambos enfoques en terminos de tiempo de ejecucion y uso de memoria.

El algoritmo CYK tiene una complejidad teorica O(n³), ya que analiza combinaciones de subcadenas. Sin embargo, en esta implementacion simplificada y con entradas pequeñas, puede mostrar tiempos bajos.

Por otro lado, ANTLR utiliza un enfoque de parsing LL(*) que en la practica se comporta de forma cercana a O(n), siendo mas eficiente y escalable para expresiones reales. Aunque en algunos casos iniciales puede consumir mas tiempo o memoria, ofrece una solucion mas completa y utilizada en compiladores reales.

---

## Punto 3

Archivo:
punto3/punto3.py

Se comparan resultados de una expresion segun:

- asociatividad izquierda  
- asociatividad derecha  
- precedencia normal  
- precedencia inversa  

### Pruebas

1. 4 - 3 - 2  
2. 2 + 3 * 4  

### Ejecucion

cd punto3  
python3 punto3.py  

El programa muestra como cambian los resultados segun cada modificacion hecha a la gramatica aritmetia.

---

## Ejecucion general

cd punto1  
python3 punto1.py  

cd ../punto2  
python3 punto2.py  

cd ../punto3  
python3 punto3.py
