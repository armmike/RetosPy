#@armmike
###########################################
'''/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''
###########################################
numero = int(input('Dime un número: '))
###########################################
def fibonacci(num):
    lista = [1,1]
    n = 0
    for j in lista:
        end = False
        
        if (j < 3):
            n += 1
            fibonacci = j + lista[n]
            lista.append(fibonacci)
            print(lista)
        if (j >= 3):
            n += 1
            fibonacci_an2 = lista[n]
            fibonacci = fibonacci + j
            lista.append(fibonacci)
            print(lista)
        if (fibonacci == num):
           end = True
           return end 
###########################################
fibonacci(numero)
if (numero % 2 != 0):
    print('Impar')
else:
    print('Par')
#an = an-1 + an-2 si n ≥ 3 y a1 = a2 = 1.
if (fibonacci):
    print('Fibonacci')
########################################### 


###########################################
###########################################
###########################################

###########################################
#@armmike
    
    
