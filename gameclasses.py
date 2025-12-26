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
        from random import randint 
        
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
        
        message =  "Here is your final score: %d" %(score)    
        print("\n" + "*" * len(message) + "\n" + message + "\n" +"*" * len(message))
        return   

# Exercise 2.3
class MathGame(Game):
     

# intermediate testing:
# game = BinaryGame(noOfQuestions=3)
# game.generateQuestions()