#CSV
import csv

#Lee archivo CSV y devuelve lista de diccionarios
def archivo_csv_leer(ruta_archivo):
    paises = []

    try:
        with open (ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                try:
                    #Se validan y convierten los tipos de datos
                    pais = {"nombre": fila["nombre"].strip(), "poblacion": int(fila["poblacion"].strip()), "superficie": int(fila["superficie"].strip()), "continente": fila["continente"].strip()}
                    paises.append(pais)
                #En caso de un mal dato númerico en CSV, se omitira la fila
                except ValueError:
                    error_nombre = fila.get("nombre", "Desconocido")
                    print (f"Se detecto un error de formato en la Superficie / Poblacion de: {error_nombre}. Se recomienda verificar la ruta.")
                except KeyError as e:
                    print (f"Falta la columna {e} en el CSV.")
                    return []
                    #Se detiene la ejecucion si el archivo CSV no esta correctamente estructurado

        print ("Los datos se han cargado correctamente.")
    
    except FileNotFoundError:
        print (f"No se pudo encontrar el archivo {ruta_archivo}. Se recomienda verificar la ruta.")
    except Exception as e:
        print (f"Ocurrio un error inesperado al leer el archivo {e}")

    return paises

def agregar_pais (paises, nombre, poblacion, superficie, continente):
    #Validar strings (vacios)
    if not nombre.strip() or not continente.strip():
        print ("El Nombre y el Continente no puedan estar vacios.")
        return False
    
    #Validación númerica (coherencia)
    if poblacion <= 0 or superficie <= 0:
        print ("Población y Superficie deben ser números enteros mayores a 0.")
        return False

    #Validación de repetición (duplicados)
    for p in paises:
        if p["nombre"].lower() == nombre.lower().strip():
            print (f"El país {nombre} ya se encuentra en el sistema.")
            return False
        
    #Diccionario
    nuevo_pais = {"nombre": nombre.strip(), "poblacion": poblacion, "superficie": superficie, "continente": continente.strip()}
    paises.append(nuevo_pais)
    print (f"El país {nombre} fue agregado con éxito.")

def actualizar_pais (paises, nombre, nueva_poblacion, nueva_superficie):
    #Validar entradas
    if nueva_poblacion <= 0 or nueva_superficie <= 0:
        print ("Los valores tienen que ser mayores a 0.")
        return False

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower().strip():
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            print (f"Los datos de {pais["nombre"]} han sido actualizados correctamente.")
            return True
    
    print (f"No se pudo encontrar el pais {nombre} para actualizar.")
    return False

# Funcion de busqueda de paises por coincidencia parcial en el nombre.
# Ej: Si se busca "ar", muestra todos los paises registrados que contengan esta secuencia de caracteres (argentina, argelia, armenia).
def buscar_paises_por_nombre(nombre, paises):
    coincidencias = [p for p in paises if nombre.lower().strip() in p['nombre'].lower()]  # Guarda las coincidencias en una lista

    if not coincidencias:  # Lista vacia.
        print('No se encontraron coincidencias.')
        return None  # Devuelve una lista vacia
    
    elif len(coincidencias) == 1:
        print(f"Se ha encontrado una coincidencia: {coincidencias[0]['nombre']}.")
        return coincidencias[0]  # Devuelve el diccionario con los datos del pais encontrado.
    
    elif len(coincidencias) > 1:
        print(f"Se han encontrado {len(coincidencias)} coincidencias:")
        print('0) Ninguno')
        for i, pais in enumerate(coincidencias):
            print(f"{i+1}) {pais['nombre']}")  # Imprime todas las coincidencias encontradas.

        try:
            coincide = int(input('Seleccione el pais que busca: '))  # Permite elegir una opcion entre las coincidencias.
            if coincide < 0 or coincide > len(coincidencias):
                print('ERROR: Valor fuera de rango.')
            elif coincide == 0:
                return None  # En el caso de elegir "Ninguno" se retorna una lista vacia.
            else:
                return coincidencias[coincide-1]  # Devuelve el diccionario del pais
        except ValueError:
            print('ERROR: Ingrese un valor valido.')
            return None  # Si se elige una opcion por fuera de las que se muestran se devuelve una lista vacia.

def filtrar_paises_por_continente(continente,paises):
    if len(paises) == 0:
        print('Aun no se han registrado datos.')
    else:
        encontrado = False
        for c in paises:
            if c['continente'].lower() == continente.lower().strip():
                print(f"Pais: {c['nombre']} | Poblacion: {c['poblacion']} habitantes | Superficie: {c['superficie']} km².")
                encontrado = True

        if not encontrado:
            print('No se encontraron coincidencias.')

def filtrar_por_rango(valor_min,valor_max,categoria,paises):
    if categoria.strip().lower() == 'poblacion':
        encontrado = False

        for p in paises:
            if valor_min <= p['poblacion'] <= valor_max:
                print(f"Pais: {p['nombre']} | Poblacion: {p['poblacion']} habitantes | Superficie: {p['superficie']} km² | Continente: {p['continente']}.")
                encontrado = True

        if not encontrado:
            print('No se encontraron paises dentro de este rango de poblacion.')

    elif categoria.strip().lower() == 'superficie':
        encontrado = False
        for p in paises:
            if valor_min <= p['superficie'] <= valor_max:
                print(f"Pais: {p['nombre']} | Poblacion: {p['poblacion']} habitantes | Superficie: {p['superficie']} km² | Continente: {p['continente']}.")
                encontrado = True

        if not encontrado:
            print('No se encontraron paises en este rango de superficie.')
    else:
        print('ERROR: Ingrese una categoria valida.')

def ordenar_paises(categoria,orden,paises):
    categorias_validas = ['nombre','poblacion','superficie']
    cat = categoria.lower().strip()
    ord_ = orden.lower().strip()

    if cat not in categorias_validas:
        print('ERROR: Categoria invalida.')
        return
    if ord_ not in ['ascendente', 'descendente']:
        print('ERROR: Orden invalido.')
        return
    ordenado = sorted(paises, key = lambda p: p[cat], reverse = (ord_ == 'descendente'))
    for p in ordenado:
        print(f"Pais: {p['nombre']} | Poblacion: {p['poblacion']} habitantes | Superficie: {p['superficie']} Km² | Continente: {p['continente']}.")

def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print('Aun no se han registrado datos.')
        return
    # Paises con mayor y menor poblacion.
    mayor = paises[0]
    menor = paises[0]
    for p in paises:
        if p['poblacion'] > mayor['poblacion']:
            mayor = p
        if p['poblacion'] < menor['poblacion']:
            menor = p
    print(f'Pais con mayor poblacion: {mayor['nombre']}')
    print(f'Pais con menor poblacion: {menor['nombre']}\n')
    print('=================================================\n')
    
    # Promedio de poblacion y superficie.
    poblacion_total = 0
    superficie_total = 0
    for p in paises:
        poblacion_total += int(p['poblacion'])
        superficie_total += float(p['superficie'])
    promedio_poblacion = poblacion_total/len(paises)
    promedio_superficie = superficie_total/len(paises)
    print(f'Promedio de poblacion: {promedio_poblacion:.2f} habitantes.')
    print(f'Promedio de superficie: {promedio_superficie:.2f} Km²\n')
    print('=================================================\n')

    # Cantidad de paises por continente.
    conteo = {}
    for p in paises:
        continente = p['continente']
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1
    for continente in conteo:
        print(f"Continente: {continente} | Cantidad de paises: {conteo[continente]}.")
    print('=================================================\n')
