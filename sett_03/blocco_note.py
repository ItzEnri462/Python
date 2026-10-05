def salva_appunto(testo):
    with open("appunti.txt", "a", encoding="utf-8") as f:
        f.write(testo + "\n")

testo = "Ciao"
salva_appunto(testo)
testo = "Questa è una prova"
salva_appunto(testo)
testo = "Addio"
salva_appunto(testo)
with open("appunti.txt", "r", encoding="utf-8") as f:
    for numero, riga in enumerate(f, start=1):
        print(numero, riga.strip())