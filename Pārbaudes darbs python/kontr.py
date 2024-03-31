print("\nSveiki! Šajā spēlē tev vajadzēs censties uzminēt skaitli no 1 līdz 50 vai 100. Skaitļi var atkārtoties.")
print("Katrs veiktais mēģinājums uzminēt - 2 punkti")
print("Ja spēlē no 1 līdz 50 tad:"
"Uzminot skaitli + 50"
)
print("Ja spēlē no 1 līdz 100 tad:")
print( 
"Uzminot skaitli + 100 punkti "
)

import random



def pakape():
    while True:
        
        pakapes_izvele = input("\nIzvēlies grūtības pakāpi 50 vai 100: ")
        if pakapes_izvele in ['50', '100']:
            return int(pakapes_izvele)

    
        else:
            print("Tev jāizvēlas 50 vai 100. Mēģini vēlreiz.")


def minējums(max_skaitlis):  
    while True:
        punktu_skaits = 0
        random_skaitlis = random.randint(1, max_skaitlis)
        mans_minejums = int(input("\nTavs minējums ir: "))

    
        if mans_minejums == random_skaitlis:
            if max_skaitlis == 50:
                punktu_skaits += 50
            elif max_skaitlis == 100:
                punktu_skaits += 100
            print(f"Tu uzminēji!!!!! Skaitlis bija {random_skaitlis}.")
        
        elif mans_minejums == 0:
            print(f"Paldies par spēli! Tavs punktu skaits ir {punktu_skaits} ")
            break
        
        else:
            print(f"Tu neuzminēji. Skaitlis bija {random_skaitlis}.")
            punktu_skaits -= 2
        
        print(f"Tavs punktu skaits: {punktu_skaits}.")
        return punktu_skaits
 

def lai_stradātu():
  
    grūtības_pakāpe = pakape()
    if grūtības_pakāpe == 50:
        punktu_skaits = minējums(50) 
        
    else:
        punktu_skaits = minējums(100)
    return punktu_skaits

    
lai_stradātu()


