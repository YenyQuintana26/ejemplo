import random

intentos=1
max_intentos=5
num_random= random.randint(0,10)

print("Bienvenido adivina el numero que estoy pensando")

while True:

    numero=int(input("Que numero estoy pensando? ingrese el numero: "))

    if num_random==numero:
        break

    if intentos==max_intentos:
        print("juego terminado:(")
        exit()
    
    intentos+=1

print("ganaste")
