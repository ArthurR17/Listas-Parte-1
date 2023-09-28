
doces = []
i = 0

while i < 10:
    doces.append(input(f"Digite o nome do {i+1}° doce: "))
    doces.sort()
    if doces[i].isalpha() == False:
        print("Digite apenas letras.")
        break
    i += 1

print(doces)

