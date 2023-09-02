import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Ruta del archivo de texto con los datos (ajusta la ruta según tu archivo)
archivo_datos = r'C:\Users\Sergio\OneDrive\Escritorio\Grafico\grafico\Datos.txt'

# Listas para almacenar los valores de X e Y
x = []
y = []

# Leer datos desde el archivo de texto con codificación 'utf-8'
with open(archivo_datos, 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        valores = linea.strip().split()
        if len(valores) == 2:
            x.append(float(valores[0]))
            y.append(float(valores[1]))

# Función para ajustar una parábola a los datos
def funcion_parabola(x, a, b, c):
    return a * x**2 + b * x + c

# Ajustar la curva a los datos
parametros_optimizados, _ = curve_fit(funcion_parabola, x, y)

# Crear un conjunto de puntos X para la curva de ajuste
x_curva = np.linspace(min(x), max(x), 100)

# Calcular los valores correspondientes de Y para la curva de ajuste
y_curva = funcion_parabola(x_curva, *parametros_optimizados)

# Crear la gráfica
plt.figure(figsize=(10, 6))  # Tamaño de la gráfica (opcional)
plt.plot(x, y, marker='o', linestyle='-', color='red', label='Datos')  # Datos originales en rojo
plt.plot(x_curva, y_curva, linestyle='-', color='blue', label='Curva de ajuste')  # Curva de ajuste en azul

# Personalizar la gráfica (etiquetas, título, leyenda, etc.)
plt.xlabel('Nombre 1')  # Cambiar etiqueta del eje X
plt.ylabel('Nombre 2')  # Cambiar etiqueta del eje Y
plt.title('Grafica de Datos XY con Curva de Ajuste')  # Título con caracteres Unicode
plt.legend()

# Mostrar la gráfica
plt.grid(True)  # Mostrar cuadrícula (opcional)
plt.show()

