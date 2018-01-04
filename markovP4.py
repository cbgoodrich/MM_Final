#Charlie Goodrich
#01/04/18
#markovP4.py - the fourth problem for project 5

from random import randint

forkliftList = ["working"]*27

j = 0

inShop = 0
while j < 10:
    i = 0
    for forklift in forkliftList:
        randNum = randint(0,132)
        if forkliftList[i] == "broken":
            james = 0
        else:
            if randNum <= 1:
                forkliftList[i] = "broken"
                inShop += 1
        i += 1
    j += 1