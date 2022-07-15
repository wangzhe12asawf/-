from multiprocessing import Process
import os
from time import sleep
def fun01():
    sleep(3)
    print(os.getppid(),'--',os.getpid(),'吃饭')

def fun02():
    sleep(4)
    print(os.getppid(),'--',os.getpid(),'睡觉')

def fun03():
    sleep(2)
    print(os.getppid(),'--',os.getpid(),'打豆豆')

job = []
for th in [fun01,fun02,fun03]:
    p = Process(target=th)
    job.append(p)
    p.start()
for th in job:

    p.join()