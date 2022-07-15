from socket import *
from time import sleep
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(3)
s.settimeout(3)
def fun():
    while True:
        print('等待链接：')
        try:
            c,addr=s.accept()
        except BlockingIOError as e:
            print(e)
            sleep(2)
        else:
            print('链接来自：',addr)
            data = c.recv(1024)