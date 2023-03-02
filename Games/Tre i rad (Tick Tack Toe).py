import os
from time import sleep

# Rensar konsolen
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#Printar ut spelet
def bräda(spel):
    print()
    print("""   0 1 2              """, spel[0], spel[1], spel[2], "\n"
          """   3 4 5              """, spel[3], spel[4], spel[5], "\n"
          """   6 7 8              """, spel[6], spel[7], spel[8])
    print()

#Ändar i brädan
#spel är lista
def XO(spel, spelare):
    while True:
        plats = input("Vart vill du placera " + str(spelare) + "\n Skriv en siffra: ")
        platsint = int(plats)
        if spel[platsint] == "-":
            spel.insert(platsint, spelare)
            spel.pop(platsint + 1)
            break
        else:
            clearConsole()
            print("Redan upptagen!")
            bräda(spel)
    
# Alla möjliga vinstalternativ
def vinst(spel, spelare):
    if spel[0] == spelare and spel[1] == spelare and spel[2] == spelare:
        print("Vinnare är " + spel[0])
        return True
    
    if spel[3] == spelare and spel[4] == spelare and spel[5] == spelare:
        print("Vinnare är " + spel[3])
        return True

    if spel[6] == spelare and spel[7] == spelare and spel[8] == spelare:
        print("Vinnare är " + spel[6])
        return True

    if spel[0] == spelare and spel[3] == spelare and spel[6] == spelare:
        print("Vinnare är " + spel[0])
        return True

    if spel[1] == spelare and spel[4] == spelare and spel[7] == spelare:
        print("Vinnare är " + spel[1])
        return True

    if spel[2] == spelare and spel[5] == spelare and spel[8] == spelare:
        print("Vinnare är " + spel[2])
        return True

    if spel[0] == spelare and spel[4] == spelare and spel[8] == spelare:
        print("Vinnare är " + spel[0])
        return True

    if spel[2] == spelare and spel[4] == spelare and spel[6] == spelare:
        print("Vinnare är " + spel[2])
        return True

    ledigaRutor = 0
    for loop in range(len(spel)):
        if spel[loop] == "-":
            ledigaRutor = 1

    if ledigaRutor == 0:
        print("Ingen vann")
        return True

            

#Skapar ett spel där en plats = en siffra
lista = ["-"]*9



# X börjar
print("X börjar först")
spelare = "X"

#Själva spelet
while True:
    bräda(lista)
    XO(lista, spelare)
    clearConsole()
    if vinst(lista, spelare) == True :
        bräda(lista)
        sleep(4)
        break

    if spelare == "X":
        spelare = "O"
    else:
        spelare = "X"