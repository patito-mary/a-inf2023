## Evolucion temporal
- Metodo directo para calcular fuerzas: Tree method (Barnes-Hut) (TM)


    Division en subunidades o paquetes, de tal forma que sea mas facil calcular las fuerzas sobre un lugar.


    $F = - \sum \frac{Gm_i m_j}{{(r_i-r_j)}^3}(r_i - r_j) $
    Octal tree en 3D.  


    <image src='arbol.jpg' alt='imagen de arbol'>  



    Como decido el recorrido del arbol en funcion de una particula?
    Parametro de apertura: $\frac{L_2}{D_2} > \theta$ 
                            Todo lo que caiga dentro del angulo solido puede ser considerado como una unidad.
                            $D_2$ es mas o menos chica, en vez de alejarse se consideran de menor tamaño.
                            En general esta __estudiado__ cual es el mas eficiente, y dependiendo de la escala, se determina una apertura distinta
                            Si $\theta = 0$ se vuelve al caso de particle-particle  
    > Opening criteria:  
    > Barnes-hut  
    > Min-distance  
    > Bmax  
    Entre salida de snapshot y otro, hay pequeños saltitos y derrepente se saca el snapshot pero no es que la simulacion no corra  
    Ventajas:  
    > Eficiendcia: PP ~ O($N^2$) vs TM ~ NLog(N)  
    > Utilizar los centros de masa puede generar errores en los calculos de fuerza  
    > __Expansiones multipolares__ para evaluar mejor la masa dentro de la celda  
- Metodo para calcular fuerzas: Particle Mesh (PM)  
    El potencial gravitacional se contruye por 'mesh' usando la ecuacion de poisson:  
        $\nabla^2 \Phi = 4\pi G\rho $   
        se pasa a espacio de fourier para poder resolverla de manera mas inmediata usando la transformada como solucion a la integral, asumiendo una densidad __constante__ para el pozo de potencial

    Las grillas son fijas, pero se pueden superponer   
    Las grillas se pueden usar...  

    * Gadget: smooth particle hydrodinamics.
    * Arepo: cambia el sistema hydrodinamico.  


    > PM codes, density asssignment schemes  
    > $x_i \implies \rho (g_{k,l,m})$  
    > Que particula hay al lado, no anote el metodo jaja lol  
    > Cloud in cell (CIC): forma de cuadrdaditos  
    > Triangular shaped form: forma de traingulito alrededor de la particula principal  


- Hibrids things:


    P3M: Suma directa para particulas cercanas,     
    me falto una jaja lol  

- Metodo de integracion de orbitas


    __metodos numericos jaja lol__, pero como lo elejimos? depende del problema, pero hay que considerar las siguientes cosas:  
    * Consistencia: Cuando la solucion numerica tiende a la solucion analitica, es decir, el limite, por ende tiene que se lo suficientemente bueno   
    * Bajo error local: En el caso del uso de los metodos de euler, ruge kutta o taylor, el error se considera como la siguiente aproximacion despues del corte   
    * Bajo error global: En general se calcula encomo la diferencia absoluta entre la solucion numerica y solucion exacta en ese momento, es como comparar el mejor de los casos con el caso actual. Se puede aproximar usando parametros fisicos como el calculo de la energia total, o leyes basicas tipo toda la energia se transforma y no se pierde etc  
    Por ende si se conoce el $\Phi$ es necesario que las particulas se muevan en funcion de eso


    * Metodo de Euler: Aproximacion de Taylor de primer orden, por ende el error es el siguiente termino de la expansion de taylor  
                    Es facil pero no es muy preciso, por ende existen mejoras al metodo


    * Metodo del punto medio: Se calcula el metodo de euler 2 veces, de principio a medio y de medio a fin, por ende cuesta computacionalmente un poco mas pero es infinitamente mejor. Y luego se traza la trayectoria de principio a fin  
    * Metodo de Leapfrog: Calcula la velocidad paso a paso, usando un punto medio entre dos lugares y luego en pasos completos para compara los resultados y llegar a la velocidad final  

    <image src='ranita.png' alt='ranita'>  


    Tiene muy buenas propiedades en funcion de su reversibilidad en el tiempo, conserva el __momento angular__ de manera exacta, y hay otro que no anote


    * Metodo de Runge-Kutta: Metodo de aproximacion de cuarto orden, por ende es mucho mas complejo pero con mejor aproximaciones, considera pendientes en 4 lugares distintos


        $y_{i+1} = y_i + \frac{h}{6}(k_1 + 2k_2+ 2k_3 + k+4) + O(h^5)$ 


        El error es el $O(h^5)$. Pero no es simplectico
        __(espacio vectorial simpléctico a un espacio vectorial junto con una forma bilineal antisimétrica no degenerada, es decir, fisicamente se mantienen las condiciones de conservacion de energia)__ 
