import pandas as pd
import matplotlib.pyplot as plt
datos =  pd.read_csv('ventas.csv', header=0)
datos = datos.assign(Ganancia = datos['Ventas']-datos['Gastos'])
print('------------------------------------------------------')
print('Datos resultantes')
print('------------------------------------------------------')
print(datos)
fig, ax = plt.subplots()
ax.plot(datos['Mes'], datos['Ventas'], label="Ventas")
ax.plot(datos['Mes'], datos['Gastos'], label="Gastos")
ax.legend()
plt.xlabel('Meses')
plt.ylabel('Cantidades')
plt.title('Ventas y Gastos por mes')
plt.show()





