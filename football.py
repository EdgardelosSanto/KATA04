def encontrar_equipo_con_menor_diferencia_goles(archivo):
    # Inicializar variables para almacenar el nombre del equipo con la menor diferencia y su valor
    equipo_menor_diferencia = None
    menor_diferencia = float('inf')  # Inicializar con un valor grande
    
    # Abrir el archivo
    with open(archivo, 'r') as f:
        # Leer cada línea de datos
        for linea in f:
            # Dividir la línea en partes usando los espacios como separadores
            partes = linea.split()
            # Verificar si la línea contiene datos relevantes (ignorar líneas vacías y encabezados)
            if partes and partes[0].isdigit():
                # Extraer el nombre del equipo, goles a favor y goles en contra
                equipo = partes[1]
                goles_a_favor = int(partes[6])
                goles_en_contra = int(partes[8])
                # Calcular la diferencia en goles
                diferencia = abs(goles_a_favor - goles_en_contra)
                # Actualizar el equipo con la menor diferencia si encontramos uno nuevo
                if diferencia < menor_diferencia:
                    equipo_menor_diferencia = equipo
                    menor_diferencia = diferencia
    
    return equipo_menor_diferencia

# Nombre del archivo football.dat
archivo_football = r"C:\Users\edgar\Desktop\FOOT\football.dat"
# Llamar a la función para encontrar el equipo con la menor diferencia en goles a favor y en contra
equipo_menor_diferencia = encontrar_equipo_con_menor_diferencia_goles(archivo_football)
print("El equipo con la menor diferencia en goles es:", equipo_menor_diferencia)
