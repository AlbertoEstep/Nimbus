'''
Consider the following code:

---------------

    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        print(letter + suffix)

------------

Notice that it prints the names "Oack" and "Qack".

Modify the program so that it prints "Ouack" and "Quack" but leaves
 the other names the same.
'''

prefixes = 'JKLMNOPQ'
suffix = 'ack'
def AddPrefixToSuffix(prefixes='JKLMNOPQ', suffix ='ack',
            especial_letter = 'u', especial_prefixes = ['O', 'Q']):
    """
    Imprime cada prefijo concatenado con la cadena de sufijos, salvo
     para los prefijos especiales.

    Parametros
    ----------
    prefixes : string de prefijos
    suffix: string de sufijos
    especial_letter : string a concatener con los prefijos especiales
    especial_prefixes: prefijos especiales a tomar en cuenta

    Devuelve
    -------
    Impresión en pantalla de la concatenación entre sufijos y prefijos
    """
    for letter in prefixes:
        if letter in especial_prefixes:
            print(letter + especial_letter + suffix)
        else:
            print(letter + suffix)

'''
AddPrefixToSuffix(prefixes='JKLMNOPQ', suffix ='ack',
        especial_letter = 'u',  especial_prefixes = ['O', 'Q'])
'''
AddPrefixToSuffix()



'''
OTRA FORMA
def AddPrefixToSuffixLista(prefixes='JKLMNOPQ', suffix ='ack',
            especial_letter = 'u', especial_prefixes = ['O', 'Q']):
    """
    Devuelve una lista con cada prefijo concatenado con la cadena
     de sufijos, salvo para los prefijos especiales.

    Parametros
    ----------
    prefixes : string de prefijos
    suffix: string de sufijos
    especial_letter : string a concatener con los prefijos especiales
    especial_prefixes: prefijos especiales a tomar en cuenta

    Devuelve
    -------
    Impresión en pantalla de la concatenación entre sufijos y prefijos
    """
    return [letter + suffix
                if letter not in especial_prefixes
                else letter + especial_letter + suffix
                    for letter in prefixes ]


print(AddPrefixToSuffixLista())
'''
