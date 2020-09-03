from time import *
import pyinputplus as pip
import os
import sys
import random

def HelloWorld ():
 sleep(2.5)
 print("")
 print("ADA SUPERCOMPUTER v.0.1")
 sleep(3.5)   
 print ("")
 print("Hello world!!! I haven't missed You for a second!! >:3")
 print ("")

def MyAssHurts ():
	print ("My ass hurts.")
	print ("")

def AdamIsAGenius ():
 print ("HURRAAAAAAAAAY!!!!! Adam, You are a genius!!!!")
 print ("")
 print("High five!!!!")
 print("")  
    
def InMyAssHole ():
 print ("In my asshole.")
 print ("")

def ThereShouldBeOnePersonHandelingThisShit():
 print("There should be only one slave doing this kind of work!!! Five slaves are too expensive!!!!")
 print ("")

def AngryBastard():
 print ("I'm hungry and I haven't eaten for the whole week!! I don't even know how I can be alive!! Oh, right!! This is a game!!! Right??! Now give me the motherblessing burrito!!! I'm starving, You piece of badabipidaboop!!!!")
 print ("")

HelloWorld()

MyAssHurts()

AdamIsAGenius()

InMyAssHole ()

ThereShouldBeOnePersonHandelingThisShit()

AngryBastard()




lst = ["Burrito", "Panini", "Nachos", "Olives", "Pizza", "Pasta", "Bullshit"]

print ("Today's menu is the one below this useless advert:")
print("")

print (lst [0], lst [2], lst [3], lst [6])
print("")
print("Have a nice motherblessing day!!! And stop annoying me for FOX SAKE!!!!!")
print("")
print("--     END OF MESSAGE     -- ")
print("")
sleep(1.5)
print(" -  Remember to keep all your mails, our super annoying supremacist highness in my asshole!!!  -")
print("")





# This shows how to use a lambda function


def fmult1(a, b):
    z = a * b
    return z

def fmult2(a, b):
    return a * b

def fmult3(a, b): return a * b

fmult4 = lambda a, b: a * b

sleep(3)
print(fmult1(3, 4))
print("")
print(fmult2(3, 4))
print("")
print(fmult3(3, 4))
print("")
print(fmult4(3, 4))

print("")

sleep(2.5)
print ("The next coming numbers is Your code verification of Your ID of the system.")
print("")
print("You shall not forget Your ID or Your system will crash.")
print ("")
sleep(1.5)
print("To anytime hide your fingerprints, type: 0 ")
print("")        
rspNm = pip.inputStr(prompt="Enter ID Name: ")
rspPssw = pip.inputPassword(prompt="Enter ID Password: ")

#cls = os.system
#ext = sys.exit

        
print("")
print ("ID is being verified.")
print("")
sleep (2.5)
print("25% Done.")
print("")
sleep (2.5)
print("50% Done.")
print("")
sleep (2.5)
print("75% Done.")
print("")
sleep (2.5)
print("100 % Done.")
sleep(1.5)
print("")



def ext ():
 sys.exit()

def cls ():
 os.system("cls")

#if rspNm or rspPssw == "0":
if rspNm  == "0":
 cls()
 ext()
    
if rspNm != "AMCCS" or rspPssw != "123": #rspPssw != "AdaSuperComputer":


 sleep (3.5)
 print ("Identification failed.")  
 print("") 
 sleep(1.5)
 print ("The system will autodetonate.")
 print("")
 sleep(1.5)
 print("9")
 sleep(1.5)
 print("")
 sleep(1.5)
 print("8")   
 print("")
 sleep(1.5) 
 print("7")
 print("")
 sleep(1.5) 
 print("6")    
 print("")   
 sleep(1.5) 
 print("5")
 print("")
 sleep(1.5) 
 print("4")
 print("")
 sleep(1.5) 
 print("3")
 print("")
 sleep(1.5) 
 print("2")
 print("")
 sleep(1.5) 
 print("1")
 print("")
 print("Autodestruction finalized.")
 print("")
 print("Shutdown system required.")
 print("")
#Os.system("clear") clears the terminal
 cls()
 
else:
  sleep (3.5)
  print ("Identification succeeded.")
  sleep(4)
  print("")
  for List in [[a*b for b in range(-101, 101)] for a in range(-101, 101)]: print(List) 
  print("")
  print ("The code has been opened.")
  print("")
  sleep(2.5)
  print("Check for the personal ID you are looking for.")
  print("")
  sleep(2.5)
  print("WIP part, searching ID will be working soon. :3")
  print("")


 #the list ID is from 3 to 5 numbers long

  def printPromptID():
    Prompt = pip.inputNum(prompt = "Enter ID: ")
    print("")
RspID = "12345"

printPromptID()
  
if len(RspID) < 1 or len(RspID) > 5:
    print("ID not Found!")
    print("")
    print("Try with another ID.")
    print("")
    printPromptID()
    
else: 
    print("Do You want to know the typed ID?")
    print("")
    print("If yes, type y. If no, type n.")
    RspAnswer1 = pip.inputStr(prompt = "Enter answer: ")

    RndmIP = ".".join(str(random.randint(0,255)for i in range(4)))
#RndmNm ==
#RndmSrnm ==
#RndmCntnt ==
#RndmCntry ==
#RndmAge ==
#RndmFd ==
if RspAnswer1 == "n":
 RndmKll = (str(random.uniform(0.0,100.0)))
 print("")
 print("The chosen ID has a " + RndmKll + "% of killing sucess.")
 print("")
 
if RspAnswer1 == "y":
 RndmAge = (str(random.randint(20,70)))
 print ("")
 print("The chosen ID is " + RndmAge + " years old.")
 print("")
 
 ##IP is like Generator and not as IP.
 print ("The chosen ID has " + RndmIP + " as IP.")
 print("")

 #Input gets yes shows: IP, name, surname, continent, country, age, and what food he/she just ate randomly
 #Terminal asks input if wanna kill ID
 #Terminal takes a string of yes or no
 #If yes the launches an ICBM and sends a report to Putin
 #If no then asks for next ID
 #When ID got killed then terminal asks if clear and quit program
 #Whenever input gets the chance to type then input can terminate and erase the whole programs as an emergency button