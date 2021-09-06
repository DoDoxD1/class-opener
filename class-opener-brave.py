import datetime
import subprocess
from typing import IO

def ds_lab():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32152_1/outline'])
def dbms_lab():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32263_1/outline'])
def java_lab():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32374_1/outline'])
def ds():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32472_1/outline'])
def coa():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32528_1/outline'])
def dbms():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32585_1/outline'])
def java():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32641_1/outline'])
def life():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_33033_1/outline'])
def aptitude():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32920_1/outline'])
def numerical():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32755_1/outline'])
def numerical_b():
    subprocess.call(['C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe','https://cuchd.blackboard.com/ultra/courses/_32756_1/outline'])

def monday(hour, minutes):
    if hour == 9:
        if minutes>38:
            numerical_b()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>28:
            life()
        else:
            numerical_b()
    elif hour == 11:
        if minutes>18:
            ds()
        else:
            life()
    elif hour == 12:
        if minutes>8:
            print("Njoy lunch")
        else:
            ds()
    elif hour == 12:
        if minutes>58:
            ds_lab()
        else:
            print("Njoy lunch")
    elif hour == 13:
        if minutes>48:
            ds_lab()
        else:
            ds_lab()
    else:
        print("No class now njoy")
def tuesday(hour, minutes):
    if hour == 9:
        if minutes>38:
            dbms()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>27:
            numerical()
        else:
            dbms()
    elif hour == 11:
        if minutes>18:
            java()
        else:
            numerical()
    elif hour == 12:
        if minutes>8:
            print("Njoy lunch")
        else:
            java()
    else:
        print("No class now njoy")
def wednesday(hour, minutes):
    if hour == 9:
        if minutes>38:
            numerical()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>27:
            ds()
        else:
            numerical()
    elif hour == 11:
        if minutes>18:
            dbms()
        else:
            ds()
    elif hour == 12:
        if minutes>8:
            print("Njoy lunch")
        else:
            dbms()
    elif hour == 12:
        if minutes>58:
            aptitude()
        else:
            print("Njoy lunch")
    elif hour == 13:
        if minutes>48:
            aptitude()
        else:
            aptitude()
    else:
        print("No class now njoy")
def thursday(hour, minutes):
    if hour == 9:
        if minutes>38:
            coa()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>28:
            java_lab()
        else:
            coa()
    elif hour == 11:
        if minutes>18:
            java_lab()
        else:
            java_lab()
    else:
        print("No class now njoy")
def friday(hour, minutes):
    if hour == 9:
        if minutes>38:
            dbms()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>28:
            ds_lab()
        else:
            dbms()
    elif hour == 11:
        if minutes>18:
            ds_lab()
        else:
            ds_lab()
    elif hour == 11:
        if minutes>58:
            java()
        else:
            ds_lab()
    else:
        print("No class now njoy")

def saturday(hour, minutes):
    if hour == 9:
        if minutes>38:
            ds()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>28:
            numerical()
        else:
            ds()
    elif hour == 11:
        if minutes>18:
            coa()
        else:
            numerical()
    elif hour == 12:
        if minutes>8:
            print("Njoy lunch")
        else:
            coa()
    elif hour == 12:
        if minutes>58:
            dbms_lab()
        else:
            print("Njoy lunch")
    elif hour == 13:
        if minutes>48:
            dbms_lab()
        else:
            dbms_lab()
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
    elif day == 'saturday':
        friday(hour, minutes)
    else:
        print("Njoy no class!")


if __name__ == "__main__":
    day = datetime.datetime.today().strftime('%A').lower()
    checkday(day)


