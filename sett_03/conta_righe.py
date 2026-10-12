

def conta_righe(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        numero, non_vuote = 0, 0
        for numero, riga in enumerate(f, start=0):
            numero += 1;
            if riga.strip() != '':
                non_vuote += 1
    return numero, non_vuote;

for n in ["dati/parole.txt", "dati/commedia.txt"]:
    totale, non_vuote = conta_righe(n)
    print(f"{n}: totale: {totale}, non_vuote: {non_vuote}")