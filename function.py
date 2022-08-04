#!/usr/bin/python
import os

userlist = ["alpha","beta","gamma"]
for user in userlist:
    os.system(("useradd %s") % user)

os.system("groupadd science")

for user in userlist:
    os.system(("usermod -G science %s") % user)