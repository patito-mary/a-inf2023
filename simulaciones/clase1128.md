## Introduccion
Fuerzas + particulas + condiciones inciales = simulaciones numericas
Fuerzas:
- Gravedad
- Viscosidad
- Presion
Se pueden aplicar por ejemplo en: Evolucion de sistemas planetarios
En general la solucion a los problemas de mas de 3 cuerpos (no integrables, i.e. demasiados grados de libertad) son __numericas__

* caotico: peque;as perturbaciones en condiciones iniciales produce caos a largo plazo. Es muy sensible a perturbaciones de las condiciones iniciales
## Para que se usan? 

cambios en los observables fisicos debido a procesos naturales del universo (Explosiones de super nova, perdida de masa instantanea, AGN feedback)

# Pasos a seguir
1. Seleccionar problema de estudio, por que? para saber como abordarlo
2. Marco teorico: LamdaCDM, warmDM, gravedad modificada, etc. Aqui tambien vienen las suposiciones y simplifaciones
3. Generar las condiciones iniciales:
- Por ejemplo un cumulo globular se define en un espacio cumpliendo ciertas condiciones, pero tambien tienen que estar en __equilibrio__ las fuerzas para que el sistema se __mantenga__ en el tiempo
- Usar las funciones en todas las dimensiones que se vayan a analizar, con el fin de discretizar ...
4. Para resolver las ecuaciones es necesario discretizar ya que la simulacion noi avanza de manera continua en el tiempo y por ende, hay que elegir como se van a dar los saltos de tiempo.
5. Input/Output: Seleccionar y escribir el codigo

# Metodos numericos
El mas simple es resolver una integral, para ecuaciones acopladasy otros.. 
saco el área bajo la curva, pero si la fn es complicada se resuelve con aproximaciones, cuáles? dependen de cuántos errores quiero propagar, con Riemann, mientras + xikito el rectangulito mejor es la aproximación es mejor la aproximación del trapecio, hacer una línea y rellenar
__From stars to LLL__

En funcion de la fisica que esta ocurriendo mi teoria es que tal proceso afecta tal cosa y genera por ejemplo el aparicion de un brazo espiral..

Es complicado simular galaxias tipo MW (L*) por la influencia del AGN feedback en el limite de masa de dichas galaxias. A mayor masa el AGN importa mas y a menor masa (que M*) importa menos
- Migracion radial de las estrellas en galaxias discos
- A pesar de que se utilizen simetrias para poder simplificar calculos, hay que considerar el hecho de como evoluciona y afecta al resto de los parametros en funcion del tiempo

# Centro de supercomputos
- Cositas random, 300000 de horas son 343 años

# Marco Teorico
Primero debemos decir cual es la fisica que utilizaremos para correr los parametros iniciales y considerar el
__Principio cosmologico: El universo es homogeneo e isotropico__
- Homogeneo: No hay un punto preferencial en el universo
- Isotropico: El universo es igual para todas las direcciones
Fondo cosmico de microondas: Las perturbaciones en temperatura son distribuciones preferenciales de masa
Lo primero que colapsa forman los halos de materia oscura que solo interactuan gravitatoriamente con ellos mismos, y luego se convierten en sumideros que atraen gas y empiezan a formar estructuras

__Overdensity > Sheet > filamentlike structure > halo regordete__

Simulacion Aquarius (2008): Universo Jerarquico 

Halos de DM: 
- Fisica: Gravedad
Bariones:
- Estrellas:
    - Evolucion y formacion estelar: Se usa la __IMF__
    - Enriquecimiento quimico
    - Feedback de SN: Como se calienta el gas
    - Etc
- Gas:
    - Feedback de AGN: Cuando se prende cuando __calienta__ el medio
- aaa no alcanze

Para las estrellas es dificil poder simular una particula con una estrella.. Es imposible computacionalmente hablando. Cada particula es una poblacion estelar con una unica metalicidad y edad. 


