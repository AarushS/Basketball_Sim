from profile import profile
print("Welcome to Aarush's Basketball Simulator, created in collaboration with Maanav Singh. To get help press 1, to generate player profiles press 2")
try:
    userInput = int(input())
except:
    print("We could not recognize that command. Please enter 1 for help or 2 for profile generation")
if userInput == 1:
    print("Welcome to Aarush's Basketball Simulator, created in collaboration with Maanav Singh.")
    print("This simulator procedurally generates player profiles with statistics, which you can then pit together")
    print("in 1v1 scenarios to determine who is the better basketball player. When you input 2, you will be asked how many players")
    print("you wish to generate. Any number can be inputted.")
elif userInput == 2:
    print("How many players would you like to generate profiles for?")
    userInput = int(input())
    playerArray = []
    for _ in range(userInput):
        playerArray.append(profile())
    for i in playerArray:
        for k, v in i.getStats().items():
            print(k, v)
        print("\n")
