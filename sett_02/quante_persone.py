def conta_unici(nomi):
    return len(set(nomi))

l = ["Luca", "Sara", "Marco", "Luca", "Giulia", "Sara", "Luca"]
print(conta_unici(l))