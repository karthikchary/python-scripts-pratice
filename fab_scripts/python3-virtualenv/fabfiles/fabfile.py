import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
from fabric.api import *

def msg():
    print("Good Morning.")

def disk_space():
    local("df -h")
