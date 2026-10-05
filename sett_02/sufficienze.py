def sufficienze(voti):
    return [i for i in voti if i >= 6]

voti = [4, 7, 5, 8, 6, 3]
print(voti)
print(sufficienze(voti))
