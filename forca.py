from time import sleep
palavra = list(input('Digite uma palavra: '))
dica = input('Digite uma dica: ')
nao_tem = []
nao_tem1 = ' '
pl = ''.join(palavra)
np1 = list(len(palavra)*'*')
np2 = ''.join(np1)
print(f'\nPalavra: {np2}\n')
chan = len(palavra)
if chan < 5:
    chan = 5
d = 0
for t in range(5, 0 , -1):
    print(t)
    print('')
    sleep(1)
    t -=1
print('Valendo!')
print('')
if len(palavra) < 5:
    print(f'Você tem {chan} chances. Boa sorte!\n')
    print(f'Palavra: {np2}\n')
else:
    print(f'Você tem {chan} chances. Boa sorte!\n')
    print(f'Palavra: {np2}\n')
while True:
    print(f'A dica é: {dica.upper()}')
    print(f'Letras que não estão na palavra: {nao_tem1}')
    letra = input('Digite uma letra: ')
    for i in range(len(palavra)):
        if letra == palavra[i]:
            del(np1[i])
            np1.insert(i,palavra[i])
            np2 = ''.join(np1)
    if letra not in palavra:
        d += 1
        nao_tem.append(letra.upper())
        nao_tem1 = str(nao_tem)
        if (chan-d) == 1:
            print(f'\nVocê ainda tem {int(chan - d)} chance. Boa sorte!\n')
        elif (chan-d) > 1:
            print(f'\nVocê ainda tem {int(chan - d)} chances. Boa sorte!\n')
        else:
            print(f'\nVocê perdeu!\nA palavra era {pl.upper()}')
            break
    elif np1 == palavra:
        print(f'\nMeus parabéns, você acertou a palavra {pl.upper()}')
        break
    else:
        if len(palavra)>1:
            print(f'\nVocê ainda tem {chan-d} chances')
    print(f'{np2}\n')