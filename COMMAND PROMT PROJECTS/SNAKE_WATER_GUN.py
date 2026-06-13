import random

def Game(comp,you):
    if comp==you:
       return None
    elif comp=='s':
        if you== 'w':
            return False
        elif you== 'g':
            return True
    elif comp=='w':
        if you== 'g':
            return False
        elif you== 's':
            return True
    elif comp=='g':
        if you== 's':
            return False
        elif you== 'w':
            return True
        
print("Comp Turn: Snake(s),Water(w),gun(g)")
randomNO=random.randint(1,3)
if randomNO==1:
    comp= 's'
elif randomNO==2:
    comp= 'w'
else:
    comp= 'g'
you=input("Your Turn: Snake(s),Water(w),gun(g)\n")

print(f"Comp choose {comp}")
print(f"You choose {you}")

Game(comp,you)
a=Game(comp,you)
if a== None:
   print("T")
elif a==False:
    print("L")
elif a==True:
    print("W")