# Laboratorio 2 - Curso de Python Intermedio

## Alumno: Sebastian Alvarado

### Resultados de las diferentes operaciones

La siguiente tabla describe los resultados obtenidos al ejecutar las diferentes metodologias de concurrencia con el ejercicio dado:

| Metodo | Duracion(segundos) |
| ----------- | ----------- |
| Tradicional(Sincrónica) | 8.0 segundos |
| Multiprocess | 1.73 segundos |
| Asyncio | 8.3 segundos |
| Threads | 0.91 segundos |

### Hallazgos en el resultado

- Multiprocessing y Threads encabezan la lista, sin embargo Threads se volvia mas eficiente conforme se utilizaran mas workers
- Asyncio era muy similiar en eficiencia a la forma tradicional(sincronica) por lo cual el problema de eficiencia se puede deducir que estaba en el CPU ya que al manipular su uso podiamos mejorar el rendimiento de la tarea solicitada.

