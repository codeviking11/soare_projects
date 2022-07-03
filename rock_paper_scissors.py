from random import choice

selections = ['rock', 'paper', 'scissors']

user = input('Please select from rock, paper, scissors: ').lower()

while user not in selections:
    print('rock, paper, scissors')
    user = input("Please select from the list above: ").lower()

bot = choice(selections).lower()

try:
    if __name__ == '__main__':

        if (user == 'rock' and bot == 'scissors') or (user == 'paper' and bot == 'rock') or (
                user == 'scissors' and bot == 'paper'):
            print('Player wins')
            print(f"Bot has {bot}")
        elif (user == 'rock' and bot == 'paper') or (user == 'paper' and bot == 'scissors') or (
                user == 'scissors' and bot == 'rock'):
            print('Player lost')
            print(f"Bot has {bot}")
        else:
            print('Something went wrong happened')
except IndexError as err:
    print('This is not the main file')
