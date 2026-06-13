import random

def Game(comp,you):
    if comp==you:
       return None
    elif comp=='st':
        if you== 'sc':
            return False
        elif you== 'pr':
            return True
    elif comp=='pr':
        if you== 'st':
            return False
        elif you== 'sc':
           return True
    elif comp=='sc':
        if you== 'pr':
            return False
        elif you== 'st':
            return True
        
print("Comp Turn: stone(st),paper(pr),scissor(sr)")
randomNO=random.randint(1,3)
if randomNO==1:
    comp= 'st'
elif randomNO==2:
    comp= 'pr'
else:
    comp= 'sc'
you=input("Your Turn: stone(st),paper(pr),scissor(sr)\n")

print(f"Comp choose {comp}")
print(f"You choose {you}")

Game(comp,you)
a=Game(comp,you)
if a== None:
   print("TIE")
elif a==False:
    print("LOSE")
elif a==True:
    print("WIN")
