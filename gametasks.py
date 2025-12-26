from os import remove, rename

# Exercise 1.1
def printInstructions(instuction):
    print(instuction)

# Exercise 1.2
''' userScores.txt example:
    Alice, 100
    Tom, 40
    Nancy, 60
'''
def getUserScore(userName):
    try:
        file = open('userScores.txt', 'r')
        for line in file:
            content = line.split(", ")
            print(content) #print list to see content
            if content[0] == userName:
                file.close()
                return content[1]
        file.close()
        return '-1'
    except IOError:
        print("The file 'userScores.txt' cannot be found. Creating new file...")
        file = open('userScores.txt', 'w')
        file.close()
        return '-1'

# Exercise 1.3
def updateUserScore(newUser, userName, score):
    if newUser == True:
        file = open('userScores.txt', 'a')
        file.write(userName + ", " + score + "\n")
        file.close()
    elif newUser == False:
        tempFile = open('userScores.tmp', 'w')
        file = open('userScores.txt', 'r')
        for line in file:
            content = line.split(", ")
            if content[0] == userName:
                tempFile.write(userName + ", " + score + "\n")
            else:
                tempFile.write(line)
        tempFile.close()
        file.close()
        remove("userScores.txt")
        rename("userScores.tmp", "userScores.txt")

            
