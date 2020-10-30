'''
Modify your program from PART 2 to read dictionary items from a file
and write the inverted dictionary to a (different) file. You will
need to decide on the following:

How to format each dictionary item as a text string in the input file.

How to covert each input string into a dictionary item.

How to format each item of your inverted dictionary as a text string
in the output file.

Create an input file with your original three-or-more keys  and add at
least three new keys, for a total of at least six keys (with at least
three elements on each).
'''

'''
Desiciones de diseño:

Se ha decidido codificar un diccionario en el archivo de texto de
 entrada como:
  - En la primera línea el nombre del diccionario
  - De la segunda línea hasta el final del documento los pares
   clave-valores introducidos como 'clave:valores' donde los valores
   se dividen con comas.

'''

from ejercicio2 import invert_dict

'''
Se podría incluir para pedir por pantalla, pero no lo he hecho
por no pedirse
'''

ruta_fichero_entrada = "./archivo_entrada_1.txt"
ruta_fichero_salida = "./archivo_salida.txt"
END_LINE = '\n'
END_KEY = ':'
COMMA = ','

def leer_diccionario(ruta_fichero_entrada = "./archivo_entrada.txt"):
    """
    Lee un diccionario de la ruta especificada

    Parametros
    ----------
    ruta_fichero_entrada : ruta del fichero de entrada


    Devuelve
    -------
    nombre_diccionario : string que indica el nombre del diccionario
    diccionario : diccionario leído
    """
    # Se lee con la función open (se podría tratar con excepciones)
    # y se separa en una lista por líneas.
    temp = open(ruta_fichero_entrada, 'r').read().split('\n')
    # Se obtiene el nombre del diccionario y se elimina de la lista
    nombre_diccionario = temp[0]
    diccionario = dict()
    temp.pop(0)
    # Para cada linea (clave-valores)
    for line in temp:
        # Se separa la clave de los valores
        line = line.split(END_KEY)
        # Si existe la clave
        if(line[0]):
            key = line[0]
            values = line[1]
            # Se separan los valores
            values = values.split(COMMA)
            # Para cada valor se incluye
            for value in values:
                if key not in diccionario:
                    diccionario[key] = [value]
                else:
                    diccionario[key].append(value)
    return nombre_diccionario, diccionario


def escribir_diccionario(diccionario,
                        ruta_fichero_salida = "./archivo_salida.txt",
                        sufijo_nombre = '_invertido',
                        nombre_diccionario = 'diccionario'):
    """
    Escibe un diccionario de la ruta especificada pero invertido

    Parametros
    ----------
    diccionario : diccionario a escribir en el fichero de salida
    ruta_fichero_salida : ruta del fichero de salida
    sufijo_nombre : sufijo que se le añade al nombre del diccionario
    nombre_diccionario : nombre del diccionario

    Devuelve
    -------
    No devuelve nada, solo la escritura en el fichero de salida
    """
    diccionario_invertido = invert_dict(diccionario)
    file = open(ruta_fichero_salida, 'w')
    file.write(nombre_diccionario + sufijo_nombre + END_LINE)
    for key in diccionario_invertido:
        file.write(key + END_KEY)
        values = diccionario_invertido[key]
        for value in values[:-1]:
            file.write(value + COMMA)
        file.write(values[-1])
        file.write(END_LINE)
    file.close()

def comprobacion(ruta_fichero_entrada = "./archivo_salida.txt"):
    """
    Funcion de testeo: lee el diccionario del fichero y lo imprime

    Parametros
    ----------
    ruta_fichero_entrada : ruta del fichero donde se lee el diccionario

    Devuelve
    -------
    Impresión del diccionario leído
    """
    nombre, diccionario = leer_diccionario(ruta_fichero_entrada)
    print("Nombre del diccionario invertido: {}".format(nombre))
    print(diccionario)


#--------------------------------------------------

def main():
    # Se obtiene el diccionario leído
    nombre, diccionario = leer_diccionario(ruta_fichero_entrada)
    # Se invierte y se escribe
    escribir_diccionario(diccionario = diccionario,
                            ruta_fichero_salida = ruta_fichero_salida,
                            nombre_diccionario=nombre)
    # Función de testeo
    comprobacion(ruta_fichero_entrada = ruta_fichero_salida)


if __name__ == "__main__":
    main()
