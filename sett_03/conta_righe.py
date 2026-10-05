from contextlib import nullcontext


def conta_righe(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        totale = 0, non_vuote = 0
        for numero, riga in enumerate(f, start=1):
            totale += 1;
            if riga.strip() == '':
                non_vuote += 1