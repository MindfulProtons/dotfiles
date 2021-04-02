#!/usr/bin/env python

''' Script created by Sollybird, edited by MindfulProtons to work with Wayland.
This script requires grim, wl-clipboard, and I recommend sway for compositor.
This also uses imgur.sh to upload to imgur automatically. '''

from datetime import datetime
import os
import subprocess

# Get time/date specifications
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
hour = datetime.now().hour
minute = datetime.now().minute
second = datetime.now().second
# month-day-year_hour:minute:second
# EXAMPLE
# 12-27-16_11:25:50
filename = "%s-%s-%s_%s:%s:%s.png" % (month, day, year, hour, minute, second)

os.system("grim -g \"$(slurp)\" %s && mv %s ~/.screenshots" % (filename, filename))
link = str(subprocess.check_output(["~/.scripts/screenshotter/imgur.sh  ~/.screenshots/%s " % filename], shell=True))
os.system('echo -n "%s" | wl-copy' % link[2:-3])
os.system('notify-send "Link copied to clipboard."')
