### Contexto
Expresiones matematicas, mejor ajuste, solucion analitica.. mas alla de encontrar el conjunto de parametros que permite minimizar cierto comportamiento __no tiene nada mas__
- `curvefit` de scipy siempre entrega una solucion __numerica__, no analitica

## Clase Anterior: Ajuste de curvas
Como determinamos que tan bien se ajusta un __modelo__ a los __datos__?
Caracterizacion del universo! 
> Ejemplo: Perfil de Navarro-Frenk-White

$\Xhi^{2}$ : Cada uno de mis datos observados, se pesa por algo y entrega el minimo cuadrado de total de cada dato. De aqui deriva la _prueba de $\Xhi^{2}$ de Pearson_.

$\Xhi^{2}$ reducido: El mismo $\Xhi^{2}$, se pesa por el numero de datos observados y los grados de libertad del modelo usado.
Solo sirve para comparar funciones

## Clase
# Metodo de MonteCarlo
Numeros aleateorios para samplear algo que permita resolver y calcular lo que se necesite
> Algoritmo no determinista
> Utiliza numeros aleateorios
> Requiere un gran numero de iteracion (poder computacional)
> Apropiados para problemas que involucran un gran numero de parametros

Nace de la Aguja de Buffon (1777): Donde calculaban pi usando una aguja

__Aplicaciones de MonteCarlo__
- Calculo de una integral cerrandola en un cuadrado
- Ray tracing para jugar minecraft
- Problemas de optimizacion multidimensionales
- Random walk

