#@armmike
###########################################
'''
Reto #0: EL FAMOSO “FIZZ BUZZ” 
Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23 
Enunciado 
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''
###########################################
#define main function to print out something
print('Escribe un programa que muestre por consola (con un print) los\
 números de 1 a 100 (ambos incluidos y con un salto de línea entre\
 cada impresión)')
###########################################
def fizzbuzz():
    i = 1
    max = 101
    ###########################################
    while (i < max):
        #x3 fizz 
        #x5 buzz
        #3 y 5 fizzbuzz
        if (i % 5 == 0) and (i % 3 == 0):
            print('fizzbuzz','\n')
        elif (i % 3 == 0):
            print('fizz','\n')
        elif (i % 5 == 0):
            print('buzz','\n')
        else:
            print(i,'\n')
        ###########################################
        i = i + 1
     ###########################################
###########################################
def fizzbuzz02():
    ###########################################
    for n in range(1,101):
        if (n % 3 == 0) and (n % 5 == 0): 
            print('fizzbuzz', '\n')
        elif (n % 3 == 0): 
            print('fizz', '\n')
        elif (n % 5 == 0): 
            print('buzz', '\n')
        else:
            print(n, '\n')
    ###########################################    
#call function main
fizzbuzz()
fizzbuzz02()
###########################################
#@armmike
