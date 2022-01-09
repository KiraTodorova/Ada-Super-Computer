#If you want to change Your log in credentials to whatever You choose in the code, change Nm = "Name" and Pssw = "Password" C:

import pyinputplus as pip
import os
import sys
import random
import names
import threading

from time import sleep
from tqdm import tqdm
from tqdm.auto import tqdm
from gtts import gTTS

AdaSCNm= """
 _______  ______   _______        _______  _______        ______   _______  _______  _______ 
(  ___  )(  __  \ (  ___  )      (  ____ \(  ____ \      (  __  \ (  ____ \(       )(  ___  )
| (   ) || (  \  )| (   ) |      | (    \/| (    \/      | (  \  )| (    \/| () () || (   ) |
| (___) || |   ) || (___) |      | (_____ | |            | |   ) || (__    | || || || |   | |
|  ___  || |   | ||  ___  |      (_____  )| |            | |   | ||  __)   | |(_)| || |   | |
| (   ) || |   ) || (   ) |            ) || |            | |   ) || (      | |   | || |   | |
| )   ( || (__/  )| )   ( |      /\____) || (____/\      | (__/  )| (____/\| )   ( || (___) |
|/     \|(______/ |/     \|      \_______)(_______/      (______/ (_______/|/     \|(_______)
                                                                                             
"""

StopThdBl = False

InfoStr = """
 ADA SUPERCOMPUTER v. 0.1
 
 This is a super secret system where Your safety and annonymity is two important factors in our business.
 
 Your work is to track people we give to You and execute direct orders.
 
 Our goal is to clean this world full of scumbags to make others safe.
 
 You can't and will never be able to leave Your new role.
 
 We have Your Bitcoin with Your bloodprint on it, that's Your signature of Your faith. Don't ever forget that. You owe us!
 
 LogIn info has come to You in a letter that is only peer to peer and destroys itself after reavealing itself to You.
 
 If You fail one single time, You had written Your death sentence on that moment.
 
 We will contact You later for You to execute our direct orders.
 
 If You choose to break or go against our orders, the execution as a traitor will fall on Your family and lastly on You.
 
 Welcome to Your new family!
 
 --     END OF MESSAGE     -- 
 
 """
 
#Change this username at Your liking 
Nm = "Name"

#Change this password at Your liking
Pssw = "Password"
 
def DevCmndAsk():
 sleep(3)
 loop = tqdm(total = 10000, position = 0, leave = False)
 for k in range(10000):
  loop.set_description("Starting Up...".format(k))
  loop.update(1)
 loop.close()
 print(AdaSCNm)
 sleep(3)
 print("")
 print("Do You want to enter a DEV command?")
 print("")
 sleep(1)
 print("If You need help, type it!")
 print("")
 sleep(2)


def AnswCheckH():
  DEVCmnd = "r00t_get-info Nm && Pssw get-r00t"
  print("")
  print(DEVCmnd + " is to get access info!")
  print("")
  DevCmnd()



def AnswCheckN():
 sleep(2)
 print("")

 loop = tqdm(total = 10000, position = 0, leave = False)
 for k in range(10000):
  loop.set_description("Loading ADA Super Computer Operative System...".format(k))
  loop.update(1)
 loop.close()
 
 sleep(3)   
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
 sleep(4.5)

def DevCmnd():
 while True:
  ArlCmd = ["r00t_get-info Nm && Pssw get-r00t"]
  DEVCmnd = pip.inputStr(prompt = "Enter DEV Command: ")
  if DEVCmnd == ArlCmd [0]:
   print("Log in info: You have "  + Nm + " as ID Name. " + Pssw + " as ID Password")
   print("")
   break
  
  elif DEVCmnd != ArlCmd [0]:
   AnswDEVCmnd = pip.inputStr(prompt = "Enter y/help/n: ")
   
DevCmndAsk()

def LogInCredentials():
 while True:
  ArLsAns = ["y","help","n"]
  Answ2 = pip.inputStr(prompt = "Enter y/help/n: ")
  if Answ2 == ArLsAns [0]:
   DevCmnd() 
   break
  
  elif Answ2 ==  ArLsAns [1]:
   AnswCheckH()
   break
    
  elif Answ2 == ArLsAns [2]:
   AnswCheckN()
   break
   
  elif Answ2 != ArLsAns [0] or Answ2 != ArLsAns [1] or Answ2 != ArLsAns [2]:
   Answ = pip.inputStr(prompt = "Enter y/help/n: ")
   
   if Answ == ArLsAns [0]:
    ArlCmd = ["r00t_get-info Nm && Pssw get-r00t"]
    print(ArlCmd [0])
    DevCmnd()
    break
    
   elif Answ == ArLsAns [1]:
    AnswCheckH()
    break
    
   elif Answ == ArLsAns [2]:
    AnswCheckN()
    break
    

LogInCredentials()

def SystemTypeWriteInfo1(InfoStr):
 while True:
   if StopThdBl == True:
    break
 
   for char in InfoStr:
    sys.stdout.write(char) 
    sys.stdout.flush()
    sleep(0.05)
  
    if char!= "\n":
     sleep(0.05)
   
    else:
     sleep(0.05)
   break

def FileStarterVOInfo():
 os.system("start .\\Assets\\5_ADA_VO_ImportantBusiness01.wav")
 sleep(14)
 os.system("start .\\Assets\\6_ADA_VO_Wokload01.wav")
 sleep(8)
 os.system("start .\\Assets\\7_ADA_VO_OtherSafety01.wav")
 sleep(9)
 os.system("start .\\Assets\\8_ADA_VO_NewRole01.wav")
 sleep(9)
 os.system("start .\\Assets\\9_ADA_VO_YouOweUs01.wav")
 sleep(14)
 os.system("start .\\Assets\\10_ADA_VO_Letter01.wav")
 sleep(16)
 os.system("start .\\Assets\\11_ADA_VO_DeathSentence01.wav")
 sleep(10)
 os.system("start .\\Assets\\12_ADA_VO_DirectOrders01.wav")
 sleep(10)
 os.system("start .\\Assets\\13_ADA_VO_Warning01.wav")
 sleep(13)
 os.system("start .\\Assets\\14_ADA_VO_WelcomeNewFamily01.wav")
 sleep(7)

def SystemInfoVO(): 
 while True:
  if StopThdBl == True:
   break
  FileStarterVOInfo()
  sleep(5)
  break

Thd1 = threading.Thread(target = SystemInfoVO)
Thd2 = threading.Thread(target = SystemTypeWriteInfo1, args = [InfoStr])

Thd1.start()
Thd2.start()
StopThdBl = True

Thd1.join()
Thd2.join()

def LogInInfo():
 sleep(1.5)
 print("")
 print ("The next coming inputs is Your ID information to be able to log in the system.")
 print("")
 sleep(3)
 print("You shall not forget Your ID or Your system will crash!")
 print ("")
 sleep(4)
 print("To anytime hide Your fingerprints, type: 0 ")
 print("") 
 sleep(3) 
 os.system("start .\\Assets\\1_ADA_VO_PlsEnterTheCredentials01.wav")
 sleep(7)
 os.system("@taskkill /IM Music.UI.exe /F")
 print("")
 
LogInInfo()

rspNm = pip.inputStr(prompt="Enter ID Name: ")
sleep(1)
rspPssw = pip.inputPassword(prompt="Enter ID Password: ")

def IDVerify():        
 sleep(3)
 
 loop = tqdm(total = 100000, position = 0, leave = False)
 for k in range(100000):
  loop.set_description("ID is being verified...".format(k))
  loop.update(1)
 loop.close()
 
 loop = tqdm(total = 5000, position = 0, leave = False)
 for k in range(5000):
  loop.set_description("Checking all instances for malware...".format(k))
  loop.update(1)
 loop.close()
  
  
 
 loop = tqdm(total = 10000, position = 0, leave = False)
 for k in range(10000):
  loop.set_description("Checking ID's references...".format(k))
  loop.update(1)
 loop.close()
 
 loop = tqdm(total = 50000, position = 0, leave = False)
 for k in range(50000):
  loop.set_description("Checking ID's records...".format(k))
  loop.update(1)
 loop.close()
 
 sleep(5.5)
 print("")
 
def LogInChck():

 if rspNm  == "0":
  cls()
  ext()
    
 elif rspNm != Nm or rspPssw != Pssw:
  sleep (3.5)
  print ("Identification failed!")  
  print("") 
  sleep(1.5)
  os.system("start .\\Assets\\4_ADA_VO_BootFailed01.wav")
  sleep(6)
  os.system("@taskkill /IM Music.UI.exe /F")
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
  os.system("start .\\Assets\\BombExplosion01.mp3") 
  sleep(7)
  os.system("@taskkill /IM Music.UI.exe /F")
  cls()
  ext()
 
 else:
  sleep (3.5)
  print ("Identification succeeded!")
  sleep(4)
  print("")
  os.system("start .\\Assets\\3_ADA_VO_BootSuccesful01.wav")
  sleep(8)
  os.system("start .\\Assets\\2_ADA_VO_Welcome007_01.wav")
  sleep(7)
  os.system("@taskkill /IM Music.UI.exe /F")
  print("")
  
  loop = tqdm(total = 100000, position = 0, leave = False)
  for k in range(100000):
   loop.set_description("Loading avaliable IDs:".format(k))
   loop.update(1)
  loop.close()
  print("")
  sleep(1)
  
  for List in [[a*b for b in range(-101, 101)] for a in range(-101, 101)]: print(List) 
  sleep(2)
  print("")
  print ("The code has succesfully opened and a list of IDs are succesfully listed!")
  print("")
  sleep(2.5)
  print("Please, select an ID from the list to get its information!")
  print("")
  sleep(2.5)

def ext():
 sys.exit()

def cls():
 os.system("cls")

IDVerify()

LogInChck()

def SecIDChck():
 while True:
  try:
   
   Prompt = input("Enter ID: ")
   IntNumberInput = int(Prompt)
   
   if len(Prompt)  < 1 or len(Prompt) > 5 or any(not i.isdigit() for i in Prompt):
    raise ValueError()
    
  except ValueError:
    print("No ID found in the system! Try again!")
 
  else:
   print("")
   print("Do You want to know the typed ID?")
   print("")
   sleep(1.5)
   print("If yes, type y. If no, type n.")
   break  

SecIDChck()

def AnswChk1():
 print("")
 RspAnswer1 = pip.inputStr(prompt = "Enter answer: ")
 RndmIP = ".".join(map(str,(random.randint(0,255)for i in range(4))))
 RndmFNm = names.get_full_name()
 RndmDrnkWtrH = random.randint(0,24)
 RndmDrnkWtrM = random.randint(0,60)
 RndmDrnkWtrS = random.randint(0,60)
 
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
  print("")
  sleep(1)
  print("The chosen ID is " + RndmAge + " years old.")
  print("")
  sleep(1)
  print ("The chosen ID has " + RndmIP + " as an IP.")
  print("")
  sleep(2)
  print("The chosen ID drank water at " + str(RndmDrnkWtrH) + ":" + str(RndmDrnkWtrM) + ":" + str(RndmDrnkWtrS) + " last time.")
  print("")
  sleep(1)
  print("The chosen ID has a " + RndmKll + "% of killing sucess!")
  sleep(1)
  print("")
  

AnswChk1()

def CinematicDramaticMusic():
 StopThdB2 = False
 while True:
  if StopThdB2 == True:
   break
  sleep(215) 
  os.system("start .\\Assets\\DramaticOrchestraLoopable01.wav")
  sleep(358)
  break
 
def AnswChk2():
 StopThdB2 = False
 while True:
  if StopThdB2 == True:
   break
  
  sleep(4)
  print("Do You want to kill the chosen ID?")
  print("")
  sleep(1.5)
  print("If yes, type y. If no, type n.")
  print("")
  RspAnswer2 = pip.inputStr(prompt = "Enter answer: ")
  
  if RspAnswer2 == "y":
   print("")
   sleep(2)  
   print("An ICBM misile will be sent soon to the chosen ID!")
   print("")
   sleep(1)
   os.system("start .\\Assets\\FactoryAlarm01.wav") 
   sleep(31)
   print("Engine of ICBM has started!")
   print("")
   sleep(2)
   print("Thrusts ignited at:")
   sleep(1)
   
   fh = open("Percentage01.txt", "r")
   PrcntTxt = fh.read().replace("\n", " ")
   language = 'en'
   output = gTTS(text=PrcntTxt, lang=language, slow=False)
   output.save("PercentageT2S-01.mp3")
   fh.close()
   os.system("start PercentageT2S-01.mp3")
   print("")
   sleep(155)
   print("Waiting...")
   print("")

   loop = tqdm(total = 100000, position = 0, leave = False)
   for k in range(100000):
    loop.set_description("Backtracking to last working system trail...".format(k))
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
   sleep(2)
   os.system("start .\\Assets\\ICBMEngineSound01.wav") 
   sleep(7)
   os.system("@taskkill /IM Music.UI.exe /F")
   
   print("")
   print("ICBM launched!")
   print("")
   sleep(6)
   os.system("start .\\Assets\\BombExplosion01.mp3") 
   sleep(6)
   
  elif RspAnswer2 == "n":
   sleep(3)
   print("")
   print("Please, choose another ID")
   print("")
   SecIDChck()
   AnswChk1()
   AnswChk2()
    
  elif RspAnswer2 != "y" or RspAnswer2 != "n":
   print("Wrong answer. Try Again!")
   print("")
   sleep(1.5)
  break

Thd3 = threading.Thread(target = CinematicDramaticMusic)
Thd4 = threading.Thread(target = AnswChk2)

Thd3.start()
Thd4.start()
StopThdB2 = True

Thd3.join()
Thd4.join()

def ReprtPrMnstr():
 print("")
 print("A message will be compiled before sending it to the Primary Minister of Tolyavgrad Vyboska!")
 print("")
 print("Compiling message...")
 sleep(5)
 print("")
 os.system("start .\\Assets\\MachineStartup01.wav") 
 sleep(67)
 os.system("@taskkill /IM Music.UI.exe /F")
 print("")
 print("Message compiled!")
 print("")

def Report():
 print("Preparing to send report...")
 os.system("start .\\Assets\\MachineFXPrintEDITED01.wav") 
 sleep(5)
 print("")
 os.system("@taskkill /IM Music.UI.exe /F")
 sleep(4)
 loop = tqdm(total = 100000, position = 0, leave = False)
 for k in range(100000):
    loop.set_description("Sending...".format(k))
    loop.update(1)
 loop.close()

def ReportSub():
 sleep(1)
 print("")
 print("Report sent!")
 sleep(3)
 print("")
 
ReprtPrMnstr()
Report()
ReportSub()