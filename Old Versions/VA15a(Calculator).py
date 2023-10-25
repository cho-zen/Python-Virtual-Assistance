from subprocess import REALTIME_PRIORITY_CLASS
from sys import implementation
import pyttsx3
import speech_recognition as sr
from random import random, randrange
import datetime
import requests
import os
import sys

from VA1 import takecommand

"""
Starting  
Engine Voice Command Mode Code 
Code for speaking the systen voice
"""
engine = pyttsx3.init('sapi5') #Initializing Engine Voice Command Mode Sys
voices = engine.getProperty('voices')  #Calling Sysytem Voices (Basically 2 Voice are there id[0] is male and id[1] is for female)
def mainfun(i, r=180):
    engine.setProperty('voice', voices[i].id)
    engine.setProperty('rate', r )
mainfun(0)

"""           End           """
#.......................................................................................................#

"""
Starting Meassage class 
class runs various functions to check indivisually 
wheather the user input is match with the given list or not 

"""
class Message():

    # Initiating Message for calling the virtual assistant 
    # Return Message like : Alaways for you Sir!
    def initiateMessage(self):
        return ["wake up",'wake up jarvis','hello','start','ok jarvis','are you there'] 

    #
    def timingMessage(self):
        return ["whatsapp", "whats up", "how you doing", "how are you"]

    # Wish Message : take input as good morning/noon/even etc...
    # Return Correct the user if he/she greet the worng input + tells about the day
    # Return the greetings and tells about day _(timing) _(weather) _(tempture)
    def wishMessage(self):
        return ["good morning", "good noon" , "good evening", "good night", 'good afternoon']

    #Time Message : Show the current time and 
    # Also asking for the schedule updatation 
    def time(self):
        return ['time','time right now', "what's the time", "time right yet", 'show time','show me time']
    
    # Change Voice : Change voice Randomly as per random index form 0 to 4
    #           
    def changevoice(self):
        return ['switch voice','change voice','change the voice','switch the voice',]
    
    # Change Assistant voice to a perticular voice 
    # After taking the name of the voice form the user
    def changeVoiceto(self):
        return ["change voice to", "Switch voice to","chnage the voice to ","switch the voice to", "change assistant voice to",'switch voice','change voice','change the voice','switch the voice']


    def weatherReport(self):
        return ["weather outside", "what's the weather","show weather","weather"]

    # def scheduleshow(self):
    #     return ['show my schedule',"my schedule","show my work details"]

    def showtodo(self):
        return ['show to do','show my to do list','what about my to do list','show my work list','show work list']

    def updatetodo(self):
        return ["update to do", "add work","add a work","open to do","update my work list", "update working list"]

    def exit(self):
        return ["exit", "see you", "good bye", "bye", "sleep", "back to sleep"]

    def calculator(self):
        return ["calculator mode", 'calculate this', 'add this', 'calculate', 'calculation']


class Speak():
    def initiateMessage(self):
        msg_initiate =  ["I'm Always here for you.......Sir!","Always for you...............Sir!","Welcome back......Sir!","I'm Up","Great to see you..........Sir!"]
        return msg_initiate[randrange(0,4)]

    def wishMessage(self,i,fun = "",fun2 = "", fun3=""):
        time = (datetime.datetime.now().hour)
        call = Speak()
        if time >= 0 and time < 12:
            if i == "good morning":
                return f"Greetings......with a very Good Morning \n{fun}{fun3}"
            else:
                return (f"Greeting....but not so, {i} \n{fun}{fun2}\n{fun3}")
        elif time>=12 and time <16:
            if i == "good noon": 
                return f"Greetings......with a Good Noon \n{fun}{fun3}"
            else:
                return (f"Greeting....but not so, {i} \n{fun}{fun2}\n{fun3}")
        elif time >=16 and time <=20:
            if i == "good evening":
                return f"Greetings......with a Good Evening \n{fun}{fun3}"
            else:
                return (f"Greeting....but not so, {i} \n{fun}{fun2}\n{fun3}")
        elif time >=20 and time<=24:
            if i == "good night":
                return f"Greetings......with a Good Night \n{fun}{fun3}"
            else:
                return (f"Greeting....but not so, {i} \n{fun}{fun2}\n{fun3}")

    def timingInitMessage(self):
        time = (datetime.datetime.now().hour)
        return f"I'm doing great, Sir!\nI wish you too\nTell me how can i assist you"
        

    def wishmeright(self):
        time = (datetime.datetime.now().hour)
        if time >= 0 and time < 12:
            return f'''With a wonderful morning Sir! '''
        elif time>=12 and time <16:
            return f'''With a bright sunny day Sir! '''
        elif time >=16 and time <=20:
            return f'''With a beautiful evening Sir! '''
        elif time >=20 and time<=24:
            return f'''With a sweet night Sir! '''

    def weatherForcasting(self):
        url = f'https://api.openweathermap.org/data/2.5/weather?q=Indore&appid=3f1c1428ac19890d026eb590ae26b157'
        data = requests.get(url).json()
        description = data['weather'][0]['description']
        temp = round(data['main']['temp']-273)
        feelslike = round(data['main']['feels_like']-273)
        clouds = data['clouds']['all']
        if clouds<=30:
            msg = "So don't forget to apply sun's cream.."
        else:
            msg = ""
        return f'''Today's weather outside will be, {description}.\nWith the tempeture of {temp} degree celsius, but feels like {feelslike}.. \nClouds appear in the sky, with the percentage of {clouds} \n {msg}'''

    def weather(self):
        API_KEY = os.environ.get('API_KEY')
        url = f'https://api.openweathermap.org/data/2.5/weather?q=Indore&appid=3f1c1428ac19890d026eb590ae26b157'
        data = requests.get(url).json()
        description = data['weather'][0]['description']
        temp = data['main']['temp']-273
        return f'''Today's weather outside will be, {description}....\nWith the tempeture of, {round(temp)}....degree celsius'''


    def time(self):
        time = datetime.datetime.now().hour
        if time<=12:
            return f'''Time right now is {datetime.datetime.now().strftime("%H, %M")} AM \nHope your are up to your work'''
        else:
            return f'''Time right now is {datetime.datetime.now().strftime("%H, %M")} PM \nHope your are up to your work'''
    
    def changevoice(self):
        i = randrange(0,len(voices))
        if i == 0:
            speak = "Changing voice to DAVID's voice"
        elif i == 1:
            speak = "Changing voice to RAVI's Voice"
        elif i == 2:
            speak = "Changing voice to MARK's Voice"
        elif i == 3:
            speak = "Changing voice to HEERA's Voice"
        elif i == 4:
            speak = "Changing voice to ZIRA's Voice"  
        mainfun(i)  
        return speak
    
    def changevoiceto(self, input):
        if "david" in input:
            speak = "Changing voice to DAVID's voice"
            return speak, mainfun(0)
        elif "ravi" in input:
            speak = "Changing voice to RAVI's voice"
            return speak, mainfun(1)
        elif "mark" in input:
            speak = "Changing voice to MARK's voice"
            return speak, mainfun(2)
        elif "heera" in input or 'hira' in input:
            speak = "Changing voice to HEERA's voice"
            return speak, mainfun(3)
        elif "zira" in input:
            speak = "Changing voice to ZIRA's voice"
            return speak, mainfun(4)
        else:
            i = randrange(0,len(voices))
            if i == 0:
                speak = "Changing voice to DAVID's voice"
            elif i == 1:
                speak = "Changing voice to RAVI's Voice"
            elif i == 2:
                speak = "Changing voice to MARK's Voice"
            elif i == 3:
                speak = "Changing voice to HEERA's Voice"
            elif i == 4:
                speak = "Changing voice to ZIRA's Voice"  
            mainfun(i)  
            return speak
    
    # def scheduleshow(self):
    #     with open("Schedule.txt","r") as f:
    #         text = f.readline()
    #         for lastline in f:
    #             pass
    #     return f"Your last Schedule on....{lastline}"


    def showtodo(self):
        with open("Todo.txt","r") as f:
            text = f.readline()
            for lastline in f:
                pass
        return f"On last you are working on.... \n{lastline}\n"

    def updatetodo(self, str):
        zone = datetime.datetime.now().hour
        time = datetime.datetime.now().strftime("%H %M")
        day = datetime.datetime.now().strftime("%A")
        with open("Todo.txt", 'a') as a:
            if zone<=12:
                a.write(f"{str}, at.....{day} {time} AM\n")
                return f"{str}, at.....{day} {time} AM"
            else:
                a.write(f"{str}, at.....{day} {time} PM\n")
                return f"{str}, at.....{day} {time} PM"
    def calculator(self):
        pass

    def exit(self):
        message = ["See you soon sir", "Have a nice day sir", "See you...Sir!\nYou can call ema ny time "]
        return message[randrange(0,3)], sys.exit()
 
    


def takecommand(n=1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold=900
        print("Listening...")
        r.pause_threshold = n
        audio = r.listen(source)    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User Said : {query}\n")
    except Exception as e:
        query = ""
    return query


if __name__ == "__main__":
    while True:
        userinput = takecommand() 
        if len(userinput)>0:
            # print(userinput) #Line to show what user's say in the terminal
            inputlist = userinput.lower()
            # print(inputlist) #Extra Code to see How it's work
            message = Message()
            speak = Speak()
            newcode = list()
            for i in message.initiateMessage():
                if i in inputlist:
                    newcode.append(i) #Append in the new list to match the words
                    # print(newcode) #Extra code to see what words program is match with my voice
                    if len(newcode)>=1:
                        say1 = speak.initiateMessage()
                        print(say1)
                        engine.say(say1)
                        engine.runAndWait()
                        break
            for i in message.wishMessage():
                if i in inputlist:
                    say = speak.wishMessage(i,fun2 = speak.wishmeright(), fun3 = speak.weather())
                    print(say)
                    engine.say(say)
                    engine.runAndWait()
                    break
            for i in message.timingMessage():
                if i in inputlist:
                    print(speak.timingInitMessage())
                    engine.say(speak.timingInitMessage())
                    engine.runAndWait()        
            for i in message.time():
                if i in inputlist:
                    print(speak.time())
                    engine.say(speak.time())
                    engine.runAndWait() 
                    break 
            # for i in message.changevoice():
            #     if i in inputlist:
            #         voice_to = speak.changevoice()
            #         print(voice_to)
            #         engine.say(voice_to)
            #         engine.runAndWait() 
            #         break     
            for i in message.weatherReport():
                if i in inputlist:
                    print(speak.weatherForcasting())
                    engine.say(speak.weatherForcasting())
                    engine.runAndWait()
                    break
            for i in message.changeVoiceto():
                if i in inputlist:
                    saycvt = speak.changevoiceto(input = inputlist)
                    print(saycvt)
                    engine.say(saycvt)
                    engine.runAndWait()      
            for i in message.showtodo():
                if i in inputlist:
                    print(speak.showtodo())
                    engine.say(speak.showtodo())
                    engine.runAndWait()
                    break  
            for i in message.updatetodo():
                if i in inputlist:
                    print("What Would you like to add in the to do list......Sir!")
                    engine.say("What Would you like to add in the to do list......Sir!")
                    engine.runAndWait()
                    loop = "_yes_"
                    while loop == "_yes_":
                            work = takecommand()
                            engine.say(f"You like to add : {work}") 
                            engine.runAndWait()
                            loop2 = "_yes_"
                            while loop2 == "_yes_":
                                yandn = takecommand()
                                if "no" in yandn:
                                    print("Then tell me again what you would like to add ? \nOr you can simply say Cancel")
                                    engine.say("Then tell me again what you would like to add ? \nOr you can simply say Cancel")
                                    engine.runAndWait()
                                    loop2 = "_no_"
                                elif "yes" in yandn:
                                    todo = speak.updatetodo(work)
                                    print(f"Updating : {todo}")
                                    engine.say(f"Updating : {todo}")
                                    engine.runAndWait()
                                    loop2 = "_no_"
                                    loop = "_no_"
                                elif "cancel" in yandn:
                                    print("Cancelling the to do list updatation ")
                                    engine.say("Cancelling the to do list updatation")
                                    engine.runAndWait()
                                    loop2 = "_no_"
                                    loop = "_no_"
                                else:
                                    print("Sorry i can't understand what you saying \nSay again would you like to update or not")
                                    engine.say("Sorry i can't understand what you saying\n Say again would you like to update or not")
                                    engine.runAndWait()               
                    else:
                        break

            for i in message.calculator():
                if i in inputlist:
                    print("Intiating Calculator mode")
                    engine.say("Intiating Calculator mode")
                    engine.runAndWait()


            for i in message.exit():
                if i in inputlist:
                    msg = speak.exit()
                    print(msg)
                    engine.say(msg)
                    engine.runAndWait()


                        
# if takecommand()=="male voice":
#     male_voice()
#     engine.say("Switch to Male Voice")
#     engine.runAndWait()

# if takecommand() == "female voice":
#     female_voice()
#     engine.say("Switch to Female Voice")
#     engine.runAndWait()