lista = [1, "f", "data", "g", 78, 32, "OMG", 100, "2B", 3, 3, "Hi Barbie!", "Hi Ken!"]

print(f"A lista: {lista} tem {len(lista)} elementos.")

lista.append("Oi")
print(lista)

lista.insert(0, "Novo elemento")
print(lista)

lista.pop(4)
print(lista)

lista.count(3)
print(f"O número 3 aparece {lista.count(3)} vezes na lista.")


print(f"O elemento 'Hi Barbie!' está na posição {lista.index('Hi Barbie!')} da lista.")

lista.reverse()
print(lista)

lista.copy()
print(f"Lista copiada: {lista.copy()}")

lista2 = ["Finish", "Him", "Her", 365]
novaLista = lista + lista2
print(novaLista)

print(f"A nova lista {novaLista} tem {len(novaLista)} elementos")
