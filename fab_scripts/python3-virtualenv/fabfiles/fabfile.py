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

def web_setup(WEBURL, DIRNAME):
    sudo("yum install httpd wget unzip -y")
    print("start & enable service")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    sudo(("wget -O website.zip %s") % WEBURL)
    sudo("unzip website.zip")
    sudo(("cp -r %s/* /var/www/html") % DIRNAME)
    sudo("systemctl restart httpd")
    print("Website setup done")
