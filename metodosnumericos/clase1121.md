### Introduccion a los metodos numericos
# Contexto:

Debemos ser concientes que no hay una __solucion unica__

# Metodos numericos:

Nos permite modelar y resolver problemas complejos utilizando la computacion 
Por ejemplo: La ecuacion de Navie-Stokes

# Scipy

- Interpolacion: Funcion que pase exactamente por un conjunto de datos
                Puede ser interpolacion de lineas o de polinomios.. Uso del teorema fundamental del calculo para generar una serie infinita que sean los datos
                __Grados de libertad del modelo__ tenemos control de ello?

- Aproximacion: Funcion que pase por una aproximacion del conjunto de datos
                Universo __minecraft__ jajajajd
                ![el universo segun los astronomos](/cubito.png)

- Ajuste de curvas: Motivacion distinta a simplemente aproximar datos. 
                    Un    modelo mas adecuado que otro, ya que hay caracteristicas fisicas que tienen una representacion matematica y si bien la matematica cambia, la fisica es siempre la misma. Esto se hace usando __estimadores estadisticos__.
                    - funcional lineal: Una funcion ϕ: V → F se llama funcional lineal si es lineal, es decir, si es __aditiva y homogenea__. El minimo cuadrado es un funcional lineal
                    Cuando una matriz es invertible significa que se puede diagonalizar? o no necesariamente? en ese caso, una matriz no invertible puede triangulizarse.
                    - Triangulizacion de la matriz: es el ultimo metodo analitico disponible antes de entrar a metodos numericos, pero en si es mas __caro__, por ende generalmente se pasa a metodo numerico altiro, nisiquiera se intenta una solucion analitica.
                    - Evaluacion del __minimo global__: El problema de encontrarlo es que de base es muy libre el ajuste de la curva a los datos
                    - Ruido de __Poisson__ : No hay ningun indicador de la realidad que diga que los errores siguen una distribucion de Poisson
                    



