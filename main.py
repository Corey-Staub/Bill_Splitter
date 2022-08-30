import random

def numberOfGuests():
    print('Enter the number of friends joining (including you):')
    guests = int(input())
    if guests <= 0:
        raise ValueError
    return guests

def initDict(guests):
    friend_dict = dict()
    print("Enter the name of every friend (including you), each on a new line:")
    for x in range(guests):
        friends = input()
        friend_dict[friends] = 0
    return friend_dict

def billTotal():
    print("Enter the total bill value:")
    bill = int(input())
    return bill

def dictToList(friend_dict):
    #since dictionaries act strange with random.choice, lets make a list
    nameList = []
    for key in friend_dict.keys():
        name = key
        nameList.append(name)
    return nameList

def luckyFeature(nameList, bill, guests, freind_dict):
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    luckPrompt = str(input())
    if luckPrompt == 'Yes':
        luckyName = random.choice(nameList)
        print(f'{luckyName} is the lucky one!')
        guests -= 1
        payments = round((bill / guests),2)
        for key in friend_dict:
            friend_dict[key] = payments
        friend_dict[luckyName] = 0
        print(friend_dict)
    else:
        print("No one is going to be lucky")
        print(guestPayments(bill, guests, friend_dict))


def guestPayments(bill, guests, friend_dict):
    payments = round((bill / guests),2)
    for key in friend_dict:
        friend_dict[key] = payments
    return(friend_dict)

try:
    guests = numberOfGuests()
    friend_dict = initDict(guests)
    bill = billTotal()
    nameList = dictToList(friend_dict)
    luckyFeature(nameList, bill,  guests, friend_dict)
except ValueError:
    print('No one is joining for the party')
