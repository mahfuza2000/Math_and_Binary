from random import randint 

# Exercise 2.1
class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("Minimum Number of Questions = 1\n" + "Hence, number of questions will be set to 1\n")
        elif value > 10:
            self._noOfQuestions = 10
            print("Maximum Number of Questions = 10\n" + "Hence, number of questions will be set to 10\n")
        else:
            self._noOfQuestions = value

# Exercise 2.2
class BinaryGame(Game):
    def generateQuestions(self):
        score = 0
        
        for question in range(self.noOfQuestions):
            base10 = randint(1,100)
            userResult = input("\nConvert %d to a binary number: " %(base10))
            
            while True:
                try:
                    userAnswer = int(userResult, base = 2)
                    if userAnswer == base10:
                        score+=1
                        print("You are correct! \n >>>Score: %d" %(score))
                        break
                    else: 
                        print("Wrong answer. The correct answer is {:b}.".format(base10))
                        break
                except:
                    userResult = input("\nThat was not a binary number! \nConvert %d to a binary number: " %(base10))
        
        # message =  "Here is your final score: %d" %(score)    
        # print("\n" + "*" * len(message) + "\n" + message + "\n" +"*" * len(message))
        return score  

# Exercise 2.3
class MathGame(Game):
    def generateQuestions(self):
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1:" + ", 2:" - ", 3:" * ", 4:"**"}
        
        for question in range(self.noOfQuestions):    
            for i in range(0,5):
                numberList[i] = randint(1,9)    
            for i in range(0,4):
                if i != 0 and symbolList[i-1] == "**":
                    symbolList[i] = operatorDict[randint(1,3)]
                else:
                    symbolList[i] = operatorDict[randint(1,4)]
            
            questionString = str(numberList[0])  
            
            for i in range(0,4):
                questionString += symbolList[i] + str(numberList[i+1]) 
            
            result = eval(questionString)
            questionString = questionString.replace("**", "^") # replace ** with the more user-recognizable ^ symbol for exponent
            userResult = input("\nEvaluate this expression >>> %s: " %(questionString))
            
            while True:
                try:
                    userAnswer = int(userResult)
                    if userAnswer == result:
                        score += 1
                        print("You are correct! \n >>>Score: %d" %(score))
                        break
                    else: 
                        print("Wrong answer. The correct answer is {:d}".format(result))
                        break
                except:
                    userResult = input("\nThat's not a valid answer form. Please enter an integer! \nEvaluate this expression >>> %s: " %(questionString))
        
        # message =  "Here is your final score: %d" %(score)    
        # print("\n" + "*" * len(message) + "\n" + message + "\n" +"*" * len(message))
        return score
        

# intermediate testing:

# binary_game = BinaryGame(noOfQuestions=3)
# binary_game.generateQuestions()

# math_game = MathGame(noOfQuestions=2)
# math_game.generateQuestions()

