#!/usr/bin/python3
import os
from pprint import pprint
def useradd():
    userlist = ["alpha","beta","gamma"]
    for user in userlist:
        exitcode = os.system(("id %s") % user)
        if exitcode == 0:
            print("User already exists")
        else:
            os.system(("useradd %s") % user)

    exitcode = os.system("grep science /etc/group")
    if exitcode != 0:
        os.system("groupadd science")
    else:
        print("Group already exists")

    for user in userlist:
        os.system(("usermod -G science %s") % user)

def directory():
    if os.path.isdir("/opt/science_directory"):
        print("Directory already exists")
    else:
        os.mkdir("/opt/science_directory")
    print("#####################################")
    print("Assiging permissions")
    os.system("chown :science /opt/science_directory")
    os.system("chmod 770 /opt/science_directory")

useradd()
directory()