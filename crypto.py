#!/usr/bin/env python
#-*- coding: utf-8 -*-
import hashlib
print("\u001b[36mCRYPTO PROGRAM by CYB3RMX_")
print("\u001b[37m==========================")
print("CURRENT CRYPTO ALGORITHMS")
print("[1] MD5")
print("[2] SHA256")
print("[3] SHA512")
select = int(input("SELECT ALGORITHM: "))
message = str(input("INPUT YOUR STRING MESSAGE: "))
if select == 1:
  print("\033[32m==========================")
  print(hashlib.md5(b"message").hexdigest())
  print("==========================")
elif select == 2:
  print("\033[32m==========================")
  print(hashlib.sha256(b"message").hexdigest())
  print("==========================")
elif select == 3:
  print("\033[32m==========================")
  print(hashlib.sha512(b"message").hexdigest())
  print("==========================")
else:
  print("\u001b[31m=========================")
  print("NEW ALGORITHMS COMING SOON...")
