from profile import profile
print("Welcome to Aarush's Basketball Simulator, created in collaboration with Maanav Singh. To get help press 1, to generate player profiles press 2")
try:
    userInput = int(input())
except:
    print("We could not recognize that command. Please enter 1 for help or 2 for profile generation")
if userInput == 1:
    #will fill out later
    pass
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