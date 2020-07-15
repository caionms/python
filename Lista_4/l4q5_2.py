print('Iremos contar quantas palavras possuem uma das letras de "python" e tenham mais de 4 caracteres no texto.')
texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.".lower()
import string
for letter in string.punctuation:
    texto = texto.replace(letter, ' ')    
def fun(palavra):
    for letra in palavra:
        if letra in "python":
            return True
    return False        
aux = []
for word in texto.split():
    if fun(word) and len(word) > 4:
        aux.append(word)
print(aux)
print(len(aux))
