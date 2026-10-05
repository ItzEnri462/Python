def conta_parole(frase):
    conteggio = {}
    for i in frase.lower().split():
        conteggio[i] = conteggio.get(i, 0) + 1
    return conteggio

frase = "il gatto dorme il cane dorme il topo corre"
piu_frequente = max(conta_parole(frase), key=conta_parole(frase).get)
print(piu_frequente, conta_parole(frase)[piu_frequente])