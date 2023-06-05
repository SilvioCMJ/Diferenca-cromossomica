import random
# letras
letras = 'AV'
letras1 = 'A'
letras2 = 'V'
# contadores
r = 0
A = 0
V = 0
# iniciando rodadas
while r < 100:
    # gerando populacao
    v = random.choice(letras)
    v1 = random.choice(letras)
    # ajustando limite de gene
    while A == 100:
        v = random.choice(letras2)
        v1 = v
    if v1 or v == 'A':
        A = A + 1
    while V == 100:
        v = random.choice(letras1)
        v1 = v
    if v1 or v == 'V':
        V = V + 1
    r = r + 1
    # exibindo resultado
    print(f'Rodada {r}: {v}|{v1}')

