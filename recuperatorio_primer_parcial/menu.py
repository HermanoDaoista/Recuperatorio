from funciones import *
import operator
from constantes import *

def ejecutar_menu():
    encabezado = ['Participante N* ','Nota Jurado 1 ','Nota Jurado 2 ','Nota Jurado 3 ','Nota Promedio ']
    bandera = 0
    while(True):
        print("COCINANDO UTN\n1.Calificar Participantes\n2.Mostrar Notas\n3.Ordenar por nota promedio\n4.Peores 3\n5.Mayores Promedio\n6.Jurado Malo\n7.Sumatoria\n8.Definir Ganador\n9.Salir")
        
        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-5\nSu opcion:",1,8)
        
        if opcion == 1:
            cocinando = inicializar_matriz(5,5,0) 
            cargar_participantes(cocinando)
            bandera = 1
         
            
        elif opcion == 2:
            if bandera == 1:
            
                imprimir_lista_encolumna(encabezado)
                mostrar_matriz(cocinando)
                
            
            
        elif opcion == 3:
            if bandera == 1:
                while(True):
                    print('Ordenar votos por Nota promedio:\n1.Ordenar por Mayor\n2.Ordenar por Menor')
                    eleccion = pedir_numero('Ingrese 1 o 2 orden ', 'Opcion invalida puede elejir entre 1 para ordenar por mayor o 2 para ordenar por menor\n.Su opcion es: ',1,2)
                    if eleccion == 1:
                        operador = operator.lt
                    
                    elif eleccion == 2:
                        operador = operator.gt
                        
                    copia_punto_tres =  copiar_matriz(cocinando)
                    ordenar_ascendente = ordenar_por_numero(copia_punto_tres,operador,I_PROMEDIO)
                    imprimir_lista_encolumna(encabezado)
                    mostrar_matriz(ordenar_ascendente)
                    
                    break
                
        elif opcion == 4:
            if bandera == 1:
            
                copia_punto_cuatro = copiar_matriz(cocinando)
                peores = ordenar_por_numero(copia_punto_cuatro,operator.gt,I_PROMEDIO)
                top_losers = recortar_matriz_por_filas(peores,3)
                imprimir_lista_encolumna(encabezado)
                mostrar_matriz(top_losers)
           

        elif opcion == 5:
            if bandera == 1:

                nota_promedio = promediar_columna(cocinando,I_PROMEDIO)
                alumnos_top_promedio = encontrar_mayores_promedios(cocinando,I_PROMEDIO,nota_promedio)
                imprimir_lista_encolumna(encabezado)
                mostrar_matriz(alumnos_top_promedio)
            
            
        elif opcion == 6:
            if bandera == 1:
                promedio_notas_jurado_uno = promediar_columna(cocinando,I_JURADO_UNO)
                promedio_notas_jurado_dos = promediar_columna(cocinando,I_JURADO_DOS)
                promedio_notas_jurado_tres = promediar_columna(cocinando,I_JURADO_TRES)
                resultado = encontrar_peor_jurado(promedio_notas_jurado_uno,promedio_notas_jurado_dos,promedio_notas_jurado_tres)
                print(resultado)
        elif opcion == 7:
            if bandera == 1:
                buscar_por_notas_sumadas(cocinando)

            
        elif opcion == 8:
            if bandera == 1:
                copia_punto_ocho = copiar_matriz(cocinando)
                ordenar_ganadores = ordenar_por_numero(copia_punto_ocho,operator.lt,I_PROMEDIO)
                mejor_nota = ordenar_ganadores[0][I_PROMEDIO]
                posibles_ganadores = encontrar_ganador(ordenar_ganadores,mejor_nota,I_PROMEDIO)
                if len(posibles_ganadores) == 1:
                    print(f"El ganador es el participante {posibles_ganadores[0][0]} con una nota promedio de {mejor_nota}")
    
                else:
                    ganador_desempate = desempatar_participantes(posibles_ganadores)
                    print(f"El ganador es el participante {ganador_desempate} con una nota promedio de {mejor_nota}")
        elif opcion == 9:
            print("Saliendo...")
            break
        limpiar_consola()
    
ejecutar_menu()           
            
             
            
            
          
            
            

