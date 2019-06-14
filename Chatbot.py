import datetime, calendar, time
from random import randrange
QuitList = ['quit', ' Quit', 'QUIT', 'Goodbye', 'goodbye', 'Exit', 'exit', 'EXIT']

print ('Credits')

print ('Hayden Ivins - Primary Coder')
print ('Andrew Ivins - Advisor')
print ('Lukas Rohwer - Primary Tester & Secondary Coder')
time.sleep(3)

def Welcome():
    print ('CHATBOT')
    print ('\n')
    print ("You can quit at any time by saying 'Exit or Goodbye or Quit'")
    time.sleep(1)
    print ('\n')
    print ('my name is Chatbot')
    print ('\n')
    time.sleep(1)
    print ('type help if you want help!')
    print ('\n')
    time.sleep(1)

def EnterName():
    name = input ('What is your name?')
    print (f'Hello {name}, nice to meet you. My name is Chatbot')
    print ('')
    return name

def recall_name(ans, name):
    if 'name' in ans:
        print(f'your name was {name}!')
    
def Help (ans):
    if 'help' == ans:
        print('things you can do:')
        print('names (generalized), money (money help), banana (banana help), and objects (generalized)')

def money_help(ans):
    if 'money help' == ans:
        print('money is the main currency and can be spent on stuff')
        print('\n')
        time.sleep
        print('things you can do:')
        print('money amount, can I have money, upgrade')

def minigame (ans, bananas):
    if 'minigame' == ans:
        from random import randrange
        options = (1,2,3,4,5,6,7,8,9,10)
        number = options[randrange(0,len(options))] 

        yes = False
        thing = True

        while (yes is False): 
            question = input('Would you like to play a game? [Y/N]')
            question.lower()

            if 'n' in question :
                print ('Oh, ok')
                time.sleep(3)
                thing = False
                yes = True

            if 'y' in question :
                print ('YaY!')
                print ('Ok, I will think of a number from 1-10 and you must guess it')
                yes = True

        while(thing is True):
            guess = int(input('Go on, guess'))

            if guess < number :
                print ('The number is higher')
        
            elif guess == number :
                print ('Correct!!!')
                time.sleep(3)
                print (f'you were awarded 1 bananas')
                bananas = bananas + 1
                thing = False

            elif guess > number :
                print ('The number is lower')
            
            else:
                print ('Please type an integer(a whole number)')
    return bananas
def bananaHelp(ans):
    if 'banana help' == ans:
        print('bananas are a secondary currency which give you a money bonus')
        print('\n')
        time.sleep(1)
        print('and you can eat them????? (don\'t do it)')
        print('\n')
        time.sleep(1)
        print('things you can do:')
        print('banana amount, buy bananas, eat banana') 

def Time (ans):
        if 'time' in ans:
            currentDT = datetime.datetime.now()
            print ('The current time is: ', currentDT.strftime)

def Food (ans):
    if 'food' in ans:
        print ('My favorite food is fish and chips')

def Exit (ans):
    if ans in QuitList:
        print ('Thank you for talking with me.....')
        time.sleep(1)
        exit()

def Pokemon (ans):
    if 'pokemon' in ans:
        print ("The new dynamax feature is awesome, don't you think?")

def Zak (ans):
    if 'zak' in ans:
        print ("Someone save Zak, he doesn't have much time left!")

def Lel (ans):
    if ans == 'lel':
        print ('lel')

def Zeke (ans):
    if 'zeke' in ans:
        print ('Zeke is dead!, or is he?')

def Aryan (ans):
    if 'aryan' in ans:
        print ("Aryan is dangerous! He's an assasin! You can pay him in Ks or Ms")

def Tobias (ans):
    if 'tobias' in ans:
        print ("Tobias is a robot, and he's smart!")
               
def Lukas (ans):
    if 'lukas' in ans:
        print ('Lukas likes pokemon and is a fortnite sweat')

def Ewen (ans):
    if 'ewen' in ans:
        print ("Did you know Ewen's name is pronounced E-wan?")
def Royyan (ans):
    if 'royyan' in ans:
        print ("Royyan likes buses and doctor who, that's all there is to say about him")

def Fortnite (ans):
    if 'fortnite' in ans:
        print ('We like Fortnite!')

def Minecraft (ans):
    if 'minecraft' in ans:
        print ('Minecraft has overtaken fortnite in google trends!')

def Manesh (ans):
    if 'manesh' in ans:
        print ("Manesh's name is prounced Maneeeesh! and he is dictator of the lel chat")

def LazarBeam (ans):
    if 'lazarbeam' in ans:
        print ('No one:')
        print ('\n')
        time.sleep(2)
        print ('Literally no one:')
        print ('\n')
        time.sleep(3)
        print ('LazarBeam:')
        print ('\n')
        time.sleep(3)
        print ('YEET!')
        time.sleep(2)

def Marcus (ans):
    if 'marcus' in ans:
        print ('Marcus is crazy. Literally.')

def Edward (ans):
    if 'edward' in ans:
        print ('Edward is an eggman')

def TophatElephant (ans):
    if 'tophatelephant' in ans:
        print ("No. Just no. We're not going down that rabbit hole again")
            #caused a political split

def Leuca (ans):
    if 'leuca' in ans:
        print('Squirrel! Leuca is watching YouTube again!')

def Goat (ans):
    if 'goat' in ans:
        print('Maaaaaa')

def Banana (ans):
    if 'banana' in ans:
        print('Banana!')

def Peely (ans):
    if 'peely' in ans:
        print('...')
        time.sleep(5)
        print("No, I don't want to talk about it")
        time.sleep(5)
            #I'm mourning his death in the trailer

def Rohan (ans):
    if 'rohan' in ans:
        print('Rohan argues/tries to convince people quite a lot, often over stupid/sily things')

def Vivian (ans):
    if 'vivian' in ans:
        print('Vivian is always late for class')

def Poop (ans):
    if 'poop' in ans:
        print('Poop is gross, why are you even mentioning it?')

def Waiman (ans):
    if 'waiman' in ans:
        print('Waiman is tall.')

def ethan(ans):
    if 'ethan' in ans:
        print('Ethan jokely steals stuff. A lot.')

def denzel(ans):
    if 'denzel' in ans:
        print('Denzel likes Lego, Bionicle, and Yu-Gi-Oh')

def hayden(ans):
    if 'hayden' in ans:
        print('Hayden says \'lel\' a lot')

def MoneyAmount (ans, money):
    options = ['money amount', 'bank', 'check money']
    for option in options:
        if option in ans:
            print(f'You have ${money:.2f}')
            break
                #tells you how much money you have

def GiveMoney (ans, money, bmultiplier):
    options = ['give me money', 'can i have money', 'ask for money', 'beg for money', 'give money' ]
    for option in options:
        if option in ans:
            print(f'You got ${money_gain * bmultiplier:.2f}!')
            money = money + int(money_gain) * bmultiplier
            break
    return money
        #main way to get money

def cheat_code (ans, money, price, money_gain):
    if 'cheat_code' in ans:
        ans2 = input('')
        if '$' == ans2:
            amount = input('')
            money += int(amount)
        elif '$!' == ans2:
            amount = input('')
            money_gain = money_gain * int(amount)
            price = price * int(amount)
        elif '$¡' == ans2:
            amount = input('')
            money_gain = money_gain * int(amount)
    return money, price, money_gain
        #cheats

def upgrade(ans, money, price, money_gain):
    if 'upgrade' in ans:
        ans2 = input(f'do you wish to upgrade you money gain? It will cost ${price:.2f}. If so say yes.')
        ans2 = ans2.lower()
        if ans2 == 'yes':
            if money >= price:
                print(f'Upgrade succesfull! You now get ${money_gain * 2:.2f} every time you ask!')
                money -= int(price)
                money_gain = money_gain * 2.25
                price = price * 2
            else:
                print('You don\'t have enough money!')
        else:
            print('That\'s okay, you don\'t have do if you don\'t want to, you might not even have enough money!')
    return money, price, money_gain
        #increases amount of money you get when you ask for money

def buy(ans, money, bananas, bprice, bmultiplier):
    if 'buy' in ans:
        if 'banana' in ans:
            ans2 =input(f'Do you wish to buy one banana for ${bprice:.2f}? (Yes or No)')
            ans2 = ans2.lower()
            if 'yes' in ans2:
                if money >= bprice:
                    money -= int(bprice)
                    bananas = bananas + 1
                    bprice = bprice * 1.5
                    bmultiplier = bmultiplier * 1.01
                    print('Purchase succesful')
                else:
                    print('You don\'t have enough money!')
            else:
                print('that\'s okay, you don\'t have to')
    return money, bananas, bprice, bmultiplier

def bananaAmount (ans, bananas):
    options = ['banana amount', 'banana bank', 'check bananas', 'bbank']
    for option in options:
        if option in ans:
            print(f'You have {bananas} bananas')
            break

def eat_banana (ans, bananas):
    if 'eat banana' in ans:
        ans2 = input('are you sure you want to do this? (Yes or No)')
        if 'yes' in ans2:
            ans3 = input('you shouldn\'t do this')
            if 'yes' in ans3:
                ans4 = input('you shouldn\'t do this, it will destroy a banana')
                if 'yes' in ans4:
                    ans5 = input('last chance, you sure you want to do this?')
                    if 'yes' in ans5:
                        print('fine, you win')
                        bananas -= int(bananas)
                        print('\n')
                        time.sleep(1)
                        print('you eat a banana')
                        print('\n')
                        time.sleep(1)
                        print('all the other bananas flee in terror')
                        print('\n')
                        time.sleep(1)
                        print('you now have 0 bananas')
                    else:
                        print('good, you shouldn\'t do this')
                else:
                    print('good, you shouldn\'t do this')
            else:
                print('good, you shouldn\'t do this')
        else:
            print('good, you shouldn\'t do this')
    return bananas

def random(ans):
    options = ['moo', 'neigh', 'baa']
    if 'random' in ans:
        print (options[randrange(0,len(options))])
            #basic random program
        
def sam(ans):
    if 'sam' in ans:
        print:('sam is in an orange')
        
def impersonate(ans):
    if 'impersonate' in ans:
        if 'hayden' in ans:
            options = ['lel', 'lel', 'k', 'YaY!']
            time.sleep(1)
            print('\n')
            print(options[randrange(0,len(options))])
        if 'lukas' in ans:
            options = ['anyone wanna play?', 'Lukario']
            time.sleep(1)
            print('\n')
            print(options[randrange(0,len(options))])

                #pretends to be people

Welcome()
name = EnterName()
Continue = True
money = 0
money_gain = 1
price = 5
bananas = 0
bprice = 10000
bmultiplier = 1
while Continue == True:
    print ('')
    ans = input ('what would you like to know/do?')
    ans = ans.lower()
    Exit (ans)
    recall_name(ans, name)
    Help (ans)
    money_help(ans)
    Time (ans)
    Food (ans)
    Pokemon (ans)
    bananas = minigame (ans, bananas)
    Zak (ans)
    Lel (ans)
    Zeke (ans)
    Aryan (ans)
    Tobias (ans)
    Lukas (ans)
    Ewen (ans)
    sam (ans)
    Royyan (ans)
    Fortnite (ans)
    Minecraft (ans)
    Manesh (ans)
    LazarBeam (ans)
    Marcus (ans)
    Edward (ans)
    TophatElephant (ans)
    Leuca (ans)
    Goat (ans)
    Banana (ans)
    Peely (ans)
    Rohan (ans)
    Vivian (ans)
    Waiman (ans)
    ethan(ans)
    denzel(ans)
    hayden(ans)
    MoneyAmount (ans, money)
    money = GiveMoney (ans, money, bmultiplier)
    (money, price, money_gain) = cheat_code (ans, money, price, money_gain)
    (money, price, money_gain) = upgrade(ans, money, price, money_gain)
    (money, bananas, bprice, bmultiplier) = buy(ans, money, bananas, bprice, bmultiplier)
    bananaAmount (ans, bananas)
    bananas = eat_banana (ans, bananas)
    Poop (ans)
    random (ans)
    impersonate (ans)
    time.sleep(1)



        #list of runnable functions
