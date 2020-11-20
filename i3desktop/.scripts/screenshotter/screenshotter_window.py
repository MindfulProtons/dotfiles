#!/bin/python

from datetime import datetime
import os
import subprocess

#Get time/date specifications
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
hour = datetime.now().hour
minute = datetime.now().minute
second = datetime.now().second
#month-day-year_hour:minute:second
#EXAMPLE
#12-27-16_11:25:50
filename = "%s-%s-%s_%s:%s:%s.png" % (month, day, year, hour, minute, second)

os.system("shotgun -i $(hacksaw -f %%i) %s" % filename)
os.system("mv '%s' ~/.screenshots/" % filename)
link = str(subprocess.check_output(["~/.scripts/screenshotter/imgur.sh  ~/.screenshots/%s " % filename], shell=True))
os.system('echo -n "%s" | xclip -selection clipboard' % link[2:-3])
os.system('notify-send "Link copied to clipboard."')
