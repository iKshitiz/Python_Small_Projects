import random 
import time

def wait():
	time.sleep(2.0)

print("*"*50)
print("Welcome to Dice Game")
print("A game of Luck")
print("*"*50)
print("Roll the Dice and If 6 Come, You will Win :)")

while (True):
	user_input = input("Press 1 to role Dice\n")
	
	if(user_input == '1' or user_input == 1):
		num = random.randint(1,6)
		print("\nRolling Dice")
		wait()
		if(num == 6):
			print("You got",num)
			print("You won\n")
		else:
			print("\nYou got",num,"\nYou Lost\n")

		choice = input("Press Y to Play again\nPress N to Exit Game\n")
		
		if	(choice == 'Y' or choice == 'y'):
			continue
		elif (choice == 'N' or choice == 'n'):
			break
		else:
			print("\nPlease Enter valid Choice")
	
	else:
		print("\nNot a valid option")
