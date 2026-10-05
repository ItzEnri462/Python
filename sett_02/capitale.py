dizionario = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}

def capitale(paese):
    return dizionario.get(paese, "Non in elenco")

paese = input("Inserire un paese: ")
print(capitale(paese))