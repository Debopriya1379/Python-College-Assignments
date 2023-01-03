# Write a program for a matchstick game being played between the computer and a user. Your
# program should ensure that the computer always wins. Rules for the game are as follows:
#  There are 21 matchsticks.
#  The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
#  After the person picks, the computer does its picking.
#  Whoever is forced to pick up the last matchstick loses the game.


match_sticks = 21
# user_choice = 0
# computer_choice = 0

# while match_sticks >= 1 :
#     print(f'Total match sticks available : {match_sticks}')
#     print('Pick up the match sticks between (1 to 4):')
#     user_choice = int(input())

#     if user_choice > 4 or user_choice < 1 or user_choice > match_sticks:
#         print('Invalid Entry')
#         break

#     computer_choice = 5 - user_choice

#     print(f'Computer picks {computer_choice} sticks')

#     match_sticks = match_sticks - user_choice - computer_choice

#     if match_sticks == 1 :
#         print('You have been lost via Computer')

while True :
    print('There are ',match_sticks,'sticks available')
    user_choice = int(input('choose between 1 to 4 '))

    if match_sticks == 1 :
        print('Tou got the last stick , you lose')
        break

    if user_choice > 4 or user_choice <= 0 :
        print('Invalid choice')
        continue

    print('Computer took ',(5-user_choice),' sticks')
    match_sticks -= 5

