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