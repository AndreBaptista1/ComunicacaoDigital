'''
   sym = str(input("Indique o caracter que deseja ver"))
i = 0
with open("test.txt", "r") as f:
    for line in f:
     for ch in line:
        if ch == sym:
            i += 1
print("{}".format(i))

'''
from collections import Counter


def mostSymbol(filepath):
    '''file = open(filepath,"r")
    frequency = {}
    for ch in file:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1    '''

    with open(filepath) as f:
        amount = Counter(f.read())
    '''res = max(amount, key=amount.get)'''
    symbol = amount.most_common(3)
    print('The most frequent symbol is {} and appears with a frequency of {} '.format(symbol[0][0], symbol[0][1]))

    '''print('\n'.join(f'letter "{letter}": {count}' for letter, count in amount.items()
                    if letter != '\n'))'''
    '''print("Frequency ->" + str(amount))
    print("Character ->" + str(res))'''



mostSymbol("Text.txt")
