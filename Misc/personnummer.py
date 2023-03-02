from time import sleep

def kollaLän(år):
    
    if år >= 0 and år <= 13:
        plats = "Stockholms Län"
    elif år >= 14 and år <= 15:
        plats = "Uppsala Län"
    elif år >= 16 and år <= 18:
        plats = "Södermanlands Län"
    elif år >= 19 and år <= 23:
        plats = "Östergötlands Län"
    elif år >= 24 and år <= 26:
        plats = "Jönköpings Län"
    elif år >= 27 and år <= 28:
        plats = "Kronobergs Län"
    elif år >= 29 and år <= 31:
        plats = "Kalmar Län"
    elif år == 32:
        plats = "Gotlands Län"
    elif år >= 33 and år <= 34:
        plats = "Blekinge Län"
    elif år >= 35 and år <= 38:
        plats = "Kristianstads Län"
    elif år >= 39 and år <= 45:
        plats = "Malmöhus Län"
    elif år >= 46 and år <= 47:
        plats = "Hallands Län"
    elif år >= 48 and år <= 54:
        plats = "Göteborgs och Bohus Län"
    elif år >= 55 and år <= 58:
        plats = "Älvsborgs Län"
    elif år >= 59 and år <= 61:
        plats = "Skaraborgs Län"
    elif år >= 62 and år <= 64:
        plats = "Värmlands Län"
    elif år >= 66 and år <= 68:
        plats = "Örebro Län"
    elif år >= 69 and år <= 70:
        plats = "Västmanlands Län"
    elif år >= 71 and år <= 73:
        plats = "Kopparbergs Län"
    elif år >= 75 and år <= 77:
        plats = "Gävleborgs Län"
    elif år >= 78 and år <= 81:
        plats = "Västernorrlands Län"
    elif år >= 82 and år <= 84:
        plats = "Jämtlands Län"
    elif år >= 85 and år <= 88:
        plats = "Västerbottens Län"
    elif år >= 89 and år <= 92:
        plats = "Norrbottens Län"
    else:
        plats = "Extranummer"
        
    return plats
    
def personnummer(personnummer):
    info = ""
    summa = 0

    for loop in range(len(personnummer)):
        if ord(personnummer[loop]) < 48 and ord(personnummer[loop]) > 57:
            return "Får bara innehålla siffror"

    if len(personnummer) != 10:
        return "Inkorrekt längd av personnummer, får bara innehålla 10 siffror"
    
    år = personnummer[0:2]
    månad = personnummer[2:4]
    dag = personnummer[4:6]
    födelseplats = int(personnummer[6:8])
    könnummer = int(personnummer[8])
    
    if int(år) < 22:
        år = str(år)
        år = "20" + år
    else:
        år = "19" + år
    
    län = kollaLän(födelseplats)
        
    if könnummer%2:
        kön = "Man"
    else:
        kön = "Kvinna"
        
    
    for loop in range(len(personnummer) - 1):
        tal = 0
        if loop%2:
            tal = 1 * int(personnummer[loop])
            
        else:
            tal = 2 * int(personnummer[loop])


        tal = str(tal)
        if len(tal) >= 2:
            summa += int(tal[0]) + int(tal[1])
        else:
            summa = summa + int(tal)
            

    datum = str(år) + "-" + str(månad) + "-" + str(dag)

    if (10-(summa%10)%10 == int(personnummer[9]) and (valideraDatum(månad, dag))):
        info += "Korrekt kontrollnummer \n"
        info += "Födelsedaturm: "+ datum + "\n"
        info += "Kön: " + kön + "\n"
        info += "Län: " + län + "   VIKTIGT! Detta gäller om man är född före 1990 1 januari \n"
        return info
    else:
        info += "Inkorrekt kontrollnummer"

        if(10-(summa%10)%10 == int(personnummer[9])):
            print("Personnummret stämmer inte överens med kontrollsiffran")

        if valideraDatum(månad, dag) != True:
            print("Fel månad eller dag!")

        return info
    
def valideraDatum(mån, dag):
    
    mån = int(mån)
    dag = int(dag)

    if float(mån/12) > 1 or mån == 0:
        return False

    if mån == 1 or mån == 3 or mån == 5 or mån == 7 or mån == 8 or mån == 10 or mån == 12:
        if dag > 31 or dag == 0:
            return False
    
    if mån == 4 or mån == 6 or mån == 9 or mån == 10:
        if dag > 30 or dag == 0:
            return False
    
    if mån == 2:
        if dag > 28:
            return False
    
    return True

print("Personnummer")

print(personnummer(input(("ÅÅMMDDXXXX:  "))))
