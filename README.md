# Trabajo Final Integrador - Algoritmos y Estructuras de Datos

## Información General
* **Institución:** UTN - Facultad Regional Resistencia (FRRe)
* **Carrera:** Ingeniería en Sistemas de Información (ISI)
* **Comisión:** D
* **Escenario Asignado:** 11. Sistema de alquiler de bicicletas

## Integrantes del Grupo
* Bautista Lago Escobar - Legajo: 26658
* Lisandro Jara  - Legajo: 30089
* Dahiana Cano  - Legajo: 28821
* Acosta Lourdes - Legajo: 30339
* Cardozo Lucia Marlen - Legajo: 28819

## Descripción General del Sistema
Este proyecto consiste en un sistema de gestión en consola para el alquiler de bicicletas dentro de un parque. Desarrollado íntegramente en Python, el programa permite:
- Registrar clientes y controlar el stock de bicicletas disponibles.
- Finalizar alquileres calculando el importe en base a las horas de uso.
- Manejar errores mediante validaciones de tipo de dato para evitar caídas del programa.
- Mostrar estadísticas en tiempo real sobre la recaudación y el uso general del servicio.
El sistema está modularizado mediante funciones específicas y utiliza variables contadoras y acumuladoras para llevar la gestión económica y estadística.

## Instrucciones de Ejecución
1. Asegurarse de tener instalado Python 3.x en el equipo.
2. Clonar este repositorio o descargar los archivos fuente.
3. Abrir una terminal o línea de comandos en el directorio del proyecto.
4. Ejecutar el script principal mediante el comando:
   `python sistema_bicicletas.py`
5. Seguir las instrucciones del menú interactivo en la consola.

## Uso de Inteligencia Artificial (Declaración)
En el marco de la consigna de la cátedra, detallamos el uso de herramientas de IA durante el desarrollo:
* **Herramienta utilizada:** Gemini.
* **Propósito:** Test meticuloso del codigo, propuesta de modularización (funciones) y asistencia en la creatividad para los menus.
* **Proceso crítico:** Se adaptaron los nombres de las variables para mayor legibilidad y se decidió unificar el registro de clientes activos mediante un diccionario en memoria, asegurando que todos los miembros del equipo comprendan la lógica de actualización de los contadores (`total_recaudado`, `total_alquileres`).