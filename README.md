# Sistema de Gestión de Datos de Países

## Descripción del Proyecto

Este proyecto es un Trabajo Práctico Integrador (TPI) desarrollado para la materia Programación 1. Consiste en una aplicación de consola escrita completamente en Python que permite gestionar una base de datos de países. El sistema inicializa cargando datos desde un archivo de texto plano (`paises.csv`) y provee una interfaz interactiva para realizar operaciones de alta, actualización, búsqueda, filtrado múltiple, ordenamiento y cálculo de estadísticas globales.

## Intengrantes y Participación

**Ivan Ezequias Cardozo / Integrante A:** Desarrolló la lógica de carga de datos mediante la lectura del archivo CSV (incluyendo el manejo robusto de excepciones y validaciones), el diseño del menú principal interactivo, y las funciones fundamentales para agregar nuevos países y actualizar sus registros numéricos.

**Ivan Cukla / Intengrante B:** Desarrolló el motor de búsqueda por coincidencia parcial, los algoritmos de filtrado (por continente y rangos numéricos), los ordenamientos dinámicos (ascendente/descendente) y el módulo de cálculo de estadísticas globales (máximos, mínimos y promedios).

## Ejemplos de Entradas y Salidas

**Ejemplo 1: Buscar un país por coincidencia parcial**

* **Entrada:** `Opción 3` -> Término a buscar: `"arg"`
* **Salida:**
    ```text
    Se ha encontrado una coincidencia: Argentina.
    ```

**Ejemplo 2: Filtrar por continente**

* **Entrada:** `Opción 4` -> Sub-Opción "a" -> Continente: `"América"`
* **Salida:**
    ```text
    Pais: Argentina | Poblacion: 45376763 habitantes | Superficie: 2780400 km².
    Pais: Brasil | Poblacion: 213993437 habitantes | Superficie: 8515767 km².
    Pais: Canadá | Poblacion: 38000000 habitantes | Superficie: 9984670 km².
    ...
    ```

**Ejemplo 3: Mostrar estadísticas globales**

* **Entrada:** `Opción 6`
* **Salida:**
    ```text
    Pais con mayor poblacion: China
    Pais con menor poblacion: Fiyi
    =================================================
    Promedio de poblacion: 182603848.47 habitantes.
    Promedio de superficie: 2516421.27 Km²
    ...
    ```

## Instrucciones de Instalación y Uso

Este proyecto no requiere la instalación de librerías externas de terceros, ya que utiliza únicamente los módulos nativos de Python.

1. **Clonar el repositorio** en tu máquina local mediante Git:
    ```bash
    git clone [https://github.com/Strivander/tpi-programacion.git]
    ```

2. Asegurarse de tener instalado **Python 3.x** en el sistema.

3. Verificar que el archivo de datos base **paises.csv** se encuentre ubicado en la misma carpeta raíz que el script principal.

4. Abrir una terminal en la carpeta del proyecto y ejecutar el programa:
    ```bash
    python main.py
    ```

## Enlaces Obligatorios

A continuación se encuentran los enlaces a los entregables correspondientes de este Trabajo Práctico Integrador:

* **Documentación Académica (PDF):** [Ver informe detallado](https://github.com/Strivander/tpi-programacion/blob/main/Sistema_de_Gestion_de_Datos_Informe.pdf)
* **Video Demostrativo:** [Ver presentación del sistema](https://youtu.be/-Q5w8SN8368)
