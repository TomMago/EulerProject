from itertools import chain


def faktorisiere(n):
    l = []  # Lösungsmenge
    # Auf Teilbarkeit durch 2, n, und alle ungeraden Zahlen von 3..n/2 testen
    for i in chain([2], range(3, n//2 + 1, 2)):
        # Ein Teiler kann mehrfach vorkommen (z.B. 4 = 2 * 2), deswegen:
        while n % i == 0:
            l.append(i)
            n = n // i  # "//" ist ganzzahlige Division und entspricht int(n/i)
        if i > n:  # Alle Teiler gefunden? Dann Abbruch.
            break
    return l

print(faktorisiere(600851475143))
