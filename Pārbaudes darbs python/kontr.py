print("\nSveiki! Šajā spēlē tev vajadzēs censties uzminēt skaitli no 1 līdz 50 vai 100.")
print("Katrs veiktais mēģinājums uzminēt -2 punkti.")

print("\nJa spēlē no 1 līdz 50 tad:")
print("Uzminot skaitli + 50")

print("Ja spēlē no 1 līdz 100 tad:")
print("Uzminot skaitli + 100 punkti ")

print("\nJa vēlies pabeigt spēli vai nomainīt gŗūtību, tad veicot minējumu ieraksi 0.")

import random

def pakape():
    
    while True:
        pakapes_izvele = input("\nIzvēlies grūtības pakāpi 50 vai 100: ")
        
        if pakapes_izvele in ['50', '100']:
            return int(pakapes_izvele)
        
        else:
            print("Tev jāizvēlas 50 vai 100. Mēģini vēlreiz.")



def minējums(max_skaitlis):  
    punktu_skaits = 0
    
    while True:
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
        
        elif mans_minejums < 1 or mans_minejums > max_skaitlis:
            print(f"Minējumam jābūt ietvaros no 1 līdz {max_skaitlis}. Mēģini vēlreiz.")
            
        else:
            print(f"Tu neuzminēji. Skaitlis bija {random_skaitlis}.")
            punktu_skaits -= 2
        
        print(f"Tavs punktu skaits: {punktu_skaits}.")


def lai_stradātu():  
    
    while True:
        grūtības_pakāpe = pakape()
        
        if grūtības_pakāpe == 50:
             minējums(50) 
        else:
             minējums(100)

print(lai_stradātu())
