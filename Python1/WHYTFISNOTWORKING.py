import linecache
import  random

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
    name = name.replace('\n', ' ')
    return name


print(randomNameGenerator())