'''
PART 2.
Create a Python dictionary that returns a list of values for each key.
 The key can be whatever type you want. Its structure has to be like
 this: {'key1': [value1, value2, value3],
  'key2': [value4, value5, value6],
  'key3': [value7, value8, value9]}

Design the dictionary so that it could be useful for something
 meaningful to you. Create at least three different keys on the
 dictionary with a list of at least three elements in it. Invent the
 dictionary yourself. Do not copy the items from some other source.

Consider the invert_dict function provided below.

---------------

def invert_dict(d):
    inverse = dict()
    for key in d:
         val = d[key]
         if val not in inverse:
              inverse[val] = [key]
         else:
              inverse[val].append(key)
    return inverse

---------------

Modify this function so that it can invert your dictionary. In
 particular, the function will need to turn each of the list items
 into separate keys in the inverted dictionary. The value for each
 key in the new dictionary has to be the original dictionary key
 associated to the item.

Describe what is useful about your dictionary. Then describe whether
 the inverted dictionary is useful or meaningful, and why.
'''

'''
He creado un diccionario que indica el día que tengo que cursar las
 asignaturas correspondientes
'''

horario_materias = {
        'Lunes': ['Programación', 'Python', 'Visión por computador'],
        'Martes': ['Machine Learning', 'Estadistica', 'Análisis'],
        'Miércoles': ['PDOO', 'Geometría', 'Algebra']}

def invert_dict(d):
    """
    Invierte un diccionario de listas pasado como argumento

    Parametros
    ----------
    d : diccionario a invertir


    Devuelve
    -------
    inverse : diccionario invertido
    """
    inverse = dict()
    for key in d:
        val = d[key]
        for v in val:
            if v not in inverse:
                inverse[v] = [key]
            else:
                inverse[v].append(key)
    return inverse


def print_dict(d):
    """
    Imprime el diccionario pasado como argumento

    Parametros
    ----------
    d : diccionario a invertir


    Devuelve
    -------
    Impresión del diccionario
    """
    for key in d:
        print("{}:{}".format(key, d[key]))

#--------------------------------------------------

def main():
    print_dict(invert_dict(horario_materias))

if __name__ == "__main__":
    main()

'''
DESCRIPCIÓN DE UTILIDAD:

El diccionario original puede ser útil para una organización de las
 asignaturas de un alumno por días.

El diccionario invertido permite obtener al instante que días tiene
 cada asignatura.
'''
