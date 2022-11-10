# Sum Game

print("Welcome to Sum Game", "\n")

print("Sum Game Description:")
print("This game was founded by Ashik", "\n")

print("At the start of the game two cards will be dealt for you")
print("Then the sum of the two cards will be shown to you", "\n")

print("Based on the sum of the first two cards you have to guess how the sum of next two cards will be")
print("You will be asked to choose from the following 3 options:" + "\n" + "Less" + "\n" + "More" + "\n" + "Equal" + "\n")
print("The options are case sensitive and you have to choose one and type it in the input box")
print("If the options are entered incorrectly, you will be asked to re-enter a valid option", "\n")

print("Next you have to enter the amount you would like to bet in the input box")
print("Similarly if the bet amount is entered incorrectly, you will be asked to re-enter a valid amount", "\n")

print("If you choose Less or more as your choice option and it turns out to be right, then you win the bet amount")
print("If you choose Less or more as your choice option and it turns out to be wrong, then you lose the bet amount", "\n")

print("If you choose Equal as your choice option and it turns out to be right, then you win double the bet amount")
print("If you choose Equal as your choice option and it turns out to be wrong, then you lose double the bet amount", "\n")

print("Next the third and fourth cards are dealt and their sum is displayed")
print("Along with that your result is displayed if you have won or lost", "\n")

print("Finally your current account balance amount after the round of game is shown to you")
print("If you finish your bet amount and it goes to 0 then the game terminates automatically")
print("After every 5 rounds you will be asked if you want to continue playing. Choose 'N' or 'n' to quit")
print("If you decide to quit playing in the middle then Choose 'Q' or 'q' in the choice input to quit", "\n")

import random

# Writing a function called chosen to determine if the second number is more or less or equal to the first number

def chosen(num1, num2):
    
    if num2 > num1:
        return "More"
    elif num2 < num1:
        return "Less"
    else:
        return "Equal"
    
money = 50
current_round = 1

print("Your account balance at start: $", money, "\n")

while True:
    card1 = random.randint(1,13)
    card2 = random.randint(1,13)
    
    sum12 = card1 + card2
    
    print("Round", current_round, "\n")
    
    print("SUM GAME BEGINS NOW!!", "\n")
    
    print("Your first two cards are: ", card1,"\t", card2)
    print("The sum of your first two cards are: ", sum12, "\n")
        
    print("Sum of your next two numbers will be? " + "\n" + "Less" + "\n" + "More" + "\n" + "Equal" + "\n")
    
    choice = input("Enter your Choice? ")
    
    if choice == "Q" or choice == "q":
        break
        
    while True: 
        if choice == 'Less' or choice == 'More' or choice == 'Equal': 
            break
        else:
            print("Please choose and enter a valid option", "\n")
            choice = input("Enter your Choice? ")  
    
    bet = int(input("How much do you want to bet? "))  
    while bet > money or bet < 0:
        print("Please enter a valid amount")
        bet = int(input("How much do you want to bet? ")) 
    
    card3 = random.randint(1,13)
    card4 = random.randint(1,13)
    
    sum34 = card3 + card4
    
    print("\n" + "Your next two cards are: ", card3,"\t", card4)
    print("The sum of your next two cards are: ", sum34, "\n")
    
    if bet != 0:
        if choice == chosen(sum12, sum34):
            if chosen(sum12, sum34) == 'Equal':
                print('Yay!! You Won Double bonus!! Congrats!!')
                money += (bet * 2)
            else:
                print('Yay!! Congrats!! You Won!!')
                money += bet
        elif choice == 'Equal' and chosen(sum12, sum34) != 'Equal':
            print('Sorry, You Lost Double bonus!! Better luck next time!!')
            money -= (bet * 2)
        else:
            print('Sorry, You Lost. Better luck next time!!')
            money -= bet
        
    # if you are out of money, leave the loop
    print("Now your account balance is: $", money, "\n")
    print("-" * 117, "\n")
    if money <= 0:
        break
        
    if current_round % 5 == 0:
        cont_play = input("Do you want to continue playing Y/N: ")
        if cont_play == "N" or cont_play == "n":
            break # stops the loop from running and exits the loop
    
    current_round += 1

print("\n" + "Thanks for playing Sum Game. Have a great day. Good bye!!")
