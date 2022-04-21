'''import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from unicodedata import name
from matplotlib import pyplot as plt
from numpy import delete
from scipy.stats import entropy
#import tabulate

randomList = [10, 30, 60, 0]


def listToString(list): #Function that turns a list into a string
    str = ""
    for ele in list:
        str += ele
    return str


def stringFont(outputFile, string, l, massProbFunc, stringSize=-1):
    j = 0
    retString = ''
    while (j < l):
        subString = ''
        if (stringSize == -1):  #If the user doesn't pass a stringSize as a parameter, we pick a random int between 1 and 15
            stringActualSize = random.randint(1, 15)
        else:
            stringActualSize = stringSize
        subString = random.choices(string, weights=(massProbFunc), k=stringActualSize) #The function random.choices() returns a list, but it's easier to work with a String
        subString = listToString(subString) #So we turn that list into a String
        retString += subString + ';' #';' character used to separate the randomly generated sequences
        j += 1
        #The following lines of code:
        #   Write the code on a output file
        #   Split the string by the ';' character making the string a list
        #   Remove the last element because it was always a blank space
        #   Calculate the entropy of the generated file
        #   Build and show a histogram based on the generated file
    f = open(outputFile, "w") 
    f.write(retString)
    f.close()
    newRetString = retString.split(";")
    newRetString = newRetString[:-1]
    print(entropy(massProbFunc, base=2))
    plt.hist(newRetString, bins=4, edgecolor='black')
    plt.savefig(f'histogram.png')
    plt.show()
    pass


#stringFont("filetest.txt", "abcd", 5, randomList, 1)

# -----------------------//---------------------------

def passwordGen(outputFile, min, max):
    password = ""
    if (min < 4):
        raise Exception("The min has to be 4 or higher!")   #Since the password must have at least one of each "group" of totalString, the minimum size must be 4
    if (max < min):
        raise Exception("The max has to be greater than min!") #If the user enters, by mistake, a min greater or equal to max, the program doesn't work
    newMax = random.randint(min, max)   #Randomizes a int between min and max
    pList = [digits, ascii_uppercase, ascii_lowercase, punctuation] #A list with all the "groups" of totalString
    i = 0
    while (i < len(pList)):
        currString = random.choice(pList)  
        #In order to have at least one of each "group" in the password, we pick one randomly, and then remove it from the list, so that it doesn't get picked again
        pList.remove(currString)    
        currElement = random.choice(currString)
        password += currElement #Adding a new random char from totalString until we have one random char of each "group" of totalString
        totalString = digits + ascii_uppercase + ascii_lowercase + punctuation  #Builds a string that contains all the elements we have to use in the alphaNumeric
    while (newMax - len(password) > 0):
        password += random.choice(totalString)  #Adding a new random char from totalString until we reach newMax
    f = open(outputFile, "w")   #Opens the file so that we can write on it
    f.write(password)
    f.close()


#passwordGen(5,10)

# -----------------------//---------------------------

def alphaNumericGen(outputFile, l=24):
    alphaNumeric = ""
    totalString = digits + ascii_uppercase          #Builds a string that contains all the elements we have to use in the alphaNumeric
    i = 1
    while (i <= l):                                 
        alphaNumeric += random.choice(totalString)  #Adding a new random char from totalString until we reach the size passed as parameter
        if (i % 4 == 0): alphaNumeric += " "        #Formatting the alphaNumeric so that for each for letters it has a space, has demonstrated 
        i += 1
    f = open(outputFile, "w")                       #Opens the file so that we can write on it
    f.write(alphaNumeric)               
    f.close()  
# ------------------//-----------------------
import linecache

#def readLines(file):
 #   openFile = open(file)
  #  i = 0 
   # lines = 0 
    #while( i < len(openFile)):
     #   if(openFile[i] == '\n'):
      #      lines = lines + 1
       # i = i + 1   
    #return lines

#def countLines(file):
 #   lines = 0
  #  openFile = open(file, 'r')
   # for i in openFile:
    #    lines = lines + 1
    #return lines

def randomNameGenerator():
    firstNamesFile = "C:/Users/paula_000/PycharmProjects/pythonProject/Nomes.txt"
    firstNamesLength = len(open(firstNamesFile, encoding="utf8").readlines())
    surnamesFile = "C:/Users/paula_000/PycharmProjects/pythonProject/Apelidos.txt"
    surnamesLength = len(open(surnamesFile, encoding="utf8").readlines())
    name = linecache.getline(firstNamesFile, random.randint(0, firstNamesLength))
    surname = linecache.getline(surnamesFile, random.randint(0, surnamesLength))
    randomNumber = random.randint(1, 3)
    match randomNumber: 
        case 1:
            name += surname
        case 2:
            secondName = linecache.getline(firstNamesFile, random.randint(0, firstNamesLength))
            name += secondName + surname
        case 3:
            secondName = linecache.getline(firstNamesFile, random.randint(0, firstNamesLength))
            secondSurname = linecache.getline(surnamesFile, random.randint(0, surnamesLength))
            name += secondName + surname + secondSurname
    return name = name.replace('\n','')
            
print(randomNameGenerator())'''