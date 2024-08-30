# Fundamentos-de-programación en Python

## Grupo 6 - Participantes

- Alejandro Almendras
- Liuva Salas
- Xiorely Herrera
- Andrea Alvarez


## Descripción del proyecto

La empresa ADL fue contratada para desarrollar una App en Python que permite jugar una trivia interactiva. Esta App tendrá preguntas con 3 niveles de dificultad:

- Básica
- Intermedia
- Avanzada.

El mismo jugador define el número de preguntas a responder correspondientes a cada nivel de dificultad, y gana al responder todas las preguntas correctamente.
Las preguntas deben aparecer en un orden aleatorio, y además cada vez que alguien ejecute la app las alternativas deben ser cambiadas de orden para evitar que alguien encuentre algún patrón de resolución.

Items necesarios:

- Menu Interactivo que permita al usuario seleccionar si quiere o no jugar la trivia.
- Mostrar la pregunta y las opciones apra que el usuario pueda ingresar la respuesta.
- Dar al usuario la opcion de si quiere seguir jugando o parar.
- limpiar la consola al usuario para que la interaccion sea mas limpia.


## Contenido

Este repositorio contiene los modulos con las funciones que se ejecutan dentro de la trivia:

- level.py: selecciona el nivel de cada pregunta de acuerdo al numero de pregunta que se va a mostrar.
- preguntas.py: muestra las preguntas con sus alternativas.
- prueba.py: archivo mas pequeño para probar funcionamiento mas simple.
- question.py: permite escoger la pregunta y randomiza las alternativas.
- shuffle.py: funcion que toma las alternativas y las randomiza.
- validador.py: valida las opciones versus un valor otorgado.
- verify.py: verifica que la respuesta sea correcta.

## Prerrequisitos o Dependencias

Lista de software y herramientas, incluyendo versiones, que necesitas para instalar y ejecutar este proyecto:

- Sistema Operativo Windows, Linux MacOS
- Lenguaje de programación Python 3.12


## Instalación del Proyecto

Puedes realizar un fork desde tu Github, o clonar mi proyecto.

```bash
git clone git@github.com:Xiorelyh/Prueba-Fundamentos-de-programacion-en-Python.git
```

## Instrucciones para Ejecutar el Proyecto

Instrucciones para ejecutar el proyecto una vez instalado.

```Windows Powershell
Abrir consola "Windows Powershell" en la ubicación donde se aloja el proyecto y ejecutar el siguiente comando:

# python .\main.py <seleccionar entre las opciones del menu.>
```

## Autor

- [Liuva Salas](https://github.com/LiuvaSalas)
- [Alejandro Almendras](https://github.com/Almendras2024)
- [Andrea Alvarez](https://github.com/Andrea-Alvarez-Gonzalez)
- [Xiorely Herrera](https://github.com/Xiorelyh)

## Licencia

Este proyecto está bajo la Licencia MIT - ve el archivo [LICENSE.md](LICENSE) para detalles
