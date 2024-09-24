'''with open('email.txt', 'r') as arquivo:
    email = arquivo.read()
print(email)'''

#with open('mensagem.txt', 'r', encoding='utf-8') as arquivo:
#    mensagem = arquivo.readlines()

#   for linha in mensagem:
#        if 'faturamento' in linha:
#            print(linha)

#with open('senha.txt', 'w',encoding='utf-8') as arquivo:
#     arquivo.write('lilbi')

with open('email.txt', 'a') as arquivo:
    arquivo.write('\nmusicasdeamornuncamais08@gmail.com')