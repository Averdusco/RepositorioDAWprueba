array = ["indigo", "groc", "verd", "vermell", "blau", "cian", "taronja"]

def longitud(color):
    longitud_de_la_ona = {
        "indigo": 450,
        "groc": 570,
        "verd": 520,
        "vermell": 630,
        "blau": 470,
        "cian": 490,
        "taronja": 600
    }
    
    return longitud_de_la_ona.get(color, 0)

def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if longitud(array[j]) > longitud(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

bubble_sort(array)

print("Array ordenado con Bubble Sort de forma ascendente según longitud de onda:", array)