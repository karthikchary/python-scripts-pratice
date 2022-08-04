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
    local("yum install httpd wget unzip -y")
    print("start & enable service")
    local("systemctl start httpd")
    local("systemctl enable httpd")
    local(("wget -O website.zip %s") % WEBURL)
    local("unzip website.zip")
    with lcd(DIRNAME):
      local("zip -r tooplate.zip *")
      put("tooplate.zip","/var/www/html", use_sudo=True)
    sudo("")
    # sudo(("cp -r %s/* /var/www/html") % DIRNAME)
    sudo("systemctl restart httpd")
    print("Website setup done")
