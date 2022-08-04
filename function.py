#!/usr/bin/python3
import os
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
    os.mkdir("/opt/science_directory")
    os.system("chown :science /opt/science_directory")
    os.system("chmod 770 /opt/science_directory")

useradd()
directory()