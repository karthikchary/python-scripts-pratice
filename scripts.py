#!/usr/bin/python
import os
from urllib2 import Request, urlopen, URLError

def web():
    weburl= "https://www.tooplate.com/download/2108_dashboard"
    #weburl = Request(url)
    #weburl="https://www.tooplate.com/download/2092_shelf"
    name_of_dir=weburl.split('/')[4]
    print(name_of_dir)
    os.system("yum install httpd wget unzip -y")
    print("start & enable service")
    os.system("systemctl start httpd ")
    os.system("systemctl enable httpd ")
    os.system(("wget -O website.zip %s") % weburl)
    os.system("unzip website.zip")
    os.system(("cp -r %s/* /var/www/html/") % name_of_dir)
    os.system("systemctl restart httpd")

    print("website setup done")

web()

