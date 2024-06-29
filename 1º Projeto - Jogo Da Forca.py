import random

def desenhar_forca(erros):
    partes_boneco = [
        '',
        '|       O',
        '|      /|\\',
        '|      / \\',
        '|      / \\',
        '|       |',
        '|      / \\',
        '|      / \\'
    ]
    
    print('---------')
    print('|        |')
    for i in range(erros):
        print(partes_boneco[i])
    for _ in range(len(partes_boneco) - erros):
        print('|')

print('\033[1;32mBEM VINDO AO JOGO DA FORCA, VOCÊ TEM 6 CHANCES DE ACERTAR UMA PALAVRA DE 4 LETRAS. BOA SORTE!!\033[m')
palavras = ['PATO', 'GATO', 'CAFE', 'CASA', 'MATA', 'CAÇA']
palavra_aleatoria = random.choice(palavras).upper()
acertos = ['_'] * len(palavra_aleatoria)
erros = 0

while erros < 7 and '_' in acertos:
    print('Palavra:', ' '.join(acertos))
    palpite = input('Digite uma letra: ').upper()
    if palpite in palavra_aleatoria:
        for i in range(len(palavra_aleatoria)):
            if palavra_aleatoria[i] == palpite:
                acertos[i] = palpite
    else:
        erros += 1
        desenhar_forca(erros)

if '_' not in acertos:
    print('Parabéns, você ganhou! A palavra era', palavra_aleatoria)
else:
    print('Você perdeu. A palavra era:', palavra_aleatoria)