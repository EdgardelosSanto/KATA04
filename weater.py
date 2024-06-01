
def encontrar_dia_menor_variacion(archivo):
    menor_variacion = float('inf')
    dia_menor_variacion = None
    
    with open(archivo, 'r') as f:
        # Saltar las primeras líneas hasta llegar a los datos
        for _ in range(7):
            next(f)
        
        for linea in f:
            partes = linea.split()
            if partes:
                # Verificar si la primera columna contiene un número
                if partes[0].isdigit():
                    dia = int(partes[0])
                    max_temp = int(''.join(filter(str.isdigit, partes[1])))  # Filtrar solo dígitos
                    min_temp = int(''.join(filter(str.isdigit, partes[2])))  # Filtrar solo dígitos
                    variacion = max_temp - min_temp
                
                    if variacion < menor_variacion:
                        menor_variacion = variacion
                        dia_menor_variacion = dia
    
    return dia_menor_variacion

# Nombre del archivo Weather.dat
archivo_weather = r"C:\Users\edgar\Desktop\FOOT\weather.dat"
# Encontrar el día con la menor variación de temperatura
dia_menor_variacion = encontrar_dia_menor_variacion(archivo_weather)
print("El día con la menor variación de temperatura es:", dia_menor_variacion)
