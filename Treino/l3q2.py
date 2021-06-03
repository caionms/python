print("Iremos fazer um programa para conferir se usuário e senha não são iguais.")
user, passw = str(input('Digite usuário e senha: ')).split()
while(user in passw):
    user, passw = str(input('Usuário presente na senha! Digite novos usuário e senha: ')).split()
print(f'Usuário é {user} e senha é {passw}.')
    
