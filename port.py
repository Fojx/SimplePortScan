# -*- coding: utf-8 -*-
import socket
import sys
from colorama import Fore, Style

print (Fore.BLUE + """

██╗██╗  ██╗███╗   ██╗██╗  ██╗██╗      █████╗ ████████╗██╗  ██╗███████╗
██║╚██╗██╔╝████╗  ██║██║  ██║██║     ██╔══██╗╚══██╔══╝██║  ██║██╔════╝
██║ ╚███╔╝ ██╔██╗ ██║███████║██║     ███████║   ██║   ███████║███████╗
██║ ██╔██╗ ██║╚██╗██║██╔══██║██║     ██╔══██║   ██║   ██╔══██║╚════██║
██║██╔╝ ██╗██║ ╚████║██║  ██║███████╗██║  ██║   ██║   ██║  ██║███████║
╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝

By : Fojx

Menu

1) Fast Mode !
2) Slow Mode !
3) Exit !
""")
print(Style.RESET_ALL)


def scan(time):
    host = raw_input("Enter IP : ")
    number = int(raw_input("Range of Ports :"))
    port = 1
    try:
        while (port <= number):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(time)
            result = sock.connect_ex((host, port))
            if result == 0:
                print "=" * 30
                print (Fore.GREEN + "Port Is Open : %i") %port
            else:
                print "PORT : ",port," is close"
                sys.stdout.write("\033[F")
            port = port + 1
    except:
            print " - Program Closed !"
def settings():
    try:
        while True:
            epilogh = int(raw_input("Choose : "))
            if (epilogh == 1):
                fast = 0.01
                scan(fast)
                break
            elif (epilogh == 2):
                slow = 1
                scan(slow)
                break
            elif (epilogh == 3):
                print "Program Close"
                sys.exit()
            else:
                print "Give 1 or 2 ! "
    except:
        print "Program Close"
        
settings()