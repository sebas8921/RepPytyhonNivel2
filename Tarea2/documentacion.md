# Documentacion Tarea 1 - Pyhon Intermedio

## Alumno: Sebastian Alvarado Salazar
 
## API Elegida: Rick and Morty 
https://rickandmortyapi.com/

### Librerias necesarias

Las librerias necesarias para la ejecuccion del programa son:

- **requests** pip install requests
- **concurrent.futures** es parte de las librerias estandart
- **os** parte de las librerias estandart
- **collections** parte de las librerias estandart
- **pandas** pip install pandas
- **matplotlib** pip install matplotlib
- **datetime** parte de las librerias estandart

### Archivo api.py

En este archivo se encuentra toda la logica necesaria para conectarse a los diversos endpoints del api, asi mismo sus variaciones para obtener todo el contenido o bien una pagina en especifico

- **def getInfoPersonajes():** nos ayuda a obtener la informacion de total de registros y paginacion de personajes

- **def getInfoUbicaciones():** nos ayuda a obtener la informacion de total de registros y paginacion de ubicaciones
     
- **def getInfoEpisodios():** nos ayuda a obtener la informacion de total de registros y paginacion de episodios

- **def getPersonajesPagina(pagina):** nos ayuda a obtener la informacion de todos los personajes de una pagina completa, recibiendo como parametro el numero de pagina
     
- **def getUbicacionesPagina(pagina):** nos ayuda a obtener la informacion de todas las ubicacion de una pagina completa, recibiendo como parametro el numero de pagina
     
- **def getEpisodiosPagina(pagina):** nos ayuda a obtener la informacion de todos los episodios de una pagina completa, recibiendo como parametro el numero de pagina


### Archivo main.py

Corresponde al codigo principal del programa el cual cuenta con un menu de 7 opciones

La rutina principal del programa es la siguiente:

1. Carga inicial de los datos del api (se consumen y se cargan en sus respectivos diccionarios locales)

2. Navegacion por el menu para poder ejecutar cada una de sus opciones

3. Se utiliza la opcion 7 para salir del programa

Los comentarios situados en la parte posterior de cada funcion describen su funcionamiento, asi mismo el comentario de la derecha en cada variable global nos indica su proposito.

### Opciones del menu

**1.Informacion general de la serie'**
Muestra el detalle de del conteo general de las tres principales tablas
**2.Mostrar información general de todos los personajes'**
Muestra la informacion general de todos los personajes
**3.Mostrar informacion general de todas las ubicaciones'**
Muestra la informacion general de todos las ubicaciones
**4.Mostrar informacion general de todos los episodios'**
Muestra la informacion general de todos los episodios
**5.Contabilizar los personajes por su estatus'**
Imprime un grafico de barras de los personajes por status
**6.Contabilizar los ubicaciones por tipo'**
Imprime un grafico de barras de lsd ubicaciones por tipo
**7.Describir los datos de las 3 tablas'**
Hace uso del metodo describe de los 3 dataframes principales
**8.Contabilizar los personajes creados por año'**
Imprime un comportamiento por año de crecion de los personajes en la base de datos
**9.Distribucion de personajes por Especie'**
Imprime un grafico que muestra la distribucion de personajes por especie.
**10.Salir del programa'**
Opcion para salir del programa 

### Añadidos a la version anterior de la tarea

- **Los datos ahora se almacenan en dataframes**
- **Opciones de visualizacion nuevas y graficadas**