import math

###porównanie metod wyliczania funkcji logarytm
##
###1. wyliczanie funkcji ln(y) z rozwinięcia ln(1+x) w szereg Taylora

def logarytm1(y, eps):#x-wartość, dla której obliczamy ln(1+x), eps- tolerancja błędu względnego
    x=y-1
    test = 10000
    znak = 1 #określa znak danego wyrazu (w każdej iteracji zamienia się na przeciwny)
    potega = x #aktualna potęga x^n
    lognasz = x #suma przybliżona algorytmu
    k = 1 #liczba wykonanych iteracji (nasze k ze wzoru na szereg Taylora)
    if y <2:
        while test > eps:
            k += 1
            znak = -znak #zmieniamy na przeciwny według wzoru
            potega = potega * x
            lognasz += znak * potega / k #wykonujemy sume kolejnych elementów szeregu
            test = abs((lognasz - math.log(x + 1)) / lognasz) #porównujemy przybliżenie lognasz z dokładnym wynikiem
        return lognasz #zwraca przybliżoną wartość logarytmu
    else:
        pomoc=0
        while y > 2:
            y=y/2 
            pomoc+=1 #zliczamy ile 2 mieści się w naszym y
        lognasz1= logarytm1(y,eps) #obliczamy logarytm dla y<2 (już stworzonym algorytmem ze zmienionym y)
        return pomoc*math.log(2)+lognasz1
            

#Test dla x = 0.7
print("Logarytm ln(y):", logarytm1(1.7, 0.0000001))  
print("Wartość referencyjna:", math.log(1.7))


##2. wyliczanie funkcji ln(y) z połączenia rozwinięć ln(1+x) oraz ln(1-x) w szereg
## Taylora poprzez wyliczenie ln((1+x)/(1-x))

def logarytm2(y, eps):
    
    x = y  # W szeregu Taylora rozwijamy bezpośrednio dla y
    suma = 0  # Suma szeregu Taylora
    potega = x  # x^(2k+1), początkowo x^1
    k = 1  # Licznik w szeregu Taylora

    while abs(2 * potega / k) > eps:  # Iterujemy dopóki kolejny składnik jest większy od eps
        suma += 2 * potega / k  # Dodajemy składnik szeregu
        potega *= x * x  # Zwiększamy potęgę x^(2k+1)
        k += 2  # Zwiększamy licznik (tylko dla nieparzystych potęg)

    return suma

# Test dla y = 0.7
y = 1.7
eps = 1e-7

print("Logarytm ln(y):", logarytm2(y, eps))
print("Wartość referencyjna:", math.log(1 + y) - math.log(1 - y))

