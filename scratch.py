import string

str = string.digits + string.ascii_letters + string.punctuation
list = [1,2,3,4,5]

for i in range(0,len(list)):
    print(i)


print(len(str))