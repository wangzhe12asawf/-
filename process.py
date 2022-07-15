from multiprocessing import Process
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()
    def fun01(self):
        print('进程1')
    def fun02(self):
        print('进程2')
    def run(self):
        self.fun01()
        self.fun02()
if __name__=='__main__':
    p=MyProcess(2)
    p.start()
    p.join()
