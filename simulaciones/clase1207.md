## Contexto
Simulaciones numericas en astrofisica, cuales son los ingredientes principales que tenemos que incluir en una simulacion?  
* Estrellas
* Materia oscura
* Gas
## Gas x.x  
El estado de un fluido esta especificado por:  
- Densidad: $\rho (x,t)$ - escalar
- Presion
- campo de velocidad
- potencial gravitatorio

Hay dos formas de modelar la dinamica del gas  
- Eulerian formulation: Estaciones de medicion fuera del fluido
- Lagrangian formulation: Medicion dentro del fluido  

# Enfoque lagrangiano
por ejemplo, Smooth Particle Hydrodynamics  
Las particulas interactuan entre si con distancia de funcion de __kernel__ cuyo radio caracteristico es conocido como longitud de suavizado, los kernel no necesariamente son uniformes, e interactuan entre si. La funcion de kernel tiene que ser igual para todas las particulas ya que depende de la fisica detras del fluido  
>ventajas :  - es ilimitado en espacio por lo que no se pierde materia, la conserva
>            - no se pierde tiempo moedelando espacios vacíos, only evoluciona en regiones con densidad $!= 0$
>            - resolución adaptativa, si quiero cambiar el tamaño del kernel o cambiar la resolución de masa, (no hay que cambiar la grilla entera)
>            - historia de evolución del fluido es intrínsecamente fácil de rastrear, (con los semilagran o lagrangianos es imposible)
>           - natulareza de partículas facilita acoplamiento con física de N-body o autogravedad, si tiengo partículas trazando el campo es + fácil conectarlo con el campo gravitatorio (x ej: DM), es como una partícula en ESTE caso
>            - distribución de masa entre partículas asegura la conservación exacta de la masa, ya que la masa de c/particle es cte a lo largo del tiempo

_en euler fijo la cajita, SPH es mejor que euleriano !_

>desventajas: - si quiero calcular cualquier valor necesito saber cuáles son los vecinos, actualizar constantemente la lista de vecinos
>            - condiciones iniciales influyen en el resultado
>            - resolución está limitada por el número de partículas  

# Enfoque euleriano
en este caso, puede ser el Adaptive-mesh refinement  
Se resuelven usando un esquema de __volumen finito__ de Godunov (metodo numerico para resolver ecuaciones de conservacion en problemas de dinamicas de fluidos)
Aqui se calculan: flujos de masa, flujos de calor, cantidad de movimiento y energia  
La solucion se basa en aproximaciones del metodo de riemman en 2d

>desventajas: -No invariancia de galileo, cuando hay desplazamientos a distintas velocidades se puede commplicar el calculo de las soluciones 

# Alternative methods 