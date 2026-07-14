productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8.0, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False]
}
stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3]
}
def leer_opcion():
    try:
        opcion_input = input("Ingrese opción: ")
        opcion = int(opcion_input)
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Debe seleccionar una opción válida")
            return None
    except ValueError:
        print("Debe seleccionar una opción válida")
        return None
def buscar_codigo(productos_dict, codigo):
    codigo_limpio = codigo.strip().upper()
    return codigo_limpio in productos_dict
def unidades_categoria(productos_dict, stock_dict, categoria):
    categoria_buscar = categoria.strip().lower()
    total_unidades = 0
    for cod, datos in productos_dict.items():
        categoria_producto = datos[1].lower()
        if categoria_producto == categoria_buscar:
            if cod in stock_dict:
                total_unidades += stock_dict[cod][1]
    print(f"El total de unidades disponibles es: {total_unidades}")
def busqueda_precio(productos_dict, stock_dict, p_min, p_max):
    resultados = [] 
    for cod, datos_stock in stock_dict.items():
        precio = datos_stock[0]
        unidades = datos_stock[1]
        if p_min <= precio <= p_max and unidades > 0:
            if cod in productos_dict:
                nombre_producto = productos_dict[cod][0]
                resultados.append(f"{nombre_producto}--{cod}") 
    if len(resultados) > 0:
        resultados.sort()
        print(f"Los productos encontrados son: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")
def actualizar_precio(productos_dict, stock_dict, codigo, nuevo_precio):
    codigo_upper = codigo.strip().upper()
    if buscar_codigo(productos_dict, codigo_upper):
        stock_dict[codigo_upper][0] = nuevo_precio
        return True
    return False
def validar_codigo(productos_dict, valor):
    valor_clean = valor.strip()
    if valor_clean == "":
        return False
    if buscar_codigo(productos_dict, valor_clean):
        return False
    return True
def validar_nombre(valor):
    return valor.strip() != ""
def validar_categoria(valor):
    return valor.strip() != ""
def validar_marca(valor):
    return valor.strip() != ""
def validar_peso(valor):
    try:
        peso = float(valor)
        return peso > 0
    except ValueError:
        return False
def validar_es_importado(valor):
    return valor.strip().lower() in ['s', 'n']
def validar_es_para_cachorro(valor):
    return valor.strip().lower() in ['s', 'n']
def validar_precio(valor):
    try:
        precio = int(valor)
        return precio > 0
    except ValueError:
        return False
def validar_unidades(valor):
    try:
        unidades = int(valor)
        return unidades >= 0
    except ValueError:
        return False
def agregar_producto(productos_dict, stock_dict, codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    codigo_upper = codigo.strip().upper()  
    if buscar_codigo(productos_dict, codigo_upper):
        return False
    importado_bool = True if es_importado.strip().lower() == 's' else False
    cachorro_bool = True if es_para_cachorro.strip().lower() == 's' else False
    peso_float = float(peso_kg)
    precio_int = int(precio)
    unidades_int = int(unidades)
    productos_dict[codigo_upper] = [
        nombre.strip(),
        categoria.strip(),
        marca.strip(),
        peso_float,
        importado_bool,
        cachorro_bool
    ]
    stock_dict[codigo_upper] = [precio_int, unidades_int]
    return True
def eliminar_producto(productos_dict, stock_dict, codigo):
    codigo_upper = codigo.strip().upper()
    if buscar_codigo(productos_dict, codigo_upper):
        del productos_dict[codigo_upper]
        del stock_dict[codigo_upper]
        return True
    return False
def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")
def main():
    dict_productos = productos.copy()
    dict_stock = stock.copy()
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion is None:
            continue
        if opcion == 1:
            cat = input("Ingrese categoría a consultar: ")
            unidades_categoria(dict_productos, dict_stock, cat)
        elif opcion == 2:
            while True:
                try:
                    p_min_str = input("Ingrese precio mínimo: ")
                    p_min = int(p_min_str)
                    p_max_str = input("Ingrese precio máximo: ")
                    p_max = int(p_max_str)
                    
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(dict_productos, dict_stock, p_min, p_max)
                        break
                    else:
                        print("Debe ingresar valores lógicos coherentes (mínimo menor o igual a máximo)")
                except ValueError:
                    print("Debe ingresar valores enteros")
        elif opcion == 3:
            while True:
                cod = input("Ingrese código del producto: ")
                nuevo_precio_str = input("Ingrese nuevo precio: ")
                if nuevo_precio_str.isdigit() and int(nuevo_precio_str) > 0:
                    nuevo_p = int(nuevo_precio_str)
                    if actualizar_precio(dict_productos, dict_stock, cod, nuevo_p):
                        print("Precio actualizado")
                    else:
                        print("El código no existe")
                else:
                    print("El precio debe ser un número entero mayor que cero")
                
                repetir = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if repetir != 's':
                    break
        elif opcion == 4:
            cod = input("Ingrese código del producto: ")
            nombre = input("Ingrese nombre: ")
            categoria = input("Ingrese categoría: ")
            marca = input("Ingrese marca: ")
            peso = input("Ingrese peso (kg): ")
            importado = input("¿Es importado? (s/n): ")
            cachorro = input("¿Es para cachorro? (s/n): ")
            precio = input("Ingrese precio: ")
            unidades = input("Ingrese unidades: ")
            v_cod = validar_codigo(dict_productos, cod)
            v_nom = validar_nombre(nombre)
            v_cat = validar_categoria(categoria)
            v_mar = validar_marca(marca)
            v_pes = validar_peso(peso)
            v_imp = validar_es_importado(importado)
            v_cac = validar_es_para_cachorro(cachorro)
            v_pre = validar_precio(precio)
            v_uni = validar_unidades(unidades)
            if not v_cod:
                print("Error: El código está vacío o ya existe en el sistema.")
            elif not v_nom:
                print("Error: El nombre no puede estar vacío.")
            elif not v_cat:
                print("Error: La categoría no puede estar vacía.")
            elif not v_mar:
                print("Error: La marca no puede estar vacía.")
            elif not v_pes:
                print("Error: El peso debe ser un número mayor a cero.")
            elif not v_imp:
                print("Error: Debe ingresar 's' o 'n' para indicar si es importado.")
            elif not v_cac:
                print("Error: Debe ingresar 's' o 'n' para indicar si es para cachorro.")
            elif not v_pre:
                print("Error: El precio debe ser un entero mayor que cero.")
            elif not v_uni:
                print("Error: Las unidades deben ser un entero mayor o igual a cero.")
            else:
                if agregar_producto(dict_productos, dict_stock, cod, nombre, categoria, marca, peso, importado, cachorro, precio, unidades):
                    print("Producto agregado")
                else:
                    print("El código ya existe")    
        elif opcion == 5:
            cod = input("Ingrese código del producto: ")
            if eliminar_producto(dict_productos, dict_stock, cod):
                print("Producto eliminado")
            else:
                print("El código no existe") 
        elif opcion == 6:
            print("Programa finalizado.")
            break
if __name__ == "__main__":
    main()