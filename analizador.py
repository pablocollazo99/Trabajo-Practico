from Panel_General_de_Funciones import guardar_nombres
from Panel_General_de_Funciones import diccionario_invocaciones

def invocaciones(lista_nombres_funciones, fuente):
    """
    [Autor: Pablo Collazo]
    [Ayuda: recibe una lista con las funciones que estan en el proframa
    y leyendo el archivo fuente_unico.csv guarda en un diccionario la 
    cantidad de veces que la funcion llama a otra]
    """
    dic = {}
    linea_fuente = fuente.readline()
    while linea_fuente:
        lista_linea = linea_fuente.split(",")
        func_principal = str(lista_linea[0])
        dic[func_principal] = []
        for x in lista_nombres_funciones:
            cant_apariciones=str(lista_linea[3:]).count(x + "(")
            dic[func_principal].append(cant_apariciones)
        linea_fuente=fuente.readline()
    fuente.seek(0)
    return dic

def invocados(lista_nombres_funciones, fuente):
    """
    [Autor: Pablo Collazo]
    [Ayuda: recibe una lista con las funiones y guarda en un
    diccionario si la funcion es invocada por otra]
    """
    dic2 = {}
    linea_fuente = fuente.readline()
    lista_linea = linea_fuente.split(",")
    for func_principal in lista_nombres_funciones:
        dic2[func_principal] = []
        while linea_fuente:
            lineas = ",".join(lista_linea[3:])
            if func_principal in lineas:
                dic2[func_principal].append("X")
            else:
                dic2[func_principal].append("")
            linea_fuente = fuente.readline()
            lista_linea = linea_fuente.split(",")
        fuente.seek(0)
        linea_fuente = fuente.readline()
    fuente.seek(0)
    return dic2

def diccionario_final(dic, dic2, lista_nombres_funciones):
    """
    [Autor: Pablo Collazo]
    [Ayuda: recibe los dos diccionarios hechos anteriormente y
    los junta para formar uno]
    """
    dic_fin = {}
    for func_principal in lista_nombres_funciones:
        dic_fin[func_principal] = []
        for n in range(len(lista_nombres_funciones)):
            if dic[func_principal][n] == 0 and dic2[func_principal][n] == "":
                dic_fin[func_principal].append("")
            elif dic[func_principal][n] == 0 and dic2[func_principal][n] == "X":
                dic_fin[func_principal].append("X")
            elif dic[func_principal][n] != 0 and dic2[func_principal][n] == "":
                dic_fin[func_principal].append(dic[func_principal][n])
            elif dic[func_principal][n] != 0 and dic2[func_principal][n] == "X":
                dic_fin[func_principal].append(dic[func_principal][n])
    return dic_fin


def tabla(lista_nombres_funciones, dic_invocaciones,dic_fin):
    """
    [Autor: Pablo Collazo]
    [Ayuda: recibe el diccionario final, y un diccionario con el total de
    veces que se llama la funcion y arma , imprime y guarda en un archivo 
    una tabla donde los valores representan la cantidad de veces que la 
    función de la fila, invoca a la función de la columna y la “X” representa,
    la función de la fila, que es invocada por la función de la columna]
    """
    analizador = open("analizador.txt", "w")
    print("{0:30} \t |".format("Funciones"),end = " ")
    analizador.write("{0:30} \t |".format("Funciones"))
    for i in range(1 ,len(lista_nombres_funciones)):
        print("{0:2} \t |".format(i),end = " " )
        analizador.write("{0:2} \t |".format(i))
    print("\n")
    analizador.write("\n")
    for w in range(len(lista_nombres_funciones)):
        print("{0:30} \t | ".format(str(w+1) + "." + lista_nombres_funciones[w]),end = " ")
        analizador.write("{0:30} \t | ".format(str(w+1) + "." + lista_nombres_funciones[w]))
        for x in range(len(dic_fin) + 1):
            print("{0:2} \t | ".format(dic_fin[lista_nombres_funciones[w]][x]),end = " ")
            analizador.write("{0:2} \t | ".format(dic_fin[lista_nombres_funciones[w]][x]))
        print("\n")
        analizador.write("\n")
    print("{0:30} \t | ".format("Total invocaciones"),end = " ")
    analizador.write("{0:30} \t | ".format("Total invocaciones"))
    for n in dic_invocaciones:
        if dic_invocaciones[n] == 0:
            dic_invocaciones[n] = ""
        print("{0:2} \t | ".format(str(dic_invocaciones[n])),end = " ")
        analizador.write("{0:2} \t | ".format(str(dic_invocaciones[n])))
    analizador.close()
   

def analizador():
    """
    [Autor: Pablo Collazo]
    [Ayuda: recibe el archivo fuente_unico.csv y gestiona la tabla analizador]
    """
    fuente = open("fuente_unico.csv", "r")
    lista_nombres_funciones = guardar_nombres(fuente)
    dic_invocaciones = diccionario_invocaciones(fuente, lista_nombres_funciones)
    dic =  invocaciones(lista_nombres_funciones, fuente)
    dic2 = invocados(lista_nombres_funciones, fuente)
    dic_fin = diccionario_final(dic, dic2, lista_nombres_funciones)
    tabla(lista_nombres_funciones, dic_invocaciones, dic_fin)
    fuente.close()

analizador()