from time import sleep
print('-'*30)
print('CALCULE SEUS MACROS')
print('-'*30)
p = float(input('Qual é o seu peso atual?'))
print('Calculando seus macros...')
sleep(2)
print('''Qual é seu objetivo?
[ 1 ] Manter seu peso
[ 2 ] Emagrecer
[ 3 ] Ganhar massa muscular''')

opcao = int(input('Sua opção:'))
print('Terminando a analise...')
sleep(2)

if opcao == 1:
    proteina = p * 2
    carboidratos = p * 4
    gordura = p * 1

elif opcao == 2:
    proteina = p * 2.5
    carboidratos = p * 2.5
    gordura = p * 0.9

elif opcao == 3:
    proteina = p * 2.8
    carboidratos = p * 4
    gordura = p * 1.2
else:
    print('Opção invalida. Tente novamente.')

calorias1 = proteina * 4
calorias2 = carboidratos * 4
calorias3 = gordura * 9
calorias_totais = calorias1 + calorias2 + calorias3
print(f'''Macros a serem batidos:
      Proteínas = {proteina:.1f}g / {calorias1:.1f} cal
      Carboidratos = {carboidratos:.1f}g / {calorias2:.1f} cal
      Gordura = {gordura:.1f}g /  {calorias3:.1f} acl
      Calorias totais = {calorias_totais:.1f} cal''')

print('-'*30)
print('Aqui vai uma sugestão de acordo com seu objetivo.')
print('-'*30)

if opcao == 1:
    print('''MANTER O PESO:
    Mantenha uma dieta equilibrada com uma variedade de alimentos nutritivos, incluindo proteínas magras, carboidratos complexos, gorduras saudáveis, frutas e vegetais.
    Controle as porções para evitar excessos e mantenha um equilíbrio entre a quantidade de calorias consumidas e as calorias queimadas através da atividade física.
    Mantenha-se hidratado bebendo água suficiente ao longo do dia.''')
elif opcao == 2:
    print('''EMAGRECER:
    Reduza a ingestão de calorias, concentrando-se em alimentos ricos em nutrientes e baixos em calorias, como vegetais não amiláceos, frutas frescas, legumes, proteínas magras e grãos integrais.
    Limite o consumo de alimentos processados, açúcares adicionados, gorduras saturadas e bebidas açucaradas.
    Pratique atividade física regularmente para queimar calorias extras e promover a perda de peso.''')
elif opcao == 3:
    print('''GANHAR MASSA MUSCULAR:
    Consuma uma quantidade adequada de proteínas para apoiar o crescimento muscular, incluindo fontes de proteína magra como peito de frango, peixe, carne magra, ovos, laticínios com baixo teor de gordura, leguminosas e tofu.
    Inclua carboidratos complexos em suas refeições para fornecer energia para os treinos e ajudar na recuperação muscular, como arroz integral, batata-doce, aveia e quinoa.
    Não negligencie as gorduras saudáveis, pois elas desempenham um papel importante na saúde geral e na função hormonal. Escolha fontes de gorduras saudáveis, como abacate, nozes, sementes e azeite de oliva.''')








