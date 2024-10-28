import random
import math

def elegir_k_puntos_aleatorios(points, k):
    # Selecciona 'k' puntos aleatoriamente del conjunto de datos
    return random.sample(points, k)

def calcular_distancia(punto1, punto2):
    # Calcula la distancia euclidiana entre dos puntos
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(punto1, punto2)))

def calcular_promedio(puntos):
    # Calcula el promedio de una lista de puntos
    num_puntos = len(puntos)
    if num_puntos == 0:
        return []
    return [sum(coord) / num_puntos for coord in zip(*puntos)]

def k_means(points, k, max_iterations=100):
    # Inicialización: elegir k centroides iniciales aleatoriamente
    centroids = elegir_k_puntos_aleatorios(points, k)

    for _ in range(max_iterations):
        # Crear un diccionario para almacenar los puntos de cada clúster
        clusters = {i: [] for i in range(k)}

        # Asignación de clúster: asignar cada punto al centroide más cercano
        for punto in points:
            distancias = [calcular_distancia(punto, centroide) for centroide in centroids]
            cluster_mas_cercano = distancias.index(min(distancias))
            clusters[cluster_mas_cercano].append(punto)

        # Actualización de los centroides
        nuevos_centroids = []
        for i in range(k):
            nuevos_centroids.append(calcular_promedio(clusters[i]))

        # Convergencia: verificar si los centroides no han cambiado
        if nuevos_centroids == centroids:
            break

        centroids = nuevos_centroids

    return clusters, centroids