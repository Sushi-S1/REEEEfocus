import os
import datetime
import psutil
import time
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db


cred = credentials.Certificate('./ultimaterefocus-firebase-adminsdk-l0bn5-323cf58637.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'ReFocus').document(u'NNBOicPdhoPywjRNTHJ7')
doc = doc_ref.get()
passed = doc.to_dict()
apps = []
tasks = []
allowance = []
apps.append(passed["app"])
tasks.append(passed["name"])
allowance.append(passed["allowance"])
redir = passed["redir"]

def up_time(task):
    for x in tasks:
        process_name = x
        for proc in psutil.process_iter():
            int(time.strftime("%H", time.localtime(proc.create_time())))

def website_block(websites):
    file = open("C:\Windows\System32\drivers\etc\hosts", "a")
    if len(websites) != 0:
        for x in websites:
            file.write("0.0.0.0  ",x)
    file.close()


def break_out():
    x = False
    return x


def check_tasks(tasks, limit):
    over_time = []
    indexer = -1
    for x in tasks:
        indexer+=1
        cnt = 0
        process_name = x
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                if int(time.strftime("%H", time.localtime(proc.create_time()))) >= int(limit[indexer]):
                    if cnt != 0:
                        if over_time[0] == process_name:
                            break
                    else:
                        over_time.append(process_name)
                        cnt += 1
            else:
                pass
    return over_time

def get_time():
    time = str(datetime.datetime.now().time())
    return int(time[0:2])


def task_kill(task, log, time_limit, to_open):
    cnt = 0
    file = open(log, "a")
    time =  str(datetime.datetime.now().time())
    now = str(datetime.datetime.now()).split()
    file.write("\n{} \n\n".format(now[0]))
    over = check_tasks(task, time_limit)
    #for i in range(30): #just test code
    while(get_time()<24):
        over = check_tasks(task, time_limit)
        if break_out():
            break
        else:
            for x in over:
                temp = os.system("taskkill /f /im {}".format(x))
                if break_out():
                    break
                else:
                    if temp == 0:
                        cnt += 1
                        file.write("{} You have failed {} times for restricted programs\n".format(time[0:8], str(cnt)))
                        os.system("start {}".format(to_open))
                    if temp == 128:
                        pass
    file.close()
    exit()


website_block(apps)
task_kill(tasks, "log.txt", allowance, redir)
