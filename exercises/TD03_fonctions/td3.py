#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    x=temps[0]*86400+temps[1]*3600+temps[2]*60+temps[3]
    return x
    pass

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   



def secondeEnTemps(seconde):
    jour= seconde//86400
    heure=(seconde - (86400*jour))//3600
    minute=(seconde-(86400*jour)-(3600*heure))//60
    secondes=(seconde-(86400*jour)-(3600*heure)-(60*minute))
    time=(jour,heure,minute,secondes)
    return time

    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#fonction auxiliaire ici

def affichePlu(val,mot):
    if val!=0:
        print(" ",val,mot,end="")
    if val>1:
        print("s",end="")    

def afficheTemps(temps):
    affichePlu(temps[0],"jour")
    affichePlu(temps[1],"heure")
    affichePlu(temps[2],"minute")
    affichePlu(temps[3],"seconde")
     

afficheTemps((1,0,14,23))   



def demandeTemps():
    jour=int(input("\n Veuillez ecrire le nombre de jour"))
    heure=int(input("\n veuillez ecrire le nombre de heure"))
    minute=int(input("\n veuillez ecrire le nombre de minute"))
    seconde=int(input("\n veuillez ecrire le nombre de seconde"))
    while jour<0:
        jour = int(input("\n Veuillez reecrire le nombre de jour"))
    while heure >10 or heure<0:
        heure=int(input("\n veuillez reecrire le nombre de heure"))  
    while minute>59 or minute<0:  
        minute=int(input("\n veuillez reecrire le nombre de minute"))   
    while seconde>59 or seconde<0: 
       seconde=int(input("\n veuillez reecrire le nombre de seconde"))     
    c=(jour,heure,minute,seconde)
    return c    

afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    return secondeEnTemps(tempsEnSeconde(temps1)+tempsEnSeconde(temps2))

sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(temps,proportion):
    x=(tempsEnSeconde(temps)*proportion)
    return secondeEnTemps(x)
    
afficheTemps(proportionTemps((2,0,36,0),0.2))

def tempsEnDate(temps):
    annee= temps[0]// 364+1970
    jour= temps[0] %365
    return (annee, jours,temps[1],temps[2],temps[3])


def afficheDate(date = -1):
    print(date[0],"annee",end="")
    afficheTemps((date[1],date[2],date[3],date[4])

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
print("\n")
afficheDate(tempsEnDate(temps))