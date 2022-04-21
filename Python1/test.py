
import string
import random
import matplotlib.pyplot as plt

from scipy.stats import entropy
import pandas as pd

#exercicio 2 a)
import numpy as np


def alphabetSource(l, fmp, str):

    #str = string.digits + string.ascii_letters + string.punctuation //para ter mais do que letras
    text_file = open("EXA2.txt", "w")
    newList = []
    i = 0
    while(i<l):
        i+=1
        if(fmp == []):
            str_1 = random.choices(str,k=random.randint(1, 10))
        else:
            str_1 = random.choices(str, weights= fmp, k=random.randint(1, 10))

        rand_str = ''.join(str_1)

        newList += rand_str
        #print(newList)
        text_file.write('{};'.format(rand_str))
    text_file.close()



    arr = np.array(newList)
    plt.hist(arr,rwidth=0.9)
    plt.savefig(f'hist.png')
    plt.show()
    print(entropy(fmp,base=2))
    pass





    ''' for i in range(1,l+1):
        str_1 = random.choices(str, k=random.randint(1, 10))
        rand_str = ''.join(str_1)
        print('{}; '.format(rand_str),end='')'''


def newPasswords(min,max,l):
    str = string.digits + string.ascii_letters + string.punctuation #para ter mais do que letras
    text_file = open("EX2b.txt", "w")
    i = 0
    newList = []
    #while (i < l):
       # i += 1
    str_1 = random.choices(str, k=random.randint(min, max))
    rand_str = ''.join(str_1)
    text_file.write('{}'.format(rand_str))
    newList+=rand_str

    text_file.close()

    arr = np.array(newList)
    plt.hist(arr, rwidth=1)
    plt.savefig(f'hist2b.png')
    plt.show()
    pd_calc = pd.Series(str_1)
    counts = pd_calc.value_counts()
    print(entropy(counts,base=2))
    pass


def alphaNumeric(l):
    str = string.digits + string.ascii_uppercase
    text_file = open("EX2C.txt","w")
    i = 1
    newList = []
    while (i <= l):
        i+=1
        str_1 = random.choices(str, k = l)
        rand_alpha = ''.join(str_1)
        text_file.write('{} {}'.format(rand_alpha,'\n'))
        newList+=rand_alpha

    text_file.close()



    arr = np.array(newList)
    plt.hist(arr, rwidth=0.9)
    plt.savefig(f'hist2c.png')
    plt.show()
    pprint(entropy(base=2))
    pass

'''
def alphaNum2(l, n):
    str = string.digits + string.ascii_uppercase
    text_file = open("EX2C1.txt", "w")
    i = 1
    j = 0
    alpha = ""
    newList = []
    while (j < n):
        j += 1
        while (i <= l):
            alpha += random.choice(str)
            if (i % 4 == 0): alpha += " "
        i += 1'''

def alphaNum2(l,n):
    str = string.digits + string.ascii_uppercase
    text_file = open("EX2C0.txt","w")
    i=1
    j=0
    alpha = ""
    #newList = []
    while(j<n):
       while(i <= l):
           alpha += random.choice(str)
           if(i % 4 == 0): alpha+= " "
           i+=1
       alpha+='\n'
       j += 1
       i = 1
    text_file.write(alpha)
    text_file.close()













#alphaNum2(24,3)
#alphabetSource(4,[3/10,2/10,4/10,1/10],'abcd')
newPasswords(4,8,3)
#alphaNumeric(24)
#alphaNum2(24,3)
