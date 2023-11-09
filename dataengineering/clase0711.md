## CONTEXTO
Estrategias de almacenamiento de informacion

__Leer y escribir datos ++__

El formato tiene que ser una respuesta a un problema, no un estandar

Estrategia para leer: `open`

Importancia de cerrar los archivos: Los discos duros son mucho mas lentos que el guardado de datos

> Trabajar con los datos en la memoria RAM es mucho mas rapido que trabajar con los datos en el disco duro

Los archivos de texto son vectores unidimensionales, que usan el `\n, \t` para hacer los saltos de linea

> `seek` permite moverse dentro de los archivos

### CATEDRA

# Parseo
---
-split: subentiende separadores en los campos que tienen string, pero se puede usar el `sep = '\n' ` por ejemplo

Es mucho mas facil si usamos `numpy` para cargar los datos de manera que sean _float_ . Pero esto tiene una restriccion con respecto a acceder a los datos por __columnas__

> columnas: campos
> filas: registros

- unpack: toma un registro y lo desempaqueta, sirve para tratar columnas

# Pandas
---
Subentiende los tipos de datos, es una ventaja sobre `numpy`

`Pandas` es un cañon, por ende para cosas mas pequeñas es mejor usar `numpy`

`pandas` tambien permite utilizar iteradores para procesar archivos de texto cuya cantidad de datos es restrictiva segun los recursos computacionales y hacemos el proceso por partes usando los __chunks__




