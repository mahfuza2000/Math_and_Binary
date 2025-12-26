# Exercise 3.1
from gametasks import printInstructions, getUserScore, updateUserScore
from gameclasses import Game, BinaryGame, MathGame

# Exercise 3.2
try:
    mathInstuctions = '''
    In this game, you will be given a simple arithmetic question.
    Each correct answer gives you one mark.
    No mark is deducted for wrong answers.
    '''
    binaryInstructions = '''
    In this game, you will be given a number in base 10.
    Your task is to convert this number to base 2.
    Each correct answer gives you one mark.
    No mark is deducted for wrong answers.
    '''

    bg = BinaryGame()
    mg = MathGame()

    userName = input("Type a username to keep track of your score: ")
    score = int(getUserScore(userName))

    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False

    userChoice = 0
    while userChoice != 'q':
        game = input("Math Game (1) or Binary Game (2)?: ")
        while game != '1' and game != '2':
            print("Not a valid option!")
            game = input("Math Game (1) or Binary Game (2)?: ")
        
        numPrompt = input("How many questions do you want per game (1 to 10)?: ")
        while True:
            try:
                num = int(numPrompt)
                break
            except:
                print("Invalid entry. Please type a number.")
                numPrompt = input("How many questions do you want per game (1 to 10)?: ")
        
        if game == '1':
            mg.noOfQuestions = num
            printInstructions(mathInstuctions)
            score += mg.generateQuestions()
        else:
            bg.noOfQuestions = num
            printInstructions(binaryInstructions)
            score += bg.generateQuestions()
        
        message =  "Here is your final score: %d" %(score)    
        print("\n" + "*" * len(message) + "\n" + message + "\n" +"*" * len(message))
        userChoice = input("Press 'Enter' to continue or 'q' to quit: ")
    
    updateUserScore(newUser, userName, str(score))

# Exercise 3.3
except Exception as e:
    print("An error has occured. This program will now exit.")
    print("Error: ", e)