import time

Czas = time.localtime()

ObecnyCzas = time.strftime("%H:%M:%S", Czas)
print("Obecny czas: ", ObecnyCzas)
