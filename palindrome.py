#This tells you if the entered word is a palindrome. Should work with phrases too.
##Perhaps add a library of the entered palindromes.

def finder(w):
    palabra = w.replace(' ','').lower()
    if palabra == palabra[::-1]:
        print("Encontraste un palindromo! Adios!")
        return False
    else:
        print("Ese no es un palindromo! Intenta otra vez\r\n")
        return True
    
inicio = """Bienvenido al detector de palindromos. Para salir, encuentra un palindromo :D
Escribe una palabra!
"""
loop = True
while loop == True:
    palabra = input(inicio)

    execution = finder(palabra)
    loop = execution
