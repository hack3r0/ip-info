import socket
import os
#colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW	= '\033[33m'
BLUE	= '\033[34m'
MAGENTA = '\033[35m'
CYAN	= '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")

print("""\033[35m
███╗   ███╗██╗   ██╗    ██╗██████╗
████╗ ████║╚██╗ ██╔╝    ██║██╔══██╗
██╔████╔██║ ╚████╔╝     ██║██████╔╝
██║╚██╔╝██║  ╚██╔╝      ██║██╔═══╝
██║ ╚═╝ ██║   ██║       ██║██║
╚═╝     ╚═╝   ╚═╝       ╚═╝╚═╝
 """)
def getip():
		hostname = socket.gethostname()
		IPAddr = socket.gethostbyname(hostname)
		print(hostname)
		print(IPAddr)

print("""
 
\033[33m[1] \033[32mMy Ip
 
\033[33m[2] \033[32mAbout
 
\033[33m[3] \033[32mExit
""")
D = input("select number : ")
if D == "1":
  getip()
elif D == "2":
  os.system("clear")
  print(f"""{MAGENTA}
         █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗
        ██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝
        ███████║██████╔╝██║   ██║██║   ██║   ██║
        ██╔══██║██╔══██╗██║   ██║██║   ██║   ██║
        ██║  ██║██████╔╝╚██████╔╝╚██████╔╝   ██║
        ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝    ╚═╝
  """)
  print(f"""{GREEN}
  
                My Name : Black Hacker 😈
    
    Telegram Channel : https://t.me/Anonymous_Hacking_12
    """)
elif D == "3":
      os.system("exit")
      print("done")
else:
  print("Error Number")