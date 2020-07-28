#2. Consulta de Funciones
from Panel_General_de_Funciones import guardar_nombres
def leer_fuente(ar_fuente,Max_linea):
    """
    [Autor: Patrick Soto]
    [Ayuda: lee el archivo fuente_unico.csv, devolviendo la linea o
    devolviendo Max_linea si se llega al fin de archivo]
    """
    linea = ar_fuente.readline()
    if linea:
        devolver = linea.rstrip('\n').split(',')
    else:
        devolver = Max_linea
    return devolver

def leer_comentarios(ar_comentarios,Max_linea):
    """
    [Autor: Patrick Soto]
    [Ayuda: lee el archivo comentarios.csv, devolviendo el comentario o
    devolviendo Max_linea si se llega al fin de archivo]
    """
    comentario = ar_comentarios.readline()
    if comentario:
        continuar = comentario.rstrip('\n').split(',')
    else:
        continuar = Max_linea
    return continuar


def sub_listas(ar_fuente,lista_principal):
    """
    [Autor: Patrick Soto]
    [Ayuda:Recorre la lista de funciones y crea 2 sublistas,con la mitad,
    de funciones en una lista y la otra mitad en la otra si es par y si es
    impar la lista_1 es mayor a la lista_2]
    """
    lista_1 = []
    lista_2 = []
    longitud_principal = len(lista_principal)
    n = 0 #contador,para pasar a guardar en la lista_2     
    for funcion in lista_principal:
        if longitud_principal/2 == longitud_principal//2: #compruebo si es par
            if n < longitud_principal/2:
                lista_1.append(funcion)
                n += 1
            else: lista_2.append(funcion)
        else:#al ser impar, en la lista_1 guarda la mitad mas uno
            if n <= longitud_principal//2:
                lista_1.append(funcion)
                n += 1
            else: lista_2.append(funcion)
    return lista_1,lista_2,longitud_principal

def listar_funciones(ar_fuente,lista_principal):
    """
    [Autor: Patrick Soto]
    [Ayuda:Creo una lista transitoria, en la cual voy guardando los elementos,
    de las 2 listas iterando con un for, caundo llego a 2 elementos en la lista
    paso a imprmir y elimino todos los elementos de la lista transitoria]
    """
    lista_1,lista_2,longitud_principal = sub_listas(ar_fuente,lista_principal)
    lista_t = []
    for funcion1,funcion2 in zip(lista_1,lista_2):
        lista_t.append(funcion1)
        lista_t.append(funcion2)
        if len(lista_t) == 2:#Compruebo si llegue a los 2 elementos
            imprimir_tabla(ar_fuente,lista_1,lista_t[0],lista_t[1])
            lista_t.clear()
    """Si la longitud de la lista_principal es impar, pasa a imprimir al final,
    solo el ultimo elemento de la lista_1"""
    if longitud_principal/2 != longitud_principal//2:
        imprimir_tabla(ar_fuente,lista_1,lista_1[-1],"")

def imprimir_tabla(ar_fuente,lista_1,primero,segundo):
    """
    [Autor: Patrick Soto]
    [Ayuda: Imprime las funciones en una tabla, por medio de tabulaciones]
    """
    barra = '|'
    parentesis = '()'
    if primero == lista_1[0]:#Esto controla que solo se imprima una vez esta parte
        print('+-------------------------------------------------------------------------------+')
        print('|                                funciones                                      |')
        print('|-------------------------------------------------------------------------------|')
    if len(segundo) == 0:
        parentesis = ""
    print('{0:1}\t{1:30}\t{2:1}\t{3:30}\t{4:1}'.format(barra,primero+parentesis,barra,segundo+parentesis,barra))
    if primero == lista_1[-1]:#Comprueba que ha llegado al ultimo elemento de la lista
        print('+-------------------------------------------------------------------------------+')
        
def ingreso_funcion(ar_fuente,ar_comentarios,lista_principal,Max_linea):
    """
    [Autor: Patrick Soto]
    [Ayuda: Recibe una funcion y evalua si es valida o no,comparando la funcion
    ingresada con la lista de funciones]
    """
    ar_comentarios.seek(0)
    ar_fuente.seek(0)
    comentario = leer_comentarios(ar_comentarios,Max_linea)
    linea,pase = leer_fuente(ar_fuente,Max_linea),True
    funcion = input("Ingrese funcion o presione enter para terminar:")
    #Evalua si la funcion ingresada es valida
    while funcion != "?todo" and funcion != "#todo" and funcion != "imprimir?todo" and pase:
        if funcion[:-1] not in lista_principal  and funcion != "":
            funcion = input("funcion invalida por favor reingrese funcion o presione enter para terminar:")
        else:
            while funcion[:-1] != linea[0]:
                #Si la funcion no esta en la linea, pasa a la siguiente linea,tanto de fuente_unico como de comentarios
                comentario = leer_comentarios(ar_comentarios,Max_linea)
                linea = leer_fuente(ar_fuente,Max_linea)
            pase = False #Me sirve para salir del while principal
    return funcion,comentario,linea

def evalua_funcion(ar_fuente,ar_comentarios,ar_ayuda,lista_principal,Max_linea):
    """
    [Autor: Patrick Soto]
    [Ayuda: Evalua que es lo que le piden, segun lo ingresado]
    """ 
    funcion,comentario,linea = ingreso_funcion(ar_fuente,ar_comentarios,lista_principal,Max_linea)
    while funcion != "":
        ar_comentarios.seek(0)
        ar_fuente.seek(0)
        if "?" in funcion and funcion != "?todo" and funcion != "imprimir?todo":
            imprimir("",str(comentario[1:]),linea)
        elif "#" in funcion and funcion != "#todo":
            codigo = str(linea[3:])
            imprimir(codigo,str(comentario[1:]),linea,True)
        elif funcion == "?todo":
            listar_comentarios(ar_fuente,ar_comentarios,Max_linea)
        elif funcion == "#todo":
            listar_todo(ar_fuente,ar_comentarios,Max_linea)
        else:#Si se ingresa imprimir?todo
            archivo_ayuda(ar_comentarios,ar_ayuda,ar_fuente,Max_linea)
        #Termina lo solicitado y vuelve a pedir el ingreso de una funcion
        funcion,comentario,linea = ingreso_funcion(ar_fuente,ar_comentarios,lista_principal,Max_linea)
        
def imprimir(leyenda,dato,linea,separador = False):
    """
    [Autor: Patrick Soto]
    [Ayuda: Imprime lo solicitado, si existe un separador, imprime la descripcion
    y luego el codigo]"""
    descripcion = dato.replace(',','')
    print('funcion :',linea[0])
    print('parametros :',linea[1])
    print('modulo :',linea[2])
    print('descripcion :',descripcion.strip('[]'))
    if separador:
        print("")
        codigo = leyenda.replace(',','')
        print('codigo :',codigo.strip('[]'))
        print("================================================================================")
        
        
def listar_comentarios(ar_fuente,ar_comentarios,Max_linea):
    """
    [Autor: Patrick Soto]
    [Ayuda: Recorre el archivo comentarios, imprimiendo cada linea, seguido de un
    separador, hasta llegar al fin de archivo, esto ocurre cuando se ingresa ?todo]
    """
    linea = leer_fuente(ar_fuente,Max_linea)
    comentario = leer_comentarios(ar_comentarios,Max_linea)
    while comentario != Max_linea and linea != Max_linea:#Controla que no halla llegado al fin de archivo
        descripcion = str(comentario[1:])
        print('funcion :',linea[0])
        print('parametros :',linea[1])
        print('modulo :',linea[2])
        print('descripcion :',descripcion.strip('[]'))
        print("===================================================================================")
        linea = leer_fuente(ar_fuente,Max_linea)
        comentario = leer_comentarios(ar_comentarios,Max_linea)
        
def listar_todo(ar_fuente,ar_comentarios,Max_linea):
    """
    [Autor: Patrick Soto]
    [Ayuda Recorre el archivo fuente y comentarios, guardando la linea y
    el comentario y mandandola a la funcion imprimir, esto ocurre cuando,
    se ingresa #todo]
    """
    linea = leer_fuente(ar_fuente,Max_linea)
    comentario = leer_comentarios(ar_comentarios,Max_linea)
    while linea != Max_linea and comentario != Max_linea:#Controla que no halla llegado al fin de archivo, de ninguno de los 2
        codigo = str(linea[3:])
        imprimir(codigo,str(comentario[1:]),linea,True)
        linea = leer_fuente(ar_fuente,Max_linea)
        comentario = leer_comentarios(ar_comentarios,Max_linea)
        
def archivo_ayuda(ar_comentarios,ar_ayuda,ar_fuente,Max_linea):
    """
    [Autor: Patrick Soto]
    [Ayuda: Recorre el achivo comentarios, almacenando los caracteres en una
    variable y manda a grabar]
    """
    linea = ar_comentarios.readline()
    i,f = 0,80
    # i es el inicio y f el final
    while linea != '':
        linea_limpia = linea.replace(',','')#Le quita las comas a la linea
        linea2 = linea_limpia[i:f]
        longitud = len(linea_limpia)
        unica_vez = True #unica_vez me sirve para imprimir los paremetros y el modulo, solamente al principio de cada comentario
        if longitud > 80:#Evalua si la linea tiene mas de 80 caracteres
            while len(linea2) == 80:
                """Aqui va la condicion voy almacenando de 80 en 80, hasta que,
                me quede menos de 80 caracteres en esa linea"""
                linea2 = linea_limpia[i:f]#Guarda en linea1 los 80 caracteres de la linea limpia
                grabar_archivo(ar_ayuda,linea2,ar_fuente,unica_vez,Max_linea)
                #luego de grabar avanza 80 tanto en i como en f
                unica_vez = False #Despues que los imprimio, se vuelve False
                i += 80
                f += 80
            #Cuando termino con la linea, vuelve a la i y la f del principio
            i,f = 0,80
        else:#Si es menos de 80 caracteres, graba directamente la linea
            grabar_archivo(ar_ayuda,linea2,ar_fuente,unica_vez,Max_linea)
        linea = ar_comentarios.readline()
        
def grabar_archivo(ar_ayuda,linea2,ar_fuente,unica_vez,Max_linea):
    """
    [Autor: Patrick Soto]
    [Ayuda: graba la linea recibida en ayuda_funciones.txt]
    """
    if unica_vez:#Graba una unica vez, por cada funcion
        linea1 = leer_fuente(ar_fuente,Max_linea)
        funcion,parametros,modulo = ('funcion :'+linea1[0]),('parametros :'+linea1[1]),('modulo :'+linea1[2])
        ar_ayuda.write(funcion + '\n')
        ar_ayuda.write(parametros + '\n')
        ar_ayuda.write(modulo + '\n')
        ar_ayuda.write('descripcion :' + '\n')
        ar_ayuda.write(linea2 + '\n')
    else:
        ar_ayuda.write(linea2 + '\n')
    
def consulta_funciones():
    """
    [Autor: Patrick Soto]
    [Ayuda: Abre los archivos fuente.csv, comentarios.csv y crea el archivo.txt]
    """
    ar_fuente = open('fuente_unico.csv','r')
    ar_comentarios = open('comentarios.csv','r')
    ar_ayuda = open('ayuda_funciones.txt','w')
    Max_linea = ("","","","","","","","","","","","","","")
    lista_principal = guardar_nombres(ar_fuente)
    listar_funciones(ar_fuente,lista_principal)
    evalua_funcion(ar_fuente,ar_comentarios,ar_ayuda,lista_principal,Max_linea)
    archivo_ayuda(ar_comentarios,ar_ayuda,ar_fuente,Max_linea)
    ar_fuente.close()
    ar_comentarios.close()
    ar_ayuda.close()


    

    



                

        


