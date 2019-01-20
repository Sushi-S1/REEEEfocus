import os
import datetime
import psutil
import time
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('ultimaterefocus-firebase-adminsdk-l0bn5-323cf58637.json')
default_app = firebase_admin.initialize_app(cred)


#tasks = []
#websites = []
def up_time(task):
    for x in tasks:
        process_name = x
        for proc in psutil.process_iter():
            int(time.strftime("%H", time.localtime(proc.create_time())))

def website_block(websites):
    file = open("C:\Windows\System32\drivers\etc\hosts", "a")
    if len(websites) != 0:
        for x in websites:
            file.write(x)
    file.close()


def break_out():
    x = False
    return x


def check_tasks(tasks, limit):
    over_time = []
    for x in tasks:
        cnt = 0
        process_name = x
        for proc in psutil.process_iter():
            if int(time.strftime("%H", time.localtime(proc.create_time()))) >= limit:
                if cnt != 0:
                    if over_time[0] == process_name:
                        break
                else:
                    over_time.append(process_name)
                    cnt += 1
    return over_time

def get_time():
    time = str(datetime.datetime.now().time())
    return int(time[0:2])


def task_kill(task, log, local_web, time_limit, to_open): #pass in task name (maybe pass in a and log name, local_web is whether it a local program or web
    cnt = 0
    file = open(log, "a")
    time =  str(datetime.datetime.now().time())
    now = str(datetime.datetime.now()).split()
    file.write("\n{} \n\n".format(now[0]))
    over = check_tasks(task, time_limit)
    #for i in range(30): #just test code
    while(get_time()<24):
        if break_out():
            break
        elif len(over) == 0:
            break
        else:
            for x in over:
                temp = os.system("taskkill /f /im {}".format(x))
                if break_out():
                    break
                else:
                    if temp == 0:
                        cnt += 1
                        file.write("{} You have failed {} times for restricted programs\n".format(time[0:8], str(cnt)))#finish this code, writes time and # of fails
                        os.system("start {}".format(to_open))
                    if temp == 128:
                        pass
    file.close()
    exit()



task_kill(['MicrosoftEdge.exe', 'GitHubDesktop.exe'], "log.txt", "local", 1, "Taskmgr.exe") #works just need to not be terminated tested by for loop also need to grab these parameters from firebase

