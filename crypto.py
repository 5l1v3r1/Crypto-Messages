#!/usr/bin/env python
#-*- coding: utf-8 -*-
import hashlib
print("CRYPTO PROGRAM by CYB3RMX_")
print("==========================")
print("CURRENT CRYPTO ALGORITHMS")
print("[1] MD5")
print("[2] SHA256")
print("[3] SHA512")
select = int(input("SELECT ALGORITHM: "))
message = str(input("INPUT YOUR STRING MESSAGE: "))
if select == 1:
  print("==========================")
  print(hashlib.md5(b"message").hexdigest())
  print("==========================")
elif select == 2:
  print("==========================")
  print(hashlib.sha256(b"message").hexdigest())
  print("==========================")
elif select == 3:
  print("==========================")
  print(hashlib.sha512(b"message").hexdigest())
  print("==========================")
else:
  print("NEW ALGORITHMS COMING SOON...")