import random



print ("welcome to my MyMagicBall8.")
qu = input("Ask me for advise then pres ENTER to shake me \n")
print ("shaking...\n"* 4)
 


Guy1 = "No thank you"
Guy2 = "No way"
Guy3 = "Fine"
Guy4 = "Why not"
Guy5 = "Can you ask me again"
Guy6 = "Go for it"
Guy7 = "Yes, that is the rifht choice"
Guy8 = "Only you can save mankind"
 
 
choice = random.randint(1,8)

if choice == 1:
	answer=Guy1
elif choice == 2:
	answer = Guy2
elif choice == 3:
	answer = Guy3 
elif choice == 4:
	answer = Guy4
elif choice == 5:
	answer = Guy5
elif choice == 6:
	answer = Guy6
elif choice == 7:
	answer = Guy7
else:
	answer = Guy8
	
	
print(answer)

input ("\n\nPress ENTER to finish.")
