from time import *
import pyinputplus as pip
import os
import sys
import random
import names
from faker import Faker
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
 print(DEVCmnd + " is to get access info.")
 print("")
 DEVCmnd = pip.inputStr(prompt = "Enter DEV Command: ")
 
 if DEVCmnd == "r00t_get-info Nm && Pssw get-r00t":
  DEVCmnd = pip.inputStr(prompt = "Enter DEV Command: ") 
  print("Log in info: You have "  + Nm + " as ID Name" + Pssw + " as ID Password")
 
elif Answ == "n":
 
 
#1 The program asks if user wants to give an dev command
#2 The user types y or no. If y see below if no, program starts 
#3.1 The program prints "to get help, type it". And user does so. A printed command shows up-
#3.2 The user types the actual dev command and UsrNme and Psswd shows up.





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
 sleep(2.5)
 os.system("taskkill /IM Music.UI.exe /F")


def SystemIntro ():
 sleep(2.5)
 print("")
 print("")
 print("ADA SUPERCOMPUTER v.0.1")
 print("")
 print("")
 sleep(1.2)
 print("This is a super secret system where your safety and annonymity is two important factors in out business.")
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
 print("If You choose to break or go against our orders, the execution as traitor will fall on your family and lastly You.")
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
 print("You shall not forget Your ID or Your system will crash.")
 print ("")
 sleep(1.5)
 print("To anytime hide your fingerprints, type: 0 ")
 print("")        

LogInInfo()

rspNm = pip.inputStr(prompt="Enter ID Name: ")
rspPssw = pip.inputPassword(prompt="Enter ID Password: ")

#cls = os.system
#ext = sys.exit


def IDVerify ():        
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
  print ("Identification succeeded!")
  sleep(4)
  print("")
  for List in [[a*b for b in range(-101, 101)] for a in range(-101, 101)]: print(List) 
  print("")
  print ("The code has succesfully opened!")
  print("")
  sleep(2.5)
  print("Check for the personal ID you are looking for!")
  print("")
  sleep(2.5)


 #the list ID is from 3 to 5 numbers long

Prompt = pip.inputStr(prompt= "Enter ID: ")
print("")

NumLst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:

 if len(Prompt) < 1 or len(Prompt) > 5 and not NumLst[0] and not NumLst[1] and not NumLst[2]\
  and not NumLst[3] and not NumLst[4] and not NumLst[5] and not NumLst[6] and not NumLst[7]\
  and not NumLst[8] and not NumLst[9]:
    print("ID not Found!")
    print("")
    print("Try with another ID.")
    print("")
    print(Prompt)
    break
    
 else:
    print("Do You want to know the typed ID?")
    print("")
    sleep(1.5)
    print("If yes, type y. If no, type n.")
    RspAnswer1 = pip.inputStr(prompt = "Enter answer: ")

    RndmIP = ".".join(map(str,(random.randint(0,255)for i in range(4))))
    RndmFNm = names.get_full_name()
    fake = Faker()
    RndmAdrss = fake.address()
    RndmDrnkWtrH = random.randint(0,24)
    RndmDrnkWtrM = random.randint(0,60)
    RndmDrnkWtrS = random.randint(0,60)


def AnswChk1 ():
 if RspAnswer1 == "n":
  RndmKll = (str(random.uniform(0.0,100.0)))
  print("")
  sleep(1)
  print("The chosen ID has a " + RndmKll + "% of killing sucess.")
  print("")
 
 if RspAnswer1 == "y":
  RndmAge = (str(random.randint(20,70)))
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
  print("The chosen ID lives at " + RndmAdrss + " right now.")
  print("")
  sleep (1)
  print("The chosen ID drank water at " + str(RndmDrnkWtrH) + ":" + str(RndmDrnkWtrM) + ":" + str(RndmDrnkWtrS) + " last time.")
  print("")
  sleep(1)

PromptChck()

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
  print("AN ICBM misile will be sent soon to the chosen ID!")
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
  '''print("1%")
  sleep(1)
  print("2%")
  sleep(1)
  print("3%")
  sleep(1)
  print("4%")
  sleep(1)
  print("5%")
  sleep(1)
  print("6%")
  sleep(1)
  print("7%")
  sleep(1)
  print("8%")
  sleep(1)
  print("9%")
  sleep(1)
  print("10%")
  sleep(1)
  print("11%")
  sleep(1)
  print("12%")
  sleep(1)
  print("13%")
  sleep(1)
  print("14%")
  sleep(1)
  print("15%")
  sleep(1)
  print("16%")
  sleep(1)
  print("17%")
  sleep(1)
  print("18%")
  sleep(1)
  print("19%")
  sleep(1)
  print("20%")
  sleep(1)
  print("21%")
  sleep(1)
  print("22%")
  sleep(1)
  print("23%")
  sleep(1)
  print("24%")
  sleep(1)
  print("25%")
  sleep(1)
  print("26%")
  sleep(1)
  print("27%")
  sleep(1)
  print("28%")
  sleep(1)
  print("29%")
  sleep(1)
  print("30%")
  sleep(1)
  print("31%")
  sleep(1)
  print("32%")
  sleep(1)
  print("33%")
  sleep(1)
  print("34%")
  sleep(1)
  print("35%")
  sleep(1)
  print("36%")
  sleep(1)
  print("37%")
  sleep(1)
  print("38%")
  sleep(1)
  print("39%")
  sleep(1)
  print("40%")
  sleep(1)
  print("41%")
  sleep(1)
  print("42%")
  sleep(1)
  print("43%")
  sleep(1)
  print("44%")
  sleep(1)
  print("45%")
  sleep(1)
  print("46%")
  sleep(1)
  print("47%")
  sleep(1)
  print("48%")
  sleep(1)
  print("49%")
  sleep(1)
  print("50%")
  sleep(1)
  print("51%")
  sleep(1)
  print("52%")
  sleep(1)
  print("53%")
  sleep(1)
  print("54%")
  sleep(1)
  print("55%")
  sleep(1)
  print("56%")
  sleep(1)
  print("57%")
  sleep(1)
  print("58%")
  sleep(1)
  print("59%")
  sleep(1)
  print("60%")
  sleep(1)
  print("61%")
  sleep(1)
  print("62%")
  sleep(1)
  print("63%")
  sleep(1)
  print("64%")
  sleep(1)
  print("65%")
  sleep(1)
  print("66%")
  sleep(1)
  print("67%")
  sleep(1)
  print("68%")
  sleep(1)
  print("69%")
  sleep(1)
  print("70%")
  sleep(1)
  print("71%")
  sleep(1)
  print("72%")
  sleep(1)
  print("73%")
  sleep(1)
  print("74%")
  sleep(1)
  print("75%")
  sleep(1)
  print("76%")
  sleep(1)
  print("77%")
  sleep(1)
  print("78%")
  sleep(1)
  print("79%")
  sleep(1)
  print("80%")
  sleep(1)
  print("81%")
  sleep(1)
  print("82%")
  sleep(1)
  print("83%")
  sleep(1)
  print("84%")
  sleep(1)
  print("85%")
  sleep(1)
  print("86%")
  sleep(1)
  print("87%")
  sleep(1)
  print("88%")
  sleep(1)
  print("89%")
  sleep(1)
  print("90%")
  sleep(1)
  print("91%")
  sleep(1)
  print("92%")
  sleep(1)
  print("93%")
  sleep(1)
  print("94%")
  sleep(1)
  print("95%")
  sleep(1)
  print("96%")
  sleep(1)
  print("97%")
  sleep(1)
  print("98%")
  sleep(1)
  print("99%")'''


def ReprtPutn ():
 print("A message will be compiled before sending it to the Primary Minister of Russia...")
 
 print("Compiling message...")
 sleep(5)
 
 print("Message compiled")
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
sleep(121.2)
os.system("@echo off")
os.system("@taskkill /IM Music.UI.exe /F")
#print("CLOSE WINDOW WHERE THE MUSIC WILL BE PLAYED ON!!!!")
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



print("ICBM launched")
print("")



loop = tqdm(total = 100000, position = 0, leave = False)
for k in range(100000):
    loop.set_description("Sending...".format(k))
    loop.update(1)
loop.close()

ReprtPutn()

print("Report sent!")
print("")

 #Input gets yes shows: IP, name, surname, adress, age, and when he/she drank water last time randomly
 #Terminal asks input if wanna kill ID
 #Terminal takes a string of yes or no
 #If yes the launches an ICBM and sends a report to Putin
 #If no then asks for next ID
 #When ID got killed then terminal asks if clear and quit program
 #Whenever input gets the chance to type then input can terminate and erase the whole programs as an emergency button
