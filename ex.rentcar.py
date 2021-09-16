#exercício 2 - aula prática
km = float(input("Quantos km foram percorridos?"))
dias = float(input("Por quantos dias?"))
paluguel = (60 * dias) + (0.15 * km)
print('O preço à pagar é: R${}'.format(paluguel))