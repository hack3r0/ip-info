import socket
import os
#colors
RED		 = '\033[31m'
GREEN	 = '\033[32m'
YELLOW	= '\033[33m'
BLUE		= '\033[34m'
MAGENTA = '\033[35m'
CYAN		= '\033[36m'
WHITE	 = '\033[37m'
RESET	 = '\033[39m'
os.system("clear")

def getip():
		hostname = socket.gethostname()
		IPAddr = socket.gethostbyname(hostname)
		print(hostname)
		print(IPAddr)
def update():
  os.system("git clone https://github.com/hack3r0/ip-info;cd ip-info;python ip.py")

print("""\033[35m
███╗   ███╗██╗   ██╗    ██╗██████╗
████╗ ████║╚██╗ ██╔╝    ██║██╔══██╗
██╔████╔██║ ╚████╔╝     ██║██████╔╝
██║╚██╔╝██║  ╚██╔╝      ██║██╔═══╝
██║ ╚═╝ ██║   ██║       ██║██║
╚═╝     ╚═╝   ╚═╝       ╚═╝╚═╝
 """)
 
print("""
 
\033[33m[1] \033[32mMy Ip
 
\033[33m[2] \033[32mUpdate Tool
 
\033[33m[3] \033[32mExit
""")
D = input("select number : ")
if D == "1":
  getip()
  if D == "2":
    update()
    if D == "3":
      os.system("exit")