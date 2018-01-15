import random
numbe = [random.randrange(1,100) for i in range(10)] # generates 10 random numbers between 1 and 99 in puts them into a list
user_input = int(input('I\'m thinking of a list of ten numbers, find out if its in the list'))
numbe.sort()

def random_sort(numbe, user_input):
    if user_input in numbe:
        return(True)
    else:
        return(False)

if random_sort(numbe, user_input) == True:
    print("%d is in the list range" % user_input)
if random_sort(numbe, user_input) == False:
    print("%d is NOT in the list range" % user_input)

