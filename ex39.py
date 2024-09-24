a = int(input('Qual é o ano do seu nascimento:'))
if a == 2006:
    print('o senhor deve se alistar, acesse eb.com.br e se aliste online.')
elif a > 2006:
    print(f'ainda não é a hora de vc se alistar, espere daqui a {(a-2006)} anos ')
elif a < 2006:
    print(f'já passou do prazo para o senhor se alistar, vá até junta militar mais proxima regulamentar seu caso. estáis atrazado {(2006-a)} anos')
