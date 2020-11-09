import datetime
import subprocess

def bio():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9905_1/outline'])
def comt():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9908_1/outline'])
def comp():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9906_1/outline'])
def maths():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9810_1/outline'])
def cad():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9809_1/outline'])
def det():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9902_1/outline'])
def dep():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9811_1/outline'])
def ai():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9808_1/outline'])
def life():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9909_1/outline'])
def pspt():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9807_1/outline'])
def pspp():
    subprocess.call(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://cuchd.blackboard.com/ultra/courses/_9806_1/outline'])

def monday(hour, minutes):
    if hour == 9:
        if minutes>45:
            det()
        else:
            print('Class not started yet')
    if hour == 10:
        if minutes>45:
            dep()
        else:
            det()
    if hour == 11:
        if minutes>45:
            dep()
        else:
            dep()
    if hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            dep()
    if hour == 13:
        if minutes>30:
            maths()
        else:
            print("Njoy lunch")
    if hour == 14:
        if minutes>30:
            bio()
        else:
            maths()
    else:
        print("No class now njoy")
def tuesday(hour, minutes):
    if hour == 9:
        if minutes>45:
            life()
        else:
            print('Class not started yet')
    if hour == 10:
        if minutes>45:
            maths()
        else:
            life()
    if hour == 11:
        if minutes>45:
            comt()
        else:
            maths()
    if hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            comt()
    if hour == 13:
        if minutes>30:
            bio()
        else:
            print("Njoy lunch")
    else:
        print("No class now njoy")
def wednesday(hour, minutes):
    if hour == 9:
        if minutes>45:
            ai()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>45:
            ai()
        else:
            ai()
    elif hour == 11:
        if minutes>45:
            cad()
        else:
            ai()
    elif hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            cad()
    if hour == 13:
        if minutes>30:
            det()
        else:
            print("Njoy lunch")
    if hour == 14:
        if minutes>30:
            maths()
        else:
            det()
    else:
        print("No class now njoy")
def thursday(hour, minutes):
    if hour == 9:
        if minutes>45:
            maths()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>45:
            pspt()
        else:
            maths()
    elif hour == 11:
        if minutes>45:
            pspp()
        else:
            pspt()
    elif hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            pspp()
    elif hour == 13:
        if minutes>30:
            comt()  
        else:
            print("Njoy lunch")
    else:
        print("No class now njoy")
def friday(hour, minutes):
    if hour == 9:
        if minutes>45:
            cad()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>45:
            cad()
        else:
            cad()
    elif hour == 11:
        if minutes>45:
            bio()
        else:
            cad()
    elif hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            bio()
    elif hour == 13:
        if minutes>30:
            pspt()
        else:
            print("Njoy lunch")
    elif hour == 14:
        if minutes>30:
            pspp()
        else:
            pspt()
    else:
        print("No class now njoy")
def saturday(hour, minutes):
    if hour == 9:
        if minutes>45:
            det()
        else:
            print('Class not started yet')
    elif hour == 10:
        if minutes>45:
            comp()
        else:
            det()
    elif hour == 11:
        if minutes>45:
            comp()
        else:
            comp()
    elif hour == 12:
        if minutes>45:
            print("Njoy lunch")
        else:
            comp()
    elif hour == 13:
        if minutes>30:
            pspp()
        else:
            print("Njoy lunch")
    elif hour == 14:
        if minutes>30:
            pspp()
        else:
            pspp()
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
        saturday(hour, minutes)
    else:
        print("Njoy no class!")


if __name__ == "__main__":
    day = datetime.datetime.today().strftime('%A').lower()
    checkday(day)


