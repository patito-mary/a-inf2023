### HDF5 - h5py en python

 - h5repack: Controla como se organizan losdatos dentro del archivo. con chunks, para extender o reducir en tama;o el archivo
 __muy importante para mi  aaaa__

 - h5dump: sacar datos a la consola, gran ventaja

 - h5ls: explorar archivos, ver que hay adentro y de forma recursiva

> Supongamos que la mayoria de los objetos hdf5 tiene el metodo .keys( ) que devuelve todos los grupos asociados al archivo
> Para un archivo pequeno que pesa menos de 250 mb utilizo el `hdfview nombrearchivo`
>  `.attrs`: Los __atributos__ sirven para meter meta-datos en general, i.e. caracteristicas, unidades de medida, propiedades, etc

Apenas calculo la funcion de luminosidad, tomo los histogramas, los datos y se guardan en hdf5

# Metadatos utiles: 
- fecha de creacion y lugar
- version de codigo utilizado
- modificaciones a la version utilizada
- parametros utilizados
- opciones de compilacion
- naturaleza de los datos
- unidades
- etc!

Los atributos pueden estar asociados a cualquier grupo o dataset de un hdf5. 

__Es muy importante guardar como se guardan los datos, como se creo el archivo y asi evitar que deje de ser inutil al corto plazo__

# Ejemplo
Gadget y su header de 254 bits akjakjs

_El estandar actual de las simulaciones es HDF5_