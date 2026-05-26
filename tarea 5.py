# # Programa: Promoción menú restaurante
# Autor: Jazmin Rativa Moreno
# -----------------------------------------

# Matriz del menú 4 productos y su categoria 

# definimos primero las constantes que vamos a ocupar
CATEGORIA_OBJETIVO = "Comida Italiana"
UMBRAL_PRECIO = 20000

# luego definimos la Matriz del menú: ["Nombre", "Categoría", Precio Base]
menu = [
    ["Hamburguesa", "Comida Rapida", 15000],
    ["Pizza", "Comida Italiana", 35000],
    ["Ensalada", "Saludable", 10000],
    ["Jugo Natural", "Bebidas", 6000],
    ["Pasta", "Comida Italiana", 15000],
    ["Lasagna", "Comida Italiana", 20000]
]

# esto de aqui abajo es un docstring, necesario cuando creamos funciones
'''Función que calcula el descuento del 15% si cumple los requisitos'''
def calcular_precio_final(categoria, precio_base):

    # aqui Evaluamos usando las constantes que definimos al principio
    if categoria == CATEGORIA_OBJETIVO and precio_base >= UMBRAL_PRECIO:
        # Multiplicar por 0.85 aplica el 15% de descuento directamente y nos ahorramos un par de lineas
        precio_final = precio_base * 0.85  
        promocion = "Sí"
    else:
        precio_final = precio_base
        promocion = "No"

    #Retornamos el precio final redondeado a entero y la promocion aplicada v 
    return round(precio_final), promocion


# Imprimimos el reporte en una tabla para que sea mas legible xd
print("=================== REPORTE DE MENÚ Y PROMOCIONES ===================")
print(f"{'PRODUCTO':<15} | {'CATEGORÍA':<16} | {'P. BASE':<9} | {'P. FINAL':<9} | {'PROMO':<5}")
print("-" * 69)

# Ciclo optimizado: Desempaquetamos los 3 datos de la fila de una sola vez pa ahoorar lineas d codigo
for nombre, categoria, precio_base in menu:
    
    # Llamamos a la función pasándole solo lo necesario pue
    precio_final, promocion = calcular_precio_final(categoria, precio_base)
    
    # Imprimimos la fila alineada con los :< 
    print(f"{nombre:<15} | {categoria:<16} | ${precio_base:<8,.0f} | ${precio_final:<8,.0f} | {promocion:<5}")