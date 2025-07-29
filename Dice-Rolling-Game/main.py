import random

roll_count=0

while True:
  choice = int(input("Do you want to roll the dice? (1 for Yes , 0 for No)"))
  if(choice == 1):
    num_dice = int(input("How many dice would you like to roll? "))
    results = []
    for i in range(num_dice):
        results.append(random.randint(1, 6))          
    print(f"Your dice say: {results}")
    roll_count += 1
  elif(choice == 0):
    print(f"Total rolls made: {roll_count}")
    print('You choose not to roll the dice.')
    break
  else:
    print('invalid choice')
    choice = int(input("Do you want to roll the dice? (1 for Yes , 0 for No)"))
