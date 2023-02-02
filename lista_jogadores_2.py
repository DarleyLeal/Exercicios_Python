jogador = dict()
time = list()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = input(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, total):
            partidas.append(int(input(f'     Quantos gols na partida {c + 1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        opc = input('Quer continuar? S/N').upper().strip()[0]
        if opc in 'SN':
            break
        print('Erro, digite apenas S ou N!')
    if opc == 'N':
        break
print('-' * 40)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? 999 para sair '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, não existe nenhum jogador com código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR: --\n{time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
