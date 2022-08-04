import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
from fabric.api import *

def greet(msg):
    print(("Good %s.")% msg)

def system_info():
    print("Disk Space")
    local("df -h")
    print("Ram Size")
    local("free -m")
