user = pasw = 'start'
while(user in pasw):
    user = input('Digite o usuário: ')
    pasw = input('Digite a senha: ')
    if(user in pasw):
        print('Senha presente no usuário, insira uma senha diferente!')
    else:
        print('Usuário e senha válidos!')
