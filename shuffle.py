import preguntas as p
import random


def shuffle_alt(pregunta):
    """
    randomiza las alternativas de las preguntas que se le atribuye a la funcion.

    Parametros:
    - pregunta: dict, diccionario con preguntas y alternativas

    Return:
    - Alternativas mezcladas, para que no se consiga un patron.
    """
    # Obtener las alternativas de la pregunta
    alternativas = pregunta["alternativas"]

    # Mezclar las alternativas
    random.shuffle(alternativas)

    return alternativas


if __name__ == "__main__":
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas["basicas"]["pregunta_1"]))
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]