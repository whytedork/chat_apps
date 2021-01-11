import socket
import os
import threading

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

ip = input("Enter Your IP:")
port = 12345
rec_ip=input('Receiver IP is => ')
rec_port=int(input('Receiver Port No =>   '))

os.system("tput setaf 2")
print("\t\t\t\t Chat App")
os.system("tput setaf 6")
print("\t\t\t\t---------------------")

s.bind((ip , port))

def rec():
    while True:
        x = s.recvfrom(1024)
        if x[0].decode()=='exit' or x[0].decode()=='bye':
            os.system("tput setaf 5")
            print('\t\t\t\t\t Bye-Bye\n\n\n')
            s.sendto('exit'.encode(), (rec_ip, rec_port))
            os.system("tput setaf 7")
            os._exit(1)
        clientip = x[1][0]
        data = x[0].decode()
        os.system("tput setaf 3")
        print("\n\t\t\t\t\t\t\t " + clientip + ":" + data)
        os.system("tput setaf 6")


def send():
    while True:
        s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        os.system("tput setaf 6")
        print()
        x = input("You: ")
        os.system("tput setaf 6")
        s.sendto(x.encode(),(rec_ip,rec_port))
        os.system("tput setaf 6")
        if(x=="bye" or x=="exit"):
        	os._exit(1)


x1 = threading.Thread( target = rec )
x2 = threading.Thread( target = send)

x1.start()
x2.start()
