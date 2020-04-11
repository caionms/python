print('Iremos criar uma lista com as palavras de um texto.')
aux = ""
aux1 = []
texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
if texto.isalnum():
    lista = texto.split()
    print(lista)
else:
    for character in texto:
        if character.isalnum() or character == " ":
            aux += character
aux = aux.casefold()
listaux = aux.split()
for char in listaux:
    if char[0] in "python":
        aux1.append(char)
    if char[len(char)-1] in "python":
        aux1.append(char)
print(aux1)
