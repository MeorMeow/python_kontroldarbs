print("Sveiki! Šajā spēlē tev vajadzēs censties uzminēt 5 skaitļus no 1 līdz 50 vai 100.")
print("Katrs veiktais mēģinājums uzminēt - 2 punkti")
print("Ja spēlē no 1 līdz 50 tad:"
"Uzminot 1 skaitli + 5, "
"Uzminot 2 skaitļus + 10, "
"Uzminot 3 skaitļus + 20, "
"Uzminot 4 skaitļus + 40, "
"Uzminot 5 skaitļus + 50, "
)
print("Ja spēlē no 1 līdz 100 tad:")
print( 
"Uzminot 1 skaitli + 10, "
"Uzminot 2 skaitļus + 20, "
"Uzminot 3 skaitļus + 60, "
"Uzminot 4 skaitļus + 100, "
"Uzminot 5 skaitļus + 200, "
)

import random

sākums = input(f"Vai tu gribi minēt no 50 vai 100 cipariem?")
if sākums == "50": 
    pakape = [random.randint(1, 50) for _ in range(5)] 
    secība = sorted(pakape)
elif sākums == "100": 
    pakape = [random.randint(1, 100) for _ in range(5)]
    secība = sorted(pakape)



def minejums2():
    att = 2 
    minejums2 = "" 
    while att > 1:
        if minejums2 not in range(1,51):
            att + 0
            print("Tev vajag ievadīt no 1 līdz 50.")
        else:
            att-=1
           
        minejums2 = int(input("Mēģini uzminēt 5 skaitļus111:"))  
        
print(minejums2())




# Guessing game no 1 - 10

import random
    
num = random.randint(1, 10)
guess = None
    
while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)
    
    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")



