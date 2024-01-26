#@armmike
###########################################
'''/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
'''
###########################################
def generaContrasenia():
    global longitud
    global mayus
    global num
    global sim
    global parametersElegidos
    ###########################################
    longitud = int(input('||--Indica una longitud entre 8 y 16 caracteres||:__'))
    mayus = input('||--Indica si quieres mayúsculas con las opciones imperativas \'Con\'/\'Sin\'||:__')
    num = input('||--Indica si quieres números con las opciones imperativas \'Con\'/\'Sin\'||:__')
    sim = input('||--Indica si quieres símbolos con las opciones imperativas \'Con\'/\'Sin\'||:__')
    parametersElegidos = {
        'longitud' : 0,
        'mayus' : '',
        'num' : '',
        'sim' : '',
    }
    ########################################### 

    def peticion():
        print('=================================================')
        print('||                                          ||')
        print('||Elige los parametros para tu contraseña:__||')
        parametersElegidos['longitud'] = longitud
        parametersElegidos['mayus'] = mayus
        parametersElegidos['num'] = num
        parametersElegidos['sim'] = sim
        print('||Ha finalizado la configuración de parámetros, ||\n\
            ||espere un momento a que procesemos su contrasenia||')
        print('||                                          ||')
        print('=================================================')
    ###########################################
    print(parametersElegidos)
    #peticion
    end = True
    while end: 
        peticion()
        if (parametersElegidos['longitud'] >= 8) or (parametersElegidos['longitud'] <= 16):
            end = True
        else:
            end = False

        if (parametersElegidos['mayus'] == 'Sin') or (parametersElegidos['mayus'] == 'Con'):
            end = True
        else:
            end = False

        if (parametersElegidos['num'] == 'Sin') or (parametersElegidos['num'] == 'Con'):
            end = True
        else:
            end = False

        if (parametersElegidos['sim'] == 'Sin') or (parametersElegidos['sim'] == 'Con'):
            end = True
        else:
            end = False
        
        if end:
            break
    ###########################################
###########################################
###########################################
generaContrasenia()
#len 8..16
#con o sin may
#con o sin num
#con o sin simbolos
###########################################
#@armmike
    
    
