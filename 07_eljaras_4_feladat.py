"""
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
"""
def legrovidebb():
    print(f"A megadott szavak közül a {legrovidebb_szo}.")

szavak = []s
for i in range(3):
    szo = input("Adj meg egy szót: ")
    szavak.append(szo)

legrovidebb_szo = min(szavak)
legrovidebb()