import datetime
import linecache
import random
import string

from tabulate import tabulate


def randomBet():
    # AvailableNums = list(["%.2d % i" for i in range(1,50)])
    AvailableNums = list((range(1, 51)))
    BetNums = random.sample(AvailableNums, 5)
    return BetNums
    '''list = []
    i = 0
    y = 0
    j = i + 1
    for x in range(amount):
        rand_nmb = (random.randrange(min, max, 1))
        list.append(rand_nmb)
    print(list)
    for i in range(0, len(list)):
        j = 0
        while j < len(list):
            aux0 = list[i]
            aux1 = list[j]
            print('{}, {}'.format(aux0, aux1))
            if list[i] == list[j]:
                list.pop(j)
                list.append(random.randrange(min, max, 1))
                j += 1
            else:
                j += 1

    return list'''


def randomStars():
    # AvailableStars = list(["%.2d % i" for i in range(1,11)])
    AvailableStars = list(range(1, 12))
    BetStars = random.sample(AvailableStars, 2)
    return BetStars

    '''list = []
    for x in range(amount):
        rand_stars = (random.randrange(min, max, 1))
        list.append(rand_stars)
    while list[1] == list[0]:
        list.remove(list[1])
        list.append(random.randrange(min, max, 1))
    return list'''


def ApostaFinal():
    numbersRange = range(1, 51)
    starsRange = range(1, 12)
    aposta = random.sample(numbersRange, 5)
    aposta += random.sample(starsRange, 2)
    for i in range(0, len(aposta)):
        if aposta[i] < 10:
            aposta[i] = f'0{aposta[i]}'
    lastBet = ' '.join([str(i) for i in aposta])

    return lastBet


def randomQuantia():
    n = 0
    # for i in range(0,100):
    n += random.randint(50, 1000)
    return "{}€".format(n)


'''def listToString(l):
    str=" "
    for i in l:
        str+=i
    return str'''


def randomNames(n, filepath):
    x = 0
    with open(filepath) as f:
        line = f.readlines()
        while x < n:
            res = random.choice(line)
            x += 1
            print(res, end='')
    return ''


def randomSurname(n, filepath):
    x = 0
    with open(filepath) as f:
        line = f.readlines()
        while x < n:
            res = random.choice(line)
            x += 1
            print(res, end='')
    return ''


def randomCC():
    n = '{:08}'.format(random.randint(0, 10 ** 8 - 1))
    return n


def randomNameGenerator():
    firstNamesFile = "C:/Users/paula_000/PycharmProjects/pythonProject/Nomes.txt"
    firstNamesLength = len(open(firstNamesFile, encoding="utf8").readlines())
    surnamesFile = "C:/Users/paula_000/PycharmProjects/pythonProject/Apelidos.txt"
    surnamesLength = len(open(surnamesFile, encoding="utf8").readlines())
    name = linecache.getline(firstNamesFile, random.randint(0, firstNamesLength))
    surname = linecache.getline(surnamesFile, random.randint(0, surnamesLength))
    randomChoice = random.randint(1, 3)
    match randomChoice:
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


def randomLocation():
    locationFile = "C:/Users/paula_000/PycharmProjects/pythonProject/Concelhos.txt"
    locationLength = len(open(locationFile, encoding="utf8").readlines())
    location = linecache.getline(locationFile, random.randint(0, locationLength))
    return location


def randomJob():
    jobFile = "C:/Users/paula_000/PycharmProjects/pythonProject/Profissões.txt"
    jobLength = len(open(jobFile, encoding="utf8").readlines())
    job = linecache.getline(jobFile, random.randint(0, jobLength))
    return job


def randomDate():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2022, 12, 31)
    time_elapsed = end_date - start_date
    days_elapsed = time_elapsed.days
    random_day = random.randrange(days_elapsed)
    random_date = start_date + datetime.timedelta(days=random_day)
    return "{}-{}-{}".format(random_date.day, random_date.month, random_date.year)


def nRandomNames(n):
    list = []
    for i in range(0, n):
        list.append([randomNameGenerator()])
    return list

def cc(n):
    x = 0
    for i in range(0,n):
     x = randomCC()
    return  x

def randomInfo(n):
    list = []
    for i in range(0, n):
        list.append([randomCC(), randomNameGenerator(), randomLocation(), randomJob()])
    return list


def randomNApostas(n):
    list = []
    for i in range(0, n):
        list.append([randomCC(), ApostaFinal(), randomDate(), randomQuantia()])
    return list


print(randomInfo(3))
print(randomDate())
# print(randomNameGenerator())

'''
def testfuncn(n, min, max):
    a = list(range(min, max))
    bet = random.sample(a, n)
    return bet'''

# print(testfuncn(5,1,50))
# print(randomBet(5, 1, 5))
# print(randomStars(2, 1, 3))
print(ApostaFinal())
# print("----CC----")
# print(randomCC())
# print("----Nomes Própios----")
# print(randomNames(5, "Nomes.txt"))
# print("----Apelidos----")
# print(randomSurname(5, "Apelidos.txt"))

# list = ['{},{},{},{},{}'.format(random.randint(1, 50), end='')]



headers = ["Numero de Cidadao", "Nome(s) Próprio(s) e Apelido(s)", "Concelho de Residência", "Profissão"]
headers_aposta = ["Numero de Cidadao", "Aposta", "Data", "Quantia"]

pessoas = {'Numero de Cidadao': [randomCC()], 'Nome(s) Próprio(s) e Apelido(s)': [randomNameGenerator()],
           'Concelho de Residência': [randomLocation()],
           'Profissao': [randomJob()]}

# table = {'Número de Cidadão': [randomCC()], 'Aposta': [ApostaFinal(5, 1, 50, 2, 1, 11)], 'Nome': []}

info_pessoas = open("PessoasFINAL.txt", "w")
test_ex = open("TEST.txt", "w")
# text_file = open("APOSTAS.txt", "w")
finalInfo = open("INFORMATION.txt", "w")
ApostasInfo = open("INFOAPOSTAS.txt", "w")

ApostasInfo.write(tabulate(randomNApostas(100), headers=headers_aposta, tablefmt='github'))
finalInfo.write(tabulate(randomInfo(100), headers=headers, tablefmt='github'))
# test_ex.write((tabulate(test.keys(),headers='keys')))
info_pessoas.write((tabulate(pessoas, headers='keys', tablefmt='github')))
# text_file.write(tabulate(table, headers='keys', tablefmt='github', stralign='center'))
# print(tabulate(pessoas,headers='keys',tablefmt='github',stralign='center'))
print(tabulate(randomInfo(3), headers=headers, tablefmt='github'))
