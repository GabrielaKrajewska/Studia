import numpy as np
import matplotlib.pyplot as plt
'''
    # Cel:
    # Napisać w Pythonie funkcję do aproksymacji średniokwadratowej (Metoda Najmniejszych Kwadratów)
    
    # Opis:
    # x, y to wartości zadanych punktów,
    # n to stopień szukanego wielomianu,
    # Funkcja ma zwracać współczynniki wielomianu aproksymacyjnego: a = [a0, a1, · · · , an].
    # Algorytm ma narysowa¢ wykres wyznaczonego wielomianu wraz z zaznaczeniem punktów, do których wielomian został
    # dopasowany
'''
def Krajewska_Gabriela_MNK(x, y, n):
    
    # 1) Tworzymy macierz A: każda kolumna to x^i dla i = 0, ..., n
    punkty = len(x)  # Liczba punktów danych
    A = np.zeros((punkty, n + 1))#tworzę macierz o wymiarach: liczba punktów x(n+1) dla wielomianu

    #każda kolumna macierzy A reprezentuje potęgę wartości x.
    for i in range(n + 1):  # Iteracja po stopniach wielomianu
        for j in range(punkty):  # Iteracja po punktach danych
            A[j, i] = x[j]**i  # Obliczanie potęgi x i przypisanie do macierzy


    # 2) Obliczamy macierz równań normalnych: AT_A i AT_y
    AT_A = np.zeros((n + 1, n + 1)) #tworzę macierz do późniejszego rozwiązywania równań
    AT_y = np.zeros(n + 1)

    for i in range(n + 1):
        for j in range(n + 1):
            AT_A[i, j] = sum(A[:, i] * A[:, j]) 
        AT_y[i] = sum(A[:, i] * y)

    # 3)
    # a) Rozkład Cholesky'ego macierzy AT_A
    L = np.zeros_like(AT_A) #macierz L służy tutaj do przechowywania wyników rozkładu Cholesky'ego

    for i in range(n + 1):
        for j in range(i + 1):
            if i == j:
                L[i, j] = (AT_A[i, i] - sum(L[i, k] ** 2 for k in range(j))) ** 0.5
            else:
                L[i, j] = (AT_A[i, j] - sum(L[i, k] * L[j, k] for k in range(j))) / L[j, j]

    # b) Rozwiązywanie układów równań L * c = AT_y
    c = np.zeros(n + 1)
    for i in range(n + 1):
        c[i] = (AT_y[i] - sum(L[i, k] * c[k] for k in range(i))) / L[i, i]

    # c) Rozwiązywanie układów równań L.T * a = c
    a = np.zeros(n + 1)
    for i in range(n, -1, -1):
        a[i] = (c[i] - sum(L[k, i] * a[k] for k in range(i + 1, n + 1))) / L[i, i]

    # 5) Rysowujemy wykres aproksymacyjny wielomianu
    p_x = np.linspace(min(x), max(x), 500) #generuję punkty do wysowania wykresu
    p_y = sum(a[i] * (p_x ** i) for i in range(n + 1))

    plt.plot(p_x, p_y, label='wielomian', color='magenta')
    plt.scatter(x, y, color='darkblue', label='dane')
    plt.xlabel('x')#tworzę legendę i podpisy pod wykresem
    plt.ylabel('y')
    plt.title('Metoda najmniejszych kwadratów')
    plt.legend()
    plt.grid()
    plt.show()

    return a

# Przykładowe wywołanie funkcji

x = np.array([1, 18.1, 21, 9, 44.4, 66, 8, 99])

y = np.array([12, 19, 1, 15.3, 99.1, 99, 0, 8])

n =2  

wspolczynniki = Krajewska_Gabriela_MNK(x, y, n)
print("Współczynniki wielomianu:", wspolczynniki)



