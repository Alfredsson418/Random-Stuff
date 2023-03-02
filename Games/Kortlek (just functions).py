def skapaKortlek():
    
    minaSymbols=["♣", "♦", "♥", "♠"]
    minaNummer=["Ess","2","3","4","5","6","7","8","9","10","Knekt","Dam","Kung"]
    kortlek = []

    for Symbol in range(len(minaSymbols)):
        for nummer in range(len(minaNummer)):
            kortlek.append(minaNummer[nummer] + minaSymbols[Symbol])
            
        
    return kortlek

def blandaKortlek(kortlek):
        
    randomNummer1 = 0
    randomNummer2 = 0
    temp = 0
    import random
            

    for loop in range(200):
            
        randomNummer1 = random.random() * 52
        randomNummer1 = int(randomNummer1)
                    
        randomNummer2 = random.random() * 52
        randomNummer2 = int(randomNummer2)


        temp = kortlek[randomNummer1]
        kortlek[randomNummer1] = kortlek[randomNummer2]
        kortlek[randomNummer2] = temp
        
    return kortlek
    
def taEttKort(minaKort, kortlek):
    minaKort.append(kortlek[0])
    kortlek.pop(0)


def visaEttKort(minaKort):
    print("Du har ", len(minaKort))
    if(len(minaKort) != 0):
        print(minaKort)

kortlek = skapaKortlek()
minaKort = []
val = ""
while(val != 6):
    val = int(input("""
    Vad vill du göra?
    1. Skapa kortlek
    2. Blanda Kortleken
    3. Ta ett kort
    4. Visa Dina kort
    5. Visa Kortleken
    6. Sluta Programmet

"""))

    if(val == 1):
        kortlek = skapaKortlek()
        print("Kortlek Skapad")
    
    elif(val == 2):
        kortlek = blandaKortlek(kortlek)
        print("Kortlek blandad")
        
    elif(val == 3):
        taEttKort(minaKort, kortlek)

    elif(val == 4):
        visaEttKort(minaKort)
            
    elif(val == 5):
        print(kortlek)
