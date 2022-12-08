#Mining Simlulator
#There is no save option every progress made will be reset made for one time use only

#imports
from ast import Return
import random 
import time

#starting variables
coins = 0
MF = 1
D_Pick = coins + MF
menu_op = ("")

#start/welcome
print("Hello this your first time mining isn't it! To mine your first ore collect your pickaxe!")

#actual mining
pick_pick = input(print("Would you like to pick the pickaxe up? Y/N"))
while pick_pick == 'N':
    pick_pic = input(print("Would you like to pick the pickaxe up? Y/N"))
else:
    print("You've picked up the steel pickaxe!\n +1 mining fortune")
mining = input(print("To mine press Y or to go back to the menu press N"))
while mining == 'Y':
    print(coins)
    coins = coins + 1
    miner = input(print("Would you like to mine agian? Y/N"))
    if miner == 'Y':
        print(mining)
    if miner == 'N':
        print(menu_op)
    if coins == 5:
        print("So you have unlocked a new mining method i call it 'pickonimbus' it where you have a chance of unlocking more coins by having a rare chance to get 5 coins instead of one!")
        mining_spec = input(print("To mine normally use Y or to use your pickonimbus ability press E"))
        if mining_spec == 'E':
         mintt = 60
         timer = mintt
         while (timer != 0 ):
               timer = timer-1
               time.sleep(1)
               time.sleep(6)
               print("Your 1 minute timer is up wait 1 minute to use it again")
               print(mining)
               if timer <= 60:
                  print(mining)
               elif timer >= 0:
                  print("Your pickonimbus ability timer is up to use it again press E")
                  print(mining_spec)
         seq = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
         random.sample (seq, 5)
         if seq == [7, 9, 14, 16, 20]:
                print ("You've got a lucky drop +5 coins!!!")
                coins = coins + 5
                print(coins)
    else:
        print("No rare ore drop yet, keep going!")

#main menu (shops, purse)
if mining != 'Y':
    menu_op = input(print("Would you like to go back to the menu or would you like to exit the game? Y/N"))
    if menu_op == 'Y':
        print("Welcome to the game menu here you can access the games options such as the shops, your purse or the mines again.")
        purse_total = input(print("Would you like to view your coins? Y/N"))
        if purse_total == 'Y':
            print(coins)
            print(mining)
        elif purse_total == 'N':
            print("Now why wouldn't you want to know the amount of coins you have well you need to know somehow to here you go!", coins)
        shop = input(print("Would you like to visit the shop you can get better tools! Y/N"))
        if shop == 'Y':
            purchase = input(print("Welcome to the shop we only have one item but that item will give you wonder to what you can get!\n the best item to show right now is a diamond pickaxe that give +2 mining fortune! Though everyhting comes at a cost and this cost is 100 coins would you like to buy?"))
            while purchase == 'Y':
                coins = coins - 100
                while coins < 0:
                    print("You dont have enough coins, please go mining and get more coins!")
                    print(mining)
                if coins > 0:
                    D_Pick = print("You have purchased the DIAMOND PICKAXE.\n with this you now get +2 mining fortune so that means double everything!!!")
                    if coins > 0:
                        new_MF = '2'
                        MF = True
                        if D_Pick == True:
                            print("Your new mining Fortune is 2")
                            print(mining)
                else:
                    print(mining)
#useless yet needed
else:
    print("You are great at mining aren't ya!")