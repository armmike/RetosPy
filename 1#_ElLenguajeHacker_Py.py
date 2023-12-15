'''
Reto #1: EL “LENGUAJE HACKER” 
Dificultad: Fácil | Publicación: 02/01/23 | Corrección: 09/01/23 
Enunciado 
/*
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
* se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
* con el alfabeto y los números en "leet".
* (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/

'''
def hack_str():
    text = input('Introduce un texto:\n')
    abc_hacker = {' ' : ' ','a' : '4', 'b' : '13', 'c' : '[','d' : ')','e' : '3'
              ,'f' : '|=','g' : '&','h' : '#','i' : '1', 'j' : ',_|',
               'k' : '>|','l' : '1','m' : '/\/\\','n' : '/\\/','o' : '0','p' : '|*',
                 'q' : '(_.)', 'r' : '12', 's' : '5','t' : '7','u' : '(_)','v' : '\\/','w' : '\\/\\/',
                 'x' : '><','y' : 'j', 'z' : '2','A' : '4', 'B' : '13', 'C' : '[','D' : ')','E' : '3'
              ,'F' : '|=','G' : '&','H' : '#','I' : '1', 'J' : ',_|',
               'K' : '>|','L' : '1','M' : '/\/\\', 'N' : '/\\/','O' : '0','P' : '|*',
                 'Q' : '(_.)', 'R' : '12', 'S' : '5','T' : '7','U' : '(_)','V' : '\\/','W' : '\\/\\/',
                 'X' : '><','Y' : 'j', 'Z' : '2'}

    text_hacker = ''

    for letra in text:
        if ( abc_hacker.__contains__(letra)):
            text_hacker += abc_hacker[letra]
            
    print(text)
    print(text_hacker)
hack_str()


