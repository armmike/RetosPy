###########################################
'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
'''
###########################################
import random

puntuaciones = ['Love', 15, 30, 40, 'Deuce', 'Ventaja']
players  = ['P1', 'P2']

###########################################
def generar_secuencia(n):
    secuencia = []
    for i in range(1,n):
        secuencia.append(random.choice(players))
    return secuencia
###########################################
def partido():
    sec = generar_secuencia(9)
    print(sec)
    print('EMPIEZA EL PARTIDOOOO!!!!!')
    mP1 = puntuaciones[0]
    mP2 = puntuaciones[0]
    cont1 = 0
    cont2 = 0
    
    ###########################################
    for p in sec:
        ###########################################
        #Marcador se actualiza cada vez que se recorre la lista sec
        #Partido Puntos 
        #Se suman puntos si marca P1 o P2 y su marcador no es Deuce
        if (p == 'P1') and (mP1 != puntuaciones[3]):
            cont1 += 1
            print(cont1)
            mP1 = puntuaciones[cont1]
            marcador = str(mP1) + ' - ' + str(mP2)
            print('DIABLOOOOOOS, MARCÓ ' + players[0]+ ': '+ marcador)
            print(mP1)
            

        elif (p == 'P2') and (mP2 != puntuaciones[3]):
            cont2 += 1 
            print(cont2)
            mP2 = puntuaciones[cont2]
            marcador = str(mP1) + ' - ' + str(mP2)
            print('DIABLOOOOOOS, MARCÓ ' + players[1] + ': '+ marcador)
            print(mP2)
        ###########################################
        #Empate
        #Si marca y su marcador es empate le cambia el marcador a Deuce y se imprime el elemento
            # 3 de la lista, es decir : Deuce
        if (p == 'P1') and (mP1 == puntuaciones[3]):
            cont1 += 1
            print(cont1)
            mP1 = puntuaciones[cont1]
            print('DIABLOOOOOOS, MARCÓ ' + players[0] + ', Empate señores: ' + mP1)

        if (p == 'P2') and (mP2 == puntuaciones[3]):
            cont2 += 1 
            print(cont2)
            mP2 = puntuaciones[cont2]
            print('DIABLOOOOOOS, MARCÓ ' + players[1] + ', Empate señores: ' + mP2)
        ###########################################      
        #Ventaja de los jugadores
        #Si marca y su marcador es Ventaja se le cambia
        if (p == 'P1' and mP1 == puntuaciones[4]):
            mP1 = puntuaciones[5]
            print('DIABLOOOOOOS, MARCÓ ' + players[0] + ', ' + puntuaciones[5] +\
                   ' ' + players[0]+ '!!!!')        

        if (p == 'P2' and mP2 == puntuaciones[4]):
            mP2 = puntuaciones[5]
            print('DIABLOOOOOOS, MARCÓ ' + players[1] + ', ' + puntuaciones[5] + ' ' +\
                   players[1]+ '!!!!')
        ###########################################
        #Ganador del partido
        if (p == 'P1' and mP1 == puntuaciones[5]):
            print('MARCÓ ' + players[0] + '!!!! Ha ganado el jugador ' + players[0] + '!!!!')
            break  

        if (p == 'P2' and mP2 == puntuaciones[5]):
            print('MARCÓ ' + players[1] +'!!!! Ha ganado el jugador ' + players[1]+ '!!!!')
            break
        ###########################################        
partido()
###########################################

    
    



