
import random
import os

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    """pide un numero y lo valida entre un rango

    Args:
        mensaje (str): mensaje para el input
        mensaje_error (str): mensaje de error para el input
        minimo (int): minimo que se puede introducir
        maximo (int): maximo que se puede introducir

    Returns:
        int: devuelve un entero validado
    """
    numero = int(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = int(input(mensaje_error))
    return numero

def inicializar_matriz(filas : int , columnas : int , valor_inicial : any) -> list:
    """inicializa una matriz segun el numero de columnas y filas

    Args:
        filas (int): entero que representa la cantidad de filas
        columnas (int): entero que representa la cantidad de columnas
        valor_inicial (any): numero con que se inicaliza todos los valores de la matriz 

    Returns:
        list: devuelve una lista anidada
    """
    matriz = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]

    return matriz

def cargar_participantes(matriz:list[list])->list[list]:
    """carga la mtraiz con los datos que necesitamos

    Args:
        matriz (list[list]): _description_

    Returns:
        list[list]: _description_
    """
   
    I_PARTICIPANTE = 0
    I_JURADO_UNO = 1
    I_JURADO_DOS = 2
    I_JURADO_TRES = 3
    I_PROMEDIO = 4
    partipante = 0
    
    
    for fil in range(len(matriz)):
        partipante +=1
        jurado_uno =  pedir_numero(f'Ingrese nota Jurado 1 para el Participante N* {partipante}: ', 'Error ingrese un numero del 1 al 100: ', 1 , 100)
        jurado_dos =  pedir_numero(f'Ingrese nota Jurado 2 para el Participante N* {partipante}: ', 'Error ingrese un numero del 1 al 100: ', 1 , 100)
        jurado_tres =  pedir_numero(f'Ingrese nota Jurado 3 para el Participante N* {partipante}: ', 'Error ingrese un numero del 1 al 100: ', 1 , 100)
        
        nota_promedio = calcular_promedio(jurado_uno,jurado_dos,jurado_tres)
        
        matriz[fil][I_PARTICIPANTE] = f'Participante {partipante}'
        matriz[fil][I_JURADO_UNO] = jurado_uno
        matriz[fil][I_JURADO_DOS] = jurado_dos
        matriz[fil][I_JURADO_TRES] = jurado_tres
        matriz[fil][I_PROMEDIO] = nota_promedio
        
    
    return matriz

            
def mostrar_matriz(matriz:list[list]):
    """imprime una matriz

    Args:
        matriz (list[list]): recibe una lista anidada
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:<25}', end= ' ')
        print('')  

def imprimir_matriz_encolumnada(matriz: list[list]) -> None:
    for fila in matriz:
        print(f"{fila[0]:<25} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15}")


def ordenar_por_numero(matriz: list[list], operador, fila: int)-> list[list]:
    """ordena una matriz alfabeticamente, tambien funciona con enteros

    Args:
        matriz (list[list]): _recibe una matriz_
        operador (_type_): _recibe parametro de la funcion operator_
        fila (int): _un entero que representa la columna de la matriz que vamos a ordenar_

    Returns:
        _type_: _ddevuelve una lista anidada excluyendo la fila[0]
    """
    for i in range(len(matriz) - 1):
        for j in range(i+1,len(matriz)):
            if operador(matriz[i][fila], matriz[j][fila]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
        
    return matriz


def imprimir_lista_encolumna(lista:list)->None:
    """imprime una lista con espacio a elejir

    Args:
        lista (list): una lista
    """
    for i in range(len(lista)):
        print(f'{lista[i]:<16}' , end = '')
    print(' ')  
    print(' ')  
        
  

def imprimir_por_filas(matriz:list[list], filas:int)->None:
    """imprime las filas que le indiques de una matriz

    Args:
        matriz (list[list]): recibe una matriz
        filas (int): la cantidad de filas que queremos imprimir
    """
    for i in range(filas):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:<15}',end='')
        print('')  


def ordenar_doble_criterio(matriz:list[list],columna_uno:int,columna_dos:int,operador)->list[list]:
    """ordena una matriz por doble criterio

    Args:
        matriz (list[list]): recibe una matriz
        columna_uno (int): primer criterio a comparar
        columna_dos (int): segundo criterio a comparar
        operador (function): la funcion operator que deseamos usar

    Returns:
        list[list]: devulve una matriz ordenada
    """
    for i in range(1,len(matriz) - 1):
        for j in range(i+1,(len(matriz))):
            if operador(matriz[i][columna_uno], matriz[j][columna_uno]):
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar     
            elif matriz[i][columna_uno] == matriz[j][columna_uno]:
                if operador(matriz[i][columna_dos], matriz[j][columna_dos]) or (matriz[i][columna_dos] == matriz[j][columna_dos]):
                            auxiliar = matriz[i]
                            matriz[i]= matriz[j]
                            matriz[j] = auxiliar   
            
    return matriz  


                    
def mostrar_matriz(matriz:list[list]):
    """imprime una matriz

    Args:
        matriz (list[list]): recibe una lista anidada
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'{matriz[i][j]:<15}', end= ' ')
        print('')  

                  
def verificar_si_es_matriz(matriz : list[list])-> bool | list: 
    """verifica si es o no matriz 

    Args:
        matriz (list[list]): matriz

    Returns:
        bool | list: devuelve verdadero o falso
    """
    retorno = False
    if type(matriz) == list:
        for fila in matriz:
            if type(fila) == list:
                retorno = True
           
    return retorno
            
            

    
def imprimir_resultado(matriz:list[list],mensaje:str) -> None:
    """verifica si es matriz o lista y las imprime,imprime mensaje sino

    Args:
        matriz (list[list]): una lista o una matriz 
        mensaje (str): mensaje que queremos dejar en caso de no ser lista o matriz
    """
    if verificar_si_es_matriz(matriz) == True:
        mostrar_matriz(matriz)
    else:
        if type(matriz) == list and len(matriz) > 0:
            imprimir_lista_encolumna(matriz)
        else:
            print(mensaje) 
    
def validad_genero(mensaje:str , mensaje_error:str , genero_a :str , genero_b: str , genero_c: str )->str:
    """valida si ingresamos una de las tres letras que designamos

    Args:
        mensaje (str): _'ingrese x cosa'
        mensaje_error (str): error ingrese x cosa
        genero_a (str): un str
        genero_b (str): un str
        genero_c (str): un str 

    Returns:
        str: un str
    """
    genero = input(mensaje)
    while genero != genero_a and genero != genero_b and genero != genero_c:
        genero = input(mensaje_error)
    return genero

def copiar_matriz(matriz:list[list])->list[list]:
    """esta funcion crea una nueva matriz con los
    mismos valores que la pasada por parametro, su mismas
    dimensiones

    Args:
        matriz (list[list]): _description_

    Returns:
        list[list]: _description_
    """
    copia = inicializar_matriz(len(matriz),len(matriz[0]),0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            copia[i][j] = matriz[i][j] 
    return copia 


def calcular_promedio(valor_uno:int,valor_dos:int,valor_tres:int)->float:
    """funcion para calcular el promedio en el ejercicio para el parcial

    Args:
        valor_uno (int): _description_
        valor_dos (int): _description_
        valor_tres (int): _description_

    Returns:
        float: _description_
    """
    suma = valor_uno + valor_dos + valor_tres
    nota_promedio = suma / 3 
    return round(nota_promedio,2) 


def recortar_matriz_por_filas(matriz:list[list], numero_filas:int)->list[list]:
    """crea una nueva matriz con la cantidad de filas que indiquemos por parametro

    Args:
        matriz (list[list]): _description_
        numero_filas (int): _description_

    Returns:
        list[list]: _description_
    """
    nueva_matriz = [None] * numero_filas

    contador = 0

    for fila in matriz:
        if contador < numero_filas:  
            nueva_matriz[contador] = fila  
            contador += 1

    return nueva_matriz   

def promediar_columna(matriz:list[list],columna:int)-> float:
    """me permite sacar el promedio de una columna de enteros

    Args:
        matriz (list[list]): _description_
        columna (int): _description_

    Returns:
        float: _description_
    """
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][columna]
    if len(matriz) > 0:    
        promedio = suma / len(matriz)   
        return round(promedio,2)   

def encontrar_mayores_promedios(matriz: list[list], columna: int, valor: int) -> list[list]:
    """

    Args:
        matriz (list[list]): _description_
        columna (int): _description_
        valor (int): _description_

    Returns:
        list[list]: _description_
    """
    
    nueva_matriz = [None] * len(matriz)
    indice = 0

    
    for fila in matriz:
        if fila[columna] > valor:
            nueva_matriz[indice] = fila  
            indice += 1

   
    matriz_final = [None] * indice
    for i in range(indice):
        matriz_final[i] = nueva_matriz[i]

    return matriz_final   
def encontrar_peor_jurado(jurado_uno:float,jurado_dos:float,jurado_tres:float)->str:
    menor_promedio = jurado_uno
    if jurado_dos < menor_promedio:
        menor_promedio = jurado_dos 
    if jurado_tres < menor_promedio:
        menor_promedio = jurado_tres 
     
    peores_jurados = [None] * 3  
    indice = 0

    
    if jurado_uno == menor_promedio:
        peores_jurados[indice] = f'Jurado 1 con una nota promedio de {jurado_uno}'
        indice += 1
    if jurado_dos == menor_promedio:
        peores_jurados[indice] = f'Jurado 2 con una nota promedio de {jurado_dos}'
        indice += 1
    if jurado_tres == menor_promedio:
        peores_jurados[indice] = f'Jurado 3 con una nota promedio de {jurado_tres}'
        indice += 1

 
    if indice == 1:
        return f'El jurado más malo es {peores_jurados[0]}'
    else:
        mensaje = 'Los jurados más malos son: '
        for i in range(indice):
            if i > 0:
                mensaje += ', '
            mensaje += peores_jurados[i]
        return mensaje 




# def filtrar_por_busqueda(matriz: list[list], columna: int, valor: int) -> list[list]:
    
#     nueva_matriz = [None] * len(matriz)
#     index = 0

   
#     for fila in matriz:
#         if fila[columna] == valor:
#             nueva_matriz[index] = fila  

    
#     matriz_final = [None] * index
#     for i in range(index):
#         matriz_final[i] = nueva_matriz[i]

#     return matriz_final     

def encontrar_ganador(matriz:list[list],nota:float,columna:int)->list | list[list]:   
    posibles_ganadores = [None] * len(matriz)  
    index = 0  

    for fila in matriz:
        if fila[columna] == nota:
            posibles_ganadores[index] = fila  
            index += 1
        else:
            break  

    posibles_ganadores_final = [None] * index
    for i in range(index):
        posibles_ganadores_final[i] = posibles_ganadores[i]

    return posibles_ganadores_final  

def desempatar_participantes(matriz_empates):
    """
    Desempata una matriz de participantes donde los jurados votan por un participante.

    Parámetros:
        matriz_empates (list): Matriz donde cada fila representa a un participante empatado.
                               Formato: [['participante', nota1, nota2, nota3, promedio], ...]

    Retorna:
        str: El participante ganador del desempate.
    """
    
    participantes = [fila[0] for fila in matriz_empates]
    votos = [0] * len(participantes)
    jurados = ["Jurado_uno", "Jurado_dos", "Jurado_tres"]

    

   

    for jurado in jurados:
        print(f"\n{jurado}, elija un participante (ingrese el número):")
        for i in range(len(participantes)):
            print(f"{i + 1}. {participantes[i]}")
        
        voto = pedir_numero(
            mensaje="Ingrese el número del participante: ",
            mensaje_error="Número inválido. Intente de nuevo: ",
            minimo=1,
            maximo=len(participantes)
        )
        votos[voto - 1] += 1

   
    contador = 0
    ganador = participantes[0]
    max_votos = votos[0]
    for k in range(1, len(participantes)):
        if votos[k] > max_votos:
            max_votos = votos[k]
            ganador = participantes[k]
    for j in range(len(participantes)):
        if votos[j] == max_votos:
            contador += 1
        if contador > 1:
            ganador = matriz_empates[random.randint(0,len(matriz_empates)-1)][0]          
            break
    
    return ganador

def buscar_por_notas_sumadas(matriz:list[list])->str:
    """guarda las sumas de cada nota por participante en una lista y verifica si alguna coincide con el entero que ingresamos

    Args:
        matriz (list[list]): _description_

    Returns:
        str: _description_
    """
    suma_notas = []

    
    for fila in matriz:
        suma = 0
        for i in range(1, 4):  
            suma += fila[i]
        suma_notas += [suma] 
    busqueda = pedir_numero('Ingrese numero del 3 al 300: ', 'ERROR solo numero entre 3 y 300',3,300)

    encontrado = False
    for i in range(len(suma_notas)):
        if suma_notas[i] == busqueda:
            print(f"El numero {busqueda} coincide con {matriz[i][0]}.")
            encontrado = True

    if not encontrado:
        print(f"No se encontró ningún participante con suma de notas igual a {busqueda}.")     