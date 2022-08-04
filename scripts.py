#!/usr/bin/python
import os
def web():
    #weburl="https://www.tooplate.com/download/2108_dashboard"
    weburl="https://www.tooplate.com/download/2092_shelf"
    directory=weburl.split('/')[4]
    os.system("yum install httpd wget unzip -y")
    print("start & enable service")
    os.system("systemctl start httpd ")
    os.system("systemctl enable httpd ")
    os.system(("wget -O website.zip %s") % weburl)
    os.system("unzip website.zip")
    os.system("cp -r %s/* /var/www/html/") % directory
    os.system("systemctl restart httpd")

    print("website setup done")

web()

