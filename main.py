nome1 = input("Digite o nome do primeiro jogador:")
idade1 = int(input("Digite a idade do primeiro jogador:"))
nome2 = input("Digite o nome do segundo jogador:")
idade2 = int(input("Digite a idade do segundo jogador:"))
if idade1 > idade2:
  print("O jogador mais velho é:", nome1)
elif idade1 == idade2:
  print("Os jogadores possuem a mesma idade")
else:
  print("O jogador mais velho é:", nome2)