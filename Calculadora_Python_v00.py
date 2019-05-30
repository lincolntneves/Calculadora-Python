

print('Bom dia!')
print('Sou sua calculadora pessoal!')
print('Estou em uma etapa experimental. Sendo assim, tenha paciência!')
resp1 = input('Vamos começar? (s/n) ')
if resp1 == 's':
    n1 = int(input('Indique o 1º número '))
    n2 = int(input('Indique o 2º número '))
    resultado = n1+n2
    print('O resultado da soma é: ' + str(resultado))
else:
    print('Obrigado por participar desse experimento!')
