
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

import random

a= int(float(input("\nENTER THE RANGE OF NUMBER STARTING FROM 1 \n")))
randomNo=random.randint(1,a)

def PERG(a,g):
    for i in range(1,a+1):
        UserNO=int(float(input("ENTER YOUR GUESS\n")))
        if randomNo==UserNO:
            print(Fore.YELLOW+f"YOU GUESSED THE NUMBER RIGHT IN TURN NUMBER {i}")
            break
        elif randomNo>UserNO:
            print(Fore.YELLOW+f"YOUR GUESS IS WRONG AS THE NUMBER IS BIGGER THAN YOUR GUESS ")
            print(Fore.YELLOW+f"REMAINING GUESSES {g-i}")
        elif randomNo<UserNO:
            print(Fore.YELLOW+f"YOUR GUESS IS WRONG AS THE NUMBER IS SMALLER THAN YOUR GUESS ")
            print(Fore.YELLOW+f"REMAINING GUESSES {g-i}")


if  a>=100 and a<200:
    g=10
    print(Fore.GREEN+f"THE NUMBER OF TURNS YOU HAVE ARE {g}")
    PERG(a,g) 
elif a>=200 and a<300:
    g=30
    print(Fore.GREEN+f"THE NUMBER OF TURNS YOU HAVE ARE {g}")
    PERG(a,g)
elif a>=300 and a<400:
    g=60
    print(Fore.GREEN+f"THE NUMBER OF TURNS YOU HAVE ARE {g}")
    PERG(a,g)
elif a>=400 and a<500:
    g=80
    print(Fore.GREEN+f"THE NUMBER OF TURNS YOU HAVE ARE {g}")
    PERG(a,g)
elif a>=500 and a<501:
    g=100
    print(Fore.GREEN+f"THE NUMBER OF TURNS YOU HAVE ARE {g}")
    PERG(a,g)
elif 100>a or a>501:
    print(Fore.RED+"PLEASE SELECT RANGE BETWEEN 100  to 500")
