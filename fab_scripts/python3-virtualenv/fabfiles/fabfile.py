from fabric.api import *

def msg():
    print "Good Morning"

def disk_space():
    local("df -h")