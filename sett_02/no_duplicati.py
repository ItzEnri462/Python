def senza_duplicati(nomi):
    visti = set()
    risultati = []
    for i in nomi:
        if i not in visti:
            visti.add(i)
            risultati.append(i)
    return risultati

lista_nomi = ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"]
print(senza_duplicati(lista_nomi))