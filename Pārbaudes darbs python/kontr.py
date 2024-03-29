print("\nSveiki! Šajā spēlē tev vajadzēs censties uzminēt 5 skaitļus no 1 līdz 50 vai 100. Skaitļi var atkārtoties.")
print("Katrs veiktais mēģinājums uzminēt - 2 punkti")
print("Ja spēlē no 1 līdz 50 tad:"
"Uzminot skaitli + 50"
)
print("Ja spēlē no 1 līdz 100 tad:")
print( 
"Uzminot skaitli + 100 punkti "
)

import random


pakapes_izvele= int(input("Izvēlies grūtības pakāpi 50 vai 100: "))
def sakums():
    if pakapes_izvele == "50": 
        rand_skaitlis = [random.randint(1, 51)] 
    
    elif pakapes_izvele == "100": 
        rand_skaitlis = [random.randint(1, 101)]
    else:
        print("Ieraksti 50 vai 100.")
    


def minejums():
    
      
    while True:
        minējums = int(input("Ieraksti skaitli:")) 
         
        if minējums > 1 and minējums < pakapes_izvele:
            print(minējums)
            break
        
        else:
            print(f"Minējumam jābūt ietvaros no 1 līdz {pakapes_izvele}.")
            
            


print(minejums())



