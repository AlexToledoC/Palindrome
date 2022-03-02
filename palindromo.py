def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True


def run():
    print('Bienvenid@ al programa para saber si lo que escribes es un palíndromo')
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

if __name__ == '__main__':
    run()