print("Welcome to snake, water, gun game!")
print()
print("Rules of the game are: \n1:Snake drinks water, snake wins\n2:Gun flows in the water, water wins \n3:Gun kills the snake, gun wins ")
print()
print("To select your choice type:\n1.s for snake \n2.w for water \n3.g for gun")
print()

#function defination for game
def snake_water_gun():
    import random
    #initializing score to 0
    player_score=0
    computer_score=0
    turns=int(input('How many rounds you want to play: '))
    print ("You will play total",turns,"rounds!")
    #display the number of round 
    for i in range(turns):
        # Add a space before starting each round for clarity
        print("-"*35)  
        print(f'Round {i+1}: ')

        #choices stored in dictionary 
        dict={'s':'snake','w':'water','g':'gun'}
        #take input from player
        player=input("Enter your choice: ").lower()
        # Validate player's input
        if player not in dict:
            print("Invalid input! \nPlease choose 's', 'w', or 'g'.")
            continue  # Skip the rest of the loop and prompt for a valid choice
        computer=random.choice(["s","w","g"])
        print('You chose: ',dict[player])
        print('Computer chose: ', computer)

        #start game
        if player==computer:
            print('It\'s a tie')
        else:
            if (player=='s' and computer=='w'):
                print('You win ')
                player_score+=1
            elif (player=='s' and computer=='g'):
                print('You lose')
                computer_score+=1
            elif (player=='w' and computer=='s'):
                print('You lose')
                computer_score+=1
            elif (player=='w' and computer=='g'):
                print('You win')
                player_score+=1
            elif (player=='g' and computer=='s'):
                print('You win')
                player_score+=1
            elif (player=='g' and computer=='w'):
                print ('You lose')
                computer_score+=1

        # Display scores after each round
        print(f'Player score: {player_score}')
        print(f'Computer score: {computer_score}')
        
    # Display the final result
    print("-"*35)
    print('Final score:')
    print(f'Player score: {player_score}')
    print(f'Computer score: {computer_score}')
    
    if (player_score > computer_score):
        print('You won the game \nCongratulations!')
    elif (player_score < computer_score):
        print('You lost the game \nBetter luck next time!')
    else:
        print('It\'s a tie!')

snake_water_gun()
print('-'*35)
while True:
  choice=input("Do you want to play again? (yes/no): ").lower()
  if choice=='yes':
      snake_water_gun()
      break
  elif choice=='no':
      print("Thank you for playing!")
      break
  else:
      print("Invalid choice! \nPlease type 'yes' or 'no'.")
