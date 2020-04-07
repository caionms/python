user = pasw = 'start'
while(user == pasw):
    user = input('Digite o usuário: ')
    pasw = input('Digite a senha: ')
    if(user == pasw):
        print('Usuário e senha iguais, insira novamente!')
    else:
        print('Usuário e senha válidos!')
