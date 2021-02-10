import datetime
import subprocess
from typing import IO

def compWork():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_15591_1/outline'])
def comt():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_16923_1/outline'])
def comp():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_16776_1/outline'])
def maths():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_17254_1/outline'])
def IOT():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_15901_1/outline'])
def BEEEt():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_16210_1/outline'])
def BEEEp():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_16147_1/outline'])
def life():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_17913_1/outline'])
def cppt():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_15736_1/outline'])
def cppp():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_15441_1/outline'])
def phyt():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_17522_1/outline'])
def phyp():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_17429_1/outline'])

def monday(hour, minutes):
    if hour == 9:
        if minutes>45:
            comt()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>45:
            phyp()
        else:
            comt()
    elif hour == 11:
        if minutes>45:
            phyp()
        else:
            phyp()
    elif hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            phyp()
    elif hour == 13:
        if minutes>30:
            maths()
        else:
            print("Njoy lunch")
    elif hour == 14:
        if minutes>30:
            comp()
        else:
            maths()
    elif hour == 15:
        if minutes>30:
            comp()
        else:
            comp()
    else:
        print("No class now njoy")
def tuesday(hour, minutes):
    if hour == 9:
        if minutes>45:
            maths()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>45:
            compWork()
        else:
            maths()
    elif hour == 11:
        if minutes>45:
            compWork()
        else:
            compWork()
    elif hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            compWork()
    elif hour == 13:
        if minutes>30:
            BEEEt()
        else:
            print("Njoy lunch")
    elif hour == 14:
        if minutes>30:
            maths()
        else:
            BEEEt()
    elif hour == 15:
        if minutes>30:
            life()
        else:
            maths()
    else:
        print("No class now njoy")
def wednesday(hour, minutes):
    if hour == 9:
        if minutes>45:
            cppp()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>45:
            cppp()
        else:
            cppp()
    elif hour == 11:
        if minutes>45:
            maths()
        else:
            cppp()
    elif hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            maths()
    elif hour == 13:
        if minutes>30:
            IOT()
        else:
            print("Njoy lunch")
    elif hour == 14:
        if minutes>30:
            IOT()
        else:
            IOT()
    elif hour == 15:
        if minutes>30:
            phyt()
        else:
            IOT()
    else:
        print("No class now njoy")
def thursday(hour, minutes):
    if hour == 9:
        if minutes>45:
            phyt()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>45:
            BEEEt()
        else:
            phyt()
    elif hour == 11:
        if minutes>45:
            print("Njoy lunch")
        else:
            BEEEt()
    elif hour == 12:
        if minutes>45:
            comt()
        else:
            print("Njoy lunch")
    elif hour == 13:
        if minutes>30:
            maths()  
        else:
            comt()
    elif hour == 14:
        if minutes>30:
            cppp()  
        else:
            maths()
    elif hour == 15:
        if minutes>30:
            cppp()  
        else:
            cppp()
    else:
        print("No class now njoy")
def friday(hour, minutes):
    if hour == 9:
        if minutes>45:
            BEEEt()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>45:
            cppt()
        else:
            BEEEt()
    elif hour == 11:
        if minutes>45:
            cppt()
        else:
            cppt()
    elif hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            cppt()
    elif hour == 13:
        if minutes>30:
            phyt()
        else:
            print("Njoy lunch")
    elif hour == 14:
        if minutes>30:
            BEEEp()
        else:
            phyt()
    elif hour == 15:
        if minutes>30:
            BEEEp()  
        else:
            BEEEp()
    else:
        print("No class now njoy")

def checkday(day):
    hour = int(datetime.datetime.now().hour)
    minutes = int(datetime.datetime.now().minute)
    
    if day == 'monday':
        monday(hour, minutes)
    elif day == 'tuesday':
        tuesday(hour, minutes)
    elif day == 'wednesday':
        wednesday(hour, minutes)
    elif day == 'thursday':
        thursday(hour, minutes)
    elif day == 'friday':
        friday(hour, minutes)
    else:
        print("Njoy no class!")


if __name__ == "__main__":
    day = datetime.datetime.today().strftime('%A').lower()
    checkday(day)


