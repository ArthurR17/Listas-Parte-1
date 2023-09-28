valores = []
soma = 0
i = 0
while i < 5:
    valores.append(int(input("Digite um valor: ")))
    soma += valores[i]
    i += 1

soma = soma - (soma * 0.05)
print(soma)

