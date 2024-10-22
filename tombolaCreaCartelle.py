filePath = input("Inserisci il percorso del file tombolaCartelle.txt (se non esiste, crea un file .txt VUOTO e inserisci il suo percorso): ")
file = open(filePath, "a")

anotherCartella = 1
while anotherCartella:
    scelta = 0
    while not scelta:
        nome = input("Inserisci il nome del giocatore: ")
        scelta = input(f"""Il nome scelto è {nome}. Confermare?
          0 - No
          1 - Sì\n""")
        while scelta not in ("0", "1"):
            scelta = input("Inserisci un numero tra 0 e 1!\n")
        scelta = int(scelta)
    file.write(f"{nome}\n")
    numbersArray = []
    for i in range(1, 16):
        while True:
            try:
                num = int(input(f"Inserisci il {i}° numero: "))
            except ValueError:
                print("Inserisci un numero intero!")
            else:
                if num <= 0 or num > 90:
                    print("Inserisci un numero compreso tra 1 e 90!")
                elif num in numbersArray:
                    print("Questo numero è già stato inserito!")
                else:
                    break
        numbersArray.append(num)
        if (i % 5 == 0):
            file.write(f"{num}\n")
        else:
            file.write(f"{num} ")
    file.write("\n")
    anotherCartella = input(f"""Aggiungere un'altra cartella?
          0 - No
          1 - Sì\n""")
    while anotherCartella not in ("0", "1"):
        anotherCartella = input("Inserisci un numero tra 0 e 1!\n")
    anotherCartella = int(anotherCartella)


    