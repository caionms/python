print('Iremos contar quantas palavras possuem uma das letras de "python" e tenham mais de 4 caracteres no texto.')
texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
aux = ""
aux1 = []
#if texto.isalnum():
#    texto.casefold()
#    lista = texto.split()
#    print(lista)
#else:
for character in texto:
    if character.isalnum() or character == " ":
        aux += character
aux = aux.casefold()
listaux = aux.split()
for string in listaux:
    naux = 0
    if len(string) > 4:
        for letter in string:
            if naux == 1:
                break
            elif letter in "python":
                aux1.append(string)
                naux = 1
count = 0
for palavra in aux1:
    count += 1
print('Foram encontradas', count, 'palavras no texto.')
