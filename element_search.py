##Write a function that takes an ordered list of numbers
##(a list where the elements are in order from smallest to largest) and another number.
##The function decides whether or not the given number
##is inside the list and returns (then prints) an appropriate boolean.
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

##import random
##lst = [i for i in range(random.randrange(0,1000))]
##n = int(raw_input("Enter a number to see if it's in the list range: "))
##def elementsearch(lst,n):
##	if n in lst:
##		return True
##	else:
##		return False
##if elementsearch(lst,n) == True:
##	print "%d is in the list range" % n
##if elementsearch(lst,n) == False:
##print "%d is NOT in the list range" % n
