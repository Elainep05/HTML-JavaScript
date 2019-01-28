from src.leilao.dominio import Usuario, Lance, Leilao

elaine = Usuario('Elaine')
maria = Usuario('Maria')

lance_da_elaine = Lance(elaine, 100.00)
lance_da_maria = Lance(maria, 200.00)

leilao = Leilao('Calcular')

leilao.lances.append(lance_da_elaine)
leilao.lances.append(lance_da_maria)

for lance in leilao.lances:
    print(f'A usuaria {lance.usuario.nome} deu um lance de {lance.valor}')

