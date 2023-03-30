'''Filip Adamus Zadanie silnia'''

def silnia(n):
    if n==0:
        return 1
    else:
        return n * silnia(n-1)

n=int(input("Podaj twoja silnie:"))

wynik = silnia(n)
print("Silnia liczby", n, "wynosi", wynik)
