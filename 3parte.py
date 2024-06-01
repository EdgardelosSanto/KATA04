def leer_datos_desde_archivo(archivo, columnas):
    datos = []
    
    with open(archivo, 'r') as f:
        # Saltar las primeras líneas hasta llegar a los datos
        for _ in range(7):
            next(f)
        
        for linea in f:
            partes = linea.split()
            if partes:
                # Verificar si la primera columna contiene un número
                if partes[0].isdigit():
                    fila = [partes[col] for col in columnas]
                    datos.append(fila)
    
    return datos

def encontrar_equipo_menor_diferencia(archivo):
    datos = leer_datos_desde_archivo(archivo, [1, 6, 8])
    # Aquí va la lógica específica para encontrar el equipo con la menor diferencia de goles
    # Retorna el nombre del equipo con la menor diferencia

def encontrar_dia_menor_variacion(archivo):
    datos = leer_datos_desde_archivo(archivo, [0, 1, 2])
    # Aquí va la lógica específica para encontrar el día con la menor variación de temperatura
    # Retorna el número del día con la menor variación

# Nombre del archivo football.dat
archivo_football = r"C:\Users\edgar\Desktop\FOOT\football.dat"
# Encontrar el equipo con la menor diferencia de goles
equipo_menor_diferencia = encontrar_equipo_menor_diferencia(archivo_football)
print("El equipo con la menor diferencia en goles es:", equipo_menor_diferencia)

# Nombre del archivo Weather.dat
archivo_weather = r"C:\Users\edgar\Desktop\FOOT\weather.dat"
# Encontrar el día con la menor variación de temperatura
dia_menor_variacion = encontrar_dia_menor_variacion(archivo_weather)
print("El día con la menor variación de temperatura es:", dia_menor_variacion)
