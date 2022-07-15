from  socket import *
import sys,os
ADDR = ('127.0.0.1',8888)

def do_send(s,name):
    while True:
        try:
            text = input('请发言：')
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip(' ') == 'quit':
            msg='Q '+name
            s.sendto(msg.encode(),ADDR)
            sys.exit('退出系统')
        msg ='C %s %s'%(name,text)
        s.sendto(msg.encode(),ADDR)

def do_recv(s):
    while True:
        try:
            data,addr = s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+'\n发言',end='')

def main():
    s= socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input('请输入姓名：')
        msg = 'L '+name
        s.sendto(msg.encode(),ADDR)
        data,addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print('已进入聊天室')
            break
        else:
            print(data.decode())
    pid = os.fork()
    if pid < 0:
        print('error')
    elif pid == 0:
        do_send(s,name)
    else:
        do_recv(s)

main()
