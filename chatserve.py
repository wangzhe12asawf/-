from socket import *
import os,sys
ADDR = ('0.0.0.0',8888)
user = {}
def  do_login(s,name,addr):
    if name in user or '管理者' in name:
        s.sendto('姓名已存在'.encode(),addr)
        return
    s.sendto(b'OK', addr)
    msg='\n欢迎%s进入聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name]=addr

def do_chat(s,name,text):
    msg="\n%s %s"%(name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_quit(s,name):
    msg='\n%s退出了聊天室'%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b"EXIT",user[i])
    del user[name]

def do_request(s):
    while True:
        data,addr=s.recvfrom(1024)
        tmp=data.decode().split(' ')
        if tmp[0]=="L":
            do_login(s,tmp[1],addr)
        elif tmp[0]=="C":
            text=' '.join(tmp[2:])
            do_chat(s,tmp[1],text)
        elif tmp[0]=="Q":
            do_quit(s,tmp[1])

def main():
    s= socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid<0:
        print('error')
    elif pid==0:
        while True:
            msg = input('管理员发言：')
            msg = 'C管理员 '+msg
            s.sendto(msg.encode(),ADDR)
    else:
        do_request(s)
main()



















































































