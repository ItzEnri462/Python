def celsius2fahrenheit(gradi):
    return gradi * 9 / 5 + 32


for i in [0, 25, 100]:
    print(f"{i}° C corrispondono a {celsius2fahrenheit(i)}")

#esercizio 2:

def e_pari(n):
    if n % 2 == 0:
        return True
    return False

for i in range(20):
    if e_pari(i + 1):
        print(i + 1, end=" ")


#esercizio 3

def media(voti):
    if len(voti) == 0:
        return None, "Non ci sono voti"
    return sum(voti) / len(voti)

voti = [9, 3, 6, 8, 1, 3, 7, 7, 7, 5]

print(f"La media dei voti è {media(voti)}")

#esercizio 4

def pullman_necessari(n):
    if n <= 0:
        return 0
    return (n + 52) // 53

print(f"con 53 persone servono {pullman_necessari(53)}, con 54 {pullman_necessari(54)} e con 106 {pullman_necessari(106)}")