#exercício 1 - apostila c/ aula prática
pprod = float(input("Qual é o preço do produto?"))
pdesc = float(input("Percentual de desconto?"))
precodesc = pprod * (pdesc / 100)
desc = pprod - pdesc
print('Total de desconto é: R${} e o produto sai por: R${}'.format(pdesc, desc))




