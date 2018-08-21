#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import hashlib,os
os.system('clear')
print("\u001b[32m")
print("            ___ __   ______ ____ ____ __  ____  __")
print("           / __|\ \ / /| _ )|__ (| _ \| \/ |\ \/ /")
print("           | (__ \ V / | _ \ |_ \| / ||\/| | >  <")
print("           \___|  |_|  |___/|___/|_|_\|_||_|/_/\_\___")
print("\u001b[33m")
print('         《"""""""""""""""""""""""""""""""""""""""""""》')
print("         《    CYB3RMX_ PROGRAMMING & CYBERSECURITY   》")
print("         《       ~~~~~MX Security Corporation~~~~~   》")
print("         《               CRYPTO MESSAGE              》")
print('         《___________________________________________》')
print("%%%%%%%%%%%%%%%%%%%%%%%%%")
print("CURRENT CRYPTO ALGORITHMS")
print("[1] MD5")
print("[2] SHA256")
print("[3] SHA512")
print("%%%%%%%%%%%%%%%%%%%%%%%%%")
print("[154] UPDATE CRYPTO MESSAGE")
print("----------")
select = int(input("[*] SELECT AN OPTION: "))
message = str(input("[*] INPUT YOUR STRING MESSAGE: "))
if select == 1:
  print("\033[32m==========================")
  print(hashlib.md5(b"message").hexdigest())
  print("==========================")
  ret = int(input("\u001b[31m[!] RETURN BACK [1/0] ?: "))
  if ret == 1:
    os.system('clear')
    os.system('python crypto.py')
  elif ret == 0:
    print("\u001b[31m[!] PROGRAM IS SHUTTING DOWN...")
    os.system('clear')
  else:
    print("\u001b[31m[!] YOU SELECTED WRONG OPTION!!")
elif select == 2:
  print("\033[32m==========================")
  print(hashlib.sha256(b"message").hexdigest())
  print("==========================")
  ret1 = int(input("\u001b[31m[!] RETURN BACK [1/0] ?: "))
  if ret1 == 1:
    os.system('clear')
    os.system('python crypto.py')
  elif ret1 == 0:
    print("\u001b[31m[!] PROGRAM IS SHUTTING DOWN...")
    os.system('clear')
  else:
    print("\u001b[31m[!] YOU SELECTED WRONG OPTION!!")
elif select == 3:
  print("\033[32m==========================")
  print(hashlib.sha512(b"message").hexdigest())
  print("==========================")
  ret2 = int(input("\u001b[31m[!] RETURN BACK [1/0] ?: "))
  if ret2 == 1:
    os.system('clear')
    os.system('python crypto.py')
  elif ret2 == 0:
    print("\u001b[31m[!] PROGRAM IS SHUTTING DOWN...")
    os.system('clear')
  else:
    print("\u001b[31m[!] YOU SELECTED WRONG OPTION!!")
elif select == 154:
    print("\u001b[32m[*] UPDATING CRYPTO MESSAGE...")
    os.system('clear')
    os.system('git clone https://github.com/CYB3RMX/Crypto-Messages')
    print("\u001b[32m[*] UPDATING COMPLETE.")
    os.system('python crypto.py')
else:
  print("\u001b[31m=============================")
  print("NEW ALGORITHMS COMING SOON...")