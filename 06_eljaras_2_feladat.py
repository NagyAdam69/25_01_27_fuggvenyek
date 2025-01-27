"""
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
"""


# def eljaras(szam): 
#     if szam < 0:
#         print("Negative!")
#     elif szam > 0:
#         print("Positive!")
#     else:
#         print("Zero!")
        
# eljaras(8)
# eljaras(-2)
# eljaras(0)

"""
Addig lehessen számokat megadni, amíg a felhasználó nem ad meg üre szringet, és a program eldönti, hogy a számok pozitív, negatív vagy nulla-e.
"""

def eljaras2(szam):
    if szam < 0:
        print("Negative!")
    elif szam > 0:
        print("Positive!")
    else:
        print("Zero!")
    return szam

while True:
    szam_input = input("Szám: ")
    if szam_input == "":
        print("Vége")
        break
    eljaras2(int(szam_input))