menu = ["Padaria", "Açougue", "Rotisseria", "Bebidas"]

while True:
    escolhido = int(input("Digite uma Opção do Menu: (1 a 4 ou 0 para sair do menu): "))
    if escolhido == 0:
        break
    print("Você escolheu a opção: %s" % (menu[escolhido - 1]))