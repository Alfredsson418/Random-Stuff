minaKort = []
bankKort = []
stop = ""
taSvar = 0
EssVärde = 0
bankTurn = 0
bankVinst = 0
SpelareVinst = 0

import os
from time import sleep


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


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
    
def taEttKort(hand, kortlek):
    hand.append(kortlek[0])
    kortlek.pop(0)


def visaEttKort(hand):
    if(len(hand) != 0):
        print(hand)

def översätt(hand, vemsTur, EssSumma):
    "♣", "♦", "♥", "♠"
    Kung = 10
    Dam = 10
    Knekt = 10
    summa = 0
    antal = 0
    antalFS = 0
    if vemsTur == "bank":
        for loop in range(len(hand)):
            temp = hand[loop]
            
            value = temp[0:len(hand[loop]) - 1]

            if(value == "Kung"):
                summa = summa + Kung
            elif(value == "Dam"):
                summa = summa + Dam
            elif(value == "Knekt"):
                summa = summa + Knekt
            elif(value == "Ess"):
                antal = antal + 1
            elif(value == "?"):
                summa = "??"

            elif(int(value) >= 2 and int(value) <= 10):
                summa = summa + int(value)

        for loop in range(antal):
            if(summa == "??"):
                break
            elif(summa > 10):
                summa = summa + 1
            else:
                summa = summa + 11
        
    if vemsTur == "spelare":
        for loop in range(len(hand)):
            temp = hand[loop]
            
            value = temp[0:len(hand[loop]) - 1]

            if(value == "Kung"):
                summa = summa + Kung
            elif(value == "Dam"):
                summa = summa + Dam
            elif(value == "Knekt"):
                summa = summa + Knekt
            elif(value == "?"):
                summa = "??"

            elif(value == "Ess"):
                summa = summa

            elif(int(value) >= 2 and int(value) <= 10):
                summa = summa + int(value)
        summa = summa + EssSumma
    return summa
        

def svarPåSpel(hand, bank):
    global bankVinst, SpelareVinst

    if(hand > 21 and bank > 21):
        print("Båda är förlorare")

    elif(hand > 21):
        print("Förlorare")
        bankVinst = bankVinst + 1

    elif(hand > bank and hand <= 21):
        print("Vinnare")
        SpelareVinst = SpelareVinst + 1

    elif(hand < bank and bank <= 21):
        print("Förlorare")
        bankVinst = bankVinst + 1

    elif(hand <= 21 and bank > 21):
        print("Vinnare")
        SpelareVinst = SpelareVinst + 1

    elif(hand == bank):
        print("Lika")

    
    

def bankAI(bank, kortlek, hand):
    if(översätt(bankKort, "bank", 0) <= 16):
        taEttKort(bankKort, kortlek)

    clearConsole()
    spel(minaKort, bankKort, "bank")


def spel(hand, bank, vemsTur):
    clearConsole()
    if(vemsTur == "bank"):
        print("-------------------------------------------------------------------------")       
        print("         Bankens kort         Antal Vinster: ", bankVinst)
        print("   ",bank, " Det blir en summa på: ", översätt(bank, "bank", 0))
        print()
        print()
        print("         Dina kort         Antal Vinster: ", SpelareVinst)
        print("   ",hand, " Det blir en summa på: ", översätt(hand, "spelare", EssSumma))
        print("-------------------------------------------------------------------------")
    else:
        temp = 0
        temp = bank[1]
        bank[1] = "??"
        print("-------------------------------------------------------------------------")
        print("         Bankens kort         Antal Vinster: ", bankVinst)
        print("   ",bank, " Det blir en summa på: ", översätt(bank, "bank", 0))
        print()
        print()
        print("         Dina kort         Antal Vinster: ", SpelareVinst)
        print("   ",hand, " Det blir en summa på: ", översätt(hand, "spelare", EssSumma))
        print("-------------------------------------------------------------------------")
        bankKort[1] = temp


        




while(stop != "2"):
    kortlek = skapaKortlek()
    kortlek = blandaKortlek(kortlek)
    clearConsole()
    bankTurn = 0
    for loop in range(2):
        taEttKort(minaKort, kortlek)
        taEttKort(bankKort, kortlek)


    while(True):
        EssSumma = 0

        #----------------------
        spel(minaKort, bankKort, "spelare")

        for Ess in range(len(minaKort)):
            
            EssTemp = minaKort[Ess]
            
            EssValue = EssTemp[0:len(minaKort[Ess]) - 1]

            if(EssValue == "Ess"):
                if översätt(minaKort, "spelare", 11) == 21:
                    EssSumma = 11
                    break
                elif översätt(minaKort, "spelare", 1) == 21 or översätt(minaKort, "spelare", 11) > 21:
                    EssSumma = 1
                    break
                else:
                    while(EssVärde != 11 or EssVärde != 1):
                        EssVärde = input("Vilket värde vill du att " + minaKort[Ess] + " ska ha? 1 eller 11? ")
                        if(EssVärde == "11" or EssVärde == "1"):
                            EssSumma = int(EssSumma) + int(EssVärde)
                            break

                spel(minaKort, bankKort, "spelare")


        if översätt(minaKort, "spelare", EssSumma) > 21 or översätt(minaKort, "spelare", EssSumma) == 21:
            break

        while(True):
            print("1. Ta kort")
            print("2. Stanna")
            taSvar = input("Vad vill du göra? ")
            if(taSvar == "1" or taSvar == "2"):
                break

        if(taSvar == "1"):
            taEttKort(minaKort, kortlek)
        else:
            break
        

        #----------------------
    while True: 

        spel(minaKort, bankKort, "bank")

        if översätt(bankKort, "bank", 0) > översätt(minaKort, "spelare", EssSumma) or översätt(bankKort, "bank", 0) == 21:
            break
        elif översätt(minaKort, "spelare", EssSumma) > 21:
            break
        else:
            taEttKort(bankKort, kortlek)
            spel(minaKort, bankKort, "bank")

    svarPåSpel(översätt(minaKort, "spelare", EssSumma), översätt(bankKort, "bank", 0))
    
    sleep(1)
    print("1. För att köra igen")
    print("2. För att avsluta")
    sleep(1)
    stop = input("Vad vill du göra? ")
    if(stop == "1"):
        minaKort = []
        bankKort = []
    else:
        break