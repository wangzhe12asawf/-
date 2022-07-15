from multiprocessing import Process,Queue
from time import sleep
q=Queue()
def a():
    for i in range(5):
        sleep(2)
        q.put(i)
def b():
    while True:
        try:
            print(q.get(timeout=3))
        except:
            return
q1=Process(target=a)
q2=Process(target=b)
q1.start()
q2.start()
q1.join()
q2.join()