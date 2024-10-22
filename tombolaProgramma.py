import random

file = input("Inserisci il percorso del file tombolaCartelle.txt: ")
cartelle = open(file, "r")
testo = cartelle.readlines()

arrayCartelle = []
for i in range(0, len(testo)):
    step = i % 5
    if (step == 0):
        cartella = ["", [], [0,0,0], [False, False, False, False, False]]
        for j in testo[i]:
            if j != "\n":
                cartella[0] += j
    elif (step == 1 or step == 2 or step == 3):
        potentialNum = 0
        for j in range(0, len(testo[i])):
            if testo[i][j] == " " or j == len(testo[i])-1:
                if potentialNum > 90:
                    print(f"La cartella di {cartella[0]} contiene un numero maggiore di 90! Sistema il file e fai ripartire il programma.")
                    exit()
                else:
                    if potentialNum in cartella[1]:
                        print(f"Il numero {potentialNum} è presente più di una volta nella cartella di {cartella[0]}! Sistema il file e fai ripartire il programma.")
                        exit()
                    cartella[1].append(potentialNum)
                    potentialNum = 0
            else:
                try:
                    potentialNum = potentialNum*10 + int(testo[i][j])
                except ValueError:
                    print(f"La cartella di {cartella[0]} contiene un carattere non numerico! Sistema il file e fai ripartire il programma.")
                    exit()
    else:
        if len(cartella[1]) != 15:
            print(f"La cartella di {cartella[0]} contiene più di 15 numeri! Sistema il file e fai ripartire il programma.")
        else:
            arrayCartelle.append(cartella)

for i in range(0, len(arrayCartelle)):
    newCartella = [[], [], []]
    for j in range(0, 5):
        newCartella[0].append(arrayCartelle[i][1][j])
    for j in range(5, 10):
        newCartella[1].append(arrayCartelle[i][1][j])
    for j in range(10, 15):
        newCartella[2].append(arrayCartelle[i][1][j])
    arrayCartelle[i][1] = newCartella

    
print("""Vuoi inserire manualmente i numeri oppure vuoi che li estragga casualmente il programma?
      0 - Manualmente
      1 - Programma""")
choice = input()
while choice not in ("0", "1"):
    print("Inserisci un numero da 0 a 1!")
    choice = input()

numbers = []
for i in range(1, 91):
    numbers.append(i)

ambi = 0
terni = 0
quaterne = 0
cinquine = 0
tombole = 0

while True:
    if choice == "0":
        print("\nInserisci un numero: ")
        while True:
            try:
                n = int(input())
            except ValueError:
                print("Inserisci un numero intero!")
            else:
                if n <= 0 or n > 90:
                    print("Inserisci un numero compreso tra 1 e 90!")
                elif n not in numbers:
                    print("Questo numero è già stato inserito!")
                else:
                    break
    else:
        n = random.choice(numbers)
        print(f"\nÈ uscito il numero {n}.")
    numbers.remove(n)

    for c in arrayCartelle:
        for j in range(0, 3):
            if n in c[1][j]:
                c[2][j] += 1
    for c in arrayCartelle:
        for j in c[2]:
            if j == 2 and c[3][0] == False:
                ambi += 1
                print(f"\n{c[0]} ha fatto l'ambo n.{ambi}!")
                c[3][0] = True
            elif j == 3 and c[3][1] == False:
                terni += 1
                print(f"\n{c[0]} ha fatto il terno n.{terni}!")
                c[3][1] = True
            elif j == 4 and c[3][2] == False:
                quaterne += 1
                print(f"\n{c[0]} ha fatto la quaterna n.{quaterne}!")
                c[3][2] = True
            elif j == 5 and c[3][3] == False:
                cinquine += 1
                print(f"\n{c[0]} ha fatto la cinquina n.{cinquine}!")
                c[3][3] = True
        if c[2][0] + c[2][1] + c[2][2] == 15 and c[3][4] == False:
            print(f"\n{c[0]} ha fatto ", end="")
            if tombole == 0:
                print("tombola!")
            else:
                print("tombolino!")
                print("\nGrazie per aver giocato! ~MC")
                exit()
            c[3][4] = True
            tombole += 1
    if choice == "1":
        input()