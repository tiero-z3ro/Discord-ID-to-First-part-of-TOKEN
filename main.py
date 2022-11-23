# Modules importation
import os
import base64
from colorama import Fore, init

init()

banner = (Fore.MAGENTA + """
__________________ _______  _______  _______ 
\__   __/\__   __/(  ____ \(  ____ )(  ___  )
   ) (      ) (   | (    \/| (    )|| (   ) |
   | |      | |   | (__    | (____)|| |   | |
   | |      | |   |  __)   |     __)| |   | |
   | |      | |   | (      | (\ (   | |   | |
   | |   ___) (___| (____/\| ) \ \__| (___) |
   )_(   \_______/(_______/|/   \__/(_______)
                                             
""" + Fore.LIGHTCYAN_EX)
print(banner)
userid = input(" [INPUT] USER ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n [LOGS] TOKEN FIRST PART : {encodedStr}')
os.system('pause >nul')  # Pause command in Batch (press any key to exit the code)
