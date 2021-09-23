print('Welcome to the great game of reversi')
print('************************************')

mode = int(input('Choose game mode (1-3): '))
if mode == 1:
    print("You've chosen to play against a local opponent")
elif mode == 2:
    print("You've chosen to play an AI agent")
elif mode == 3:
    print("You've chosen to play online")
else:
    print("You've entered an invalid option")
    
print("Goodbye")