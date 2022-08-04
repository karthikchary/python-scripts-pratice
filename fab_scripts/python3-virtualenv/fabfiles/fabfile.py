import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
from fabric.api import *

def greet(msg):
    print(("Good %s.")% msg)

def disk_space():
    local("df -h")
