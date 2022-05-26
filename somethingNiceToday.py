import random
import time


# update these variables as ideas are added
spendMoney = -2
goOutside = 13
saveMoney = 3
stayInside = 8

cheapInsideOptions = 6
cheapOutsideOptions = 11
notCheapInsideOptions = 11
notCheapOutsideOption = 16      #also total count of activities

# classes with t/f flags?
def options(num):
    if num == 1:
        print("Buy something cute from a local store")
    elif num == 2:
        print("Buy a fancy coffee/tea drink; savor it")
    elif num == 3:
        print("Plant some seeds to start")
    elif num == 4:
        print("Half hour of uninterrupted reading and tea time")
    elif num == 5:
        print("Do the whole facemask/skin care routine")
    elif num == 6:
        print("Start or plan a new knitting project")
    elif num == 7:
        print("Take a spa shower, use fancy lotions and fancy hair stuff")
    elif num == 8:
        print("Do some yoga/stretching")
    elif num == 9:
        print("Go for a walk and look at plants")
    elif num == 10:
        print("Play in your garden with your plants")
    elif num == 11:
        print("Pull weeds")
    elif num == 12:
        print("Go to the beach and see if anything interesting has washed up")
    elif num == 0:
        print("Go to a plant or garden store")
    elif num == -1:
        print("Go out to eat for dinner")
    elif num == -2:
        print("Go to a thrift store")
    elif num == 13:
        print("Pick flowers and make a bouquet")
    return True


def randomSelector(weather, cheap):
    # Use a breakpoint in the code line below to debug your script.
    if weather and not cheap:
        # the weather is good and I don't care about spending money
        return random.randint(spendMoney,goOutside)
    elif weather and cheap:
        # the weather is good but I don't want to spend money
        return random.randint(saveMoney,goOutside)
    elif cheap and not weather:
        # I don't want to spend money and the weather sucks
        return random.randint(saveMoney,stayInside)
    elif not cheap and not weather:
        # I don't care about spending money and the weather sucks
        return random.randint(spendMoney,stayInside)

def isOK(weather, cheap):
    if weather and cheap:
        if len(activities) == cheapOutsideOptions:
            return False
    elif weather and not cheap:
        if len(activities) == notCheapOutsideOption:
            return False
    elif cheap and not weather:
        if len(activities) == cheapInsideOptions:
            return False
    elif not cheap and not weather:
        if len(activities) == notCheapInsideOptions:
            return False
    return True

if __name__ == '__main__':
    weather = False
    print("Is it nice outside? t/f")
    if input() == 't':
        weather = True

    cheap = False
    print("Do you want to avoid spending money? t/f")
    if input() == 't':
        cheap = True


    activities = []
    while True:
        val = randomSelector(weather, cheap)
        if val not in activities:
            activities.append(val)
            options(activities[-1])
            print("If this doesn't work, press Enter, else write 'quit'")
            if input() != '':
                exit()
            if not isOK(weather, cheap):
                print("You've run out of ideas. Take a deep breath and let's look again.")
                activities.clear()
                time.sleep(3)