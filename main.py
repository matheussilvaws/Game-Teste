from random import randint

seu_nome = input('Ola, quall seu nome: ')
print(f'okok!{seu_nome}, eu estou escollhendo um numero de 1 a 10,, voce consegue adivinhar?')
numero_adivinhado = randint(1,10)
numero_tentativas = 3

for tentativa in range(1, numero_tentativas + 1):
  numero_escolhido = int(input('Escollha um numero: '))
  if numero_escolhido == numero_adivinhado:
    print(f'Parabens, voce acertou em {tentativa} tentativas!!')
    break
  elif numero_escolhido > numero_adivinhado:
     print('Escolha um numero menor')
  else:
     print('Escolha um numero maior')
  
print(f'O numero era {numero_adivinhado}. Obrigado por CODAR!!!')