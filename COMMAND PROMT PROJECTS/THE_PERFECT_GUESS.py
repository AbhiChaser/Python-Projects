import random
randomNo=random.randint(1,100)
print("THE NUMBER OF TURNS AVAILABLE TO YOU IS 10\n\n")

for i in range(1,11):
   userNO= int(float(input("\nENTER YOUR GUESS\n")))
   if randomNo == userNO :
       print(f"YOU GUESSED RIGHT IN GUESS NUMBER{i}")
       break
   elif randomNo>userNO :
       print("YOUR CURRENT GUESS IS WRONG\nTHE RANDOM NUMBER IS BIGGER\n")
       print(f"REMAINING GUESSES : {10-i}\n")
   elif randomNo<userNO :
       print("YOUR CURRENT GUESS IS WRONG\nTHE Random NUMBER IS SMALLER\n")
       print(f"REMAINING GUESSES : {10-i}\n")
           