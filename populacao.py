import random
# As letras A e V correspondem respectivamente ao fenotipo Amarelo e Verde
# letras
letras = 'AV'
# contadores
r = 0
A = 0
V = 0
het = 0
homo = 0
# iniciando rodadas
while r < 100:
    # gerando populacao
    v = random.choice(letras)
    v1 = random.choice(letras)
    # ajustando limite de gene
    if A >= 100:
        v = "V"
        v1 = v
    if V >= 100:
        v = "A"
        v1 = v
    if v == "A":
        A = A + 1
    if v == 'V':
        V = V + 1
    if v1 == "A":
        A = A + 1
    if v1 == "V":
        V = V + 1
    if v1 == v:
        homo = homo + 1
    if v1 != v:
        het = het + 1
    r = r + 1
    # exibindo resultado
    print(f'Rodada {r}: {v}|{v1}')
    if r == 100:
        print(f'Frequencia da cor Verde:{V}')
        print(f'Frequencia da cor Amarela:{A}')
        print(f'Frequencia de Herozigoto:{het}')
        print(f'Frequencia de Homozigoto:{homo}')
