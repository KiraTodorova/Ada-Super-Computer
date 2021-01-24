from time import *
import pyinputplus as pip
import os
import sys
import random
import names
from tqdm import tqdm
from tqdm.auto import tqdm
from gtts import gTTS

print("")
print("Do You want to enter a DEV command?")
print("")
print("If You need help, type it!")
print("")

#If You wanna change both "Nm" and "Pssw"; push Ctrl F, to Find them.
#Afterwards, change "Name" and "Password" to what You want.
#Push Ctrl F again, to find "rspNm" and "rspPssw" to what You want.
#If You find any issues; send me an email at:
#mauro.strandberg@gmail.com and I'll try to help C:


Nm = "Name"
Pssw = "Password"

Answ = pip.inputStr(prompt = "Enter y/help/n: ")
if Answ == "y":
 DEVCmnd = pip.inputStr(prompt = "Enter DEV Command: ") 
 
elif Answ == "help":

 print("")
 DEVCmnd = "r00t_get-info Nm && Pssw get-r00t"
 print(DEVCmnd + " is to get access info!")
 print("")
 DEVCmnd = pip.inputStr(prompt = "Enter DEV Command: ")
 
 if DEVCmnd == "r00t_get-info Nm && Pssw get-r00t": 
  print("Log in info: You have "  + Nm + " as ID Name" + Pssw + " as ID Password")
 
elif Answ == "n":

 print("")
 print("ATTENTION! BE AWARE OF HIGH VOLUME! LOWER VOLUME AT FIRST AND THEN RAISE AS PLEASED!")
 sleep(5)
 print("")

 fh = open("SystemName01.txt", "r")
 PrcntTxt = fh.read().replace("\n", " ")
 language = 'en'
 output = gTTS(text=PrcntTxt, lang=language, slow=False)
 output.save("SystemName01.mp3")
 fh.close()
 os.system("start SystemName01.mp3")
 sleep(4.1)
 os.system("taskkill /IM Music.UI.exe /F")


def SystemIntro ():
 sleep(2.5)
 print("")
 print("")
 print("ADA SUPERCOMPUTER v.0.1")
 print("")
 print("")
 sleep(1.2)
 print("This is a super secret system where Your safety and annonymity is two important factors in out business.")
 print("")
 print("Your work is to track pople we give to You and execute direct orfers.")
 print("")
 print("Our goal is to clean this world full of scumbags to make other's safe.")
 print("")
 print("You can't and will never be able to leave Your workplace.")
 print("")
 print("We have Your Bitcoin with Your bloodprint on it, that's Your signature of Your faith. Don't ever forget that. You owe us!")
 print("")
 print("LogIn info has come to You on a letter that is only per to per and destroys itself after reavealing itself to You.")
 print("")
 print("If You fail one single time, You had written Your death sentence on that moment.")
 print("")
 print("We will contact You later for You to execute our orders.")
 print("")
 print("If You choose to break or go against our orders, the execution as traitor will fall on Your family and lastly You.")
 print("")
 print("Welcome to Your new family!")
 print("")
 print("")
 sleep(1.5)
 print("--     END OF MESSAGE     -- ")
 print("")
 print("")

SystemIntro()

def LogInInfo ():
 sleep(1.5)
 print ("The next coming inputs is Your ID information to be able to log in the system.")
 print("")
 print("You shall not forget Your ID or Your system will crash!")
 print ("")
 sleep(1.5)
 print("To anytime hide Your fingerprints, type: 0 ")
 print("")        

LogInInfo()

rspNm = pip.inputStr(prompt="Enter ID Name: ")
rspPssw = pip.inputPassword(prompt="Enter ID Password: ")


def IDVerify ():        
 print("")
 print ("ID is being verified!")
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
 print("100% Done.")
 sleep(1.5)
 print("")

IDVerify()

def ext ():
 sys.exit()

def cls ():
 os.system("cls")
 


if rspNm  == "0":
  cls()
  ext()
    
if rspNm != "Name" or rspPssw != "Password":


  sleep (3.5)
  print ("Identification failed!")  
  print("") 
  sleep(1.5)
  print ("The system will autodetonate!")
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
  print("Autodestruction finalized!")
  print("")
  print("Shutdown system required!")
  print("")
  cls()
 
else:
  sleep (3.5)
  print ("Identification succeeded!")
  sleep(4)
  print("")
  for List in [[a*b for b in range(-101, 101)] for a in range(-101, 101)]: print(List) 
  print("")
  print ("The code has succesfully opened!")
  print("")
  sleep(2.5)
  print("Check for the personal ID Your are looking for!")
  print("")
  sleep(2.5)

Prompt = pip.inputStr(prompt= "Enter ID: ")
print("")

NumLst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:

 if len(Prompt) < 1 or len(Prompt) > 5 and not NumLst[0] and not NumLst[1] and not NumLst[2]\
  and not NumLst[3] and not NumLst[4] and not NumLst[5] and not NumLst[6] and not NumLst[7]\
  and not NumLst[8] and not NumLst[9]:
    print("ID not Found!")
    print("")
    print("Try with another ID!")
    print("")
    print(Prompt)
    
 else:
    print("Do You want to know the typed ID?")
    print("")
    sleep(1.5)
    print("If yes, type y. If no, type n.")
    RspAnswer1 = pip.inputStr(prompt = "Enter answer: ")

    RndmIP = ".".join(map(str,(random.randint(0,255)for i in range(4))))
    RndmFNm = names.get_full_name()
    RndmDrnkWtrH = random.randint(0,24)
    RndmDrnkWtrM = random.randint(0,60)
    RndmDrnkWtrS = random.randint(0,60)
    break

def AnswChk1 ():
 if RspAnswer1 == "n":
  RndmKll = (str(random.uniform(0.0,100.0)))
  print("")
  sleep(1)
  print("The chosen ID has a " + RndmKll + "% of killing sucess!")
  print("")
 
 elif RspAnswer1 == "y":
  RndmAge = (str(random.randint(20,70)))
  RndmKll = (str(random.uniform(0.0,100.0)))
  print ("")
  sleep(1)
  print("The chosen ID has " + RndmFNm + " as name.")
  sleep(1)
  print("The chosen ID is " + RndmAge + " years old.")
  print("")
  sleep(1)
  print ("The chosen ID has " + RndmIP + " as an IP.")
  print("")
  sleep(1)
  print("")
  sleep (1)
  print("The chosen ID drank water at " + str(RndmDrnkWtrH) + ":" + str(RndmDrnkWtrM) + ":" + str(RndmDrnkWtrS) + " last time.")
  print("")
  sleep(1)
  print("The chosen ID has a " + RndmKll + "% of killing sucess!")
  sleep(1)
  print("")

AnswChk1()



def AnswChk2 ():
 print("Do You want to kill the chosen ID?")
 print("")
 sleep(1.5)
 print("If yes, type y. If no, type n.")
 RspAnswer2 = pip.inputStr(prompt = "Enter answer: ")
 if RspAnswer2 == "n":
  print("The chosen ID will live for one more day!")
  print("")

 if RspAnswer2 == "y":
  print("")
  sleep(2)  
  print("An ICBM misile will be sent soon to the chosen ID!")
  print("")
  sleep(1)
  print("**Starting Sounds of Nuclear Alarm.**")
  print("")
  sleep(1)
  print("Toooooooot!!!")
  sleep(4)
  print("")
  print("Toooooooot!!!")
  sleep(4)
  print("")
  print("Toooooooot!!!")
  sleep(4)
  print("")
  print("Toooooooot!!!")
  sleep(3)
  print("")
  sleep(2)
  print("Engine of ICBM has started!")
  print("")
  sleep(2)
  print("Thrusts ignited at:")
  sleep(1)


def ReprtPrMnstr ():
 print("A message will be compiled before sending it to the Primary Minister of Tolyavgrad Vyboska!")
 
 print("Compiling message...")
 sleep(5)
 
 print("Message compiled!")
 print("")


AnswChk2()



fh = open("Percentage01.txt", "r")
PrcntTxt = fh.read().replace("\n", " ")
language = 'en'
output = gTTS(text=PrcntTxt, lang=language, slow=False)
output.save("PercentageT2S-01.mp3")
fh.close()
os.system("start PercentageT2S-01.mp3")

sleep(6)
print("")
sleep(118.05)
os.system("@echo off")
os.system("@taskkill /IM Music.UI.exe /F")
print("Waiting...")
print("")

for i, x in enumerate(list(range(1000001))):
   print(i, end='\r')


loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Backtracking to last working system trail...".format(k))
    loop.update(1)
loop.close()




loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Preparing to fix...".format(k))
    loop.update(1)
loop.close()





loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Fixing startup...".format(k))
    loop.update(1)
loop.close()



loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Stabilazing startup...".format(k))
    loop.update(1)
loop.close()



loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Stabilazing...".format(k))
    loop.update(1)
loop.close()


loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Thrusts Ignite Process startup...".format(k))
    loop.update(1)
loop.close()




loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Igniting thrusts...".format(k))
    loop.update(1)
loop.close()


loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Continuation of launch proceure...".format(k))
    loop.update(1)
loop.close()



print("ICBM launched!")
print("")



loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Sending...".format(k))
    loop.update(1)
loop.close()

ReprtPrMnstr()

print("Report sent!")
print("")
