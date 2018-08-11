#!/usr/bin/env python3

import datetime
import getpass

now = datetime.datetime.now()

user=getpass.getuser()
write="This system was accessed by the "+user+" at " + str(now.hour)+ ":"+str(now.minute)+":"+str(now.second)

f=open("f1.txt","a")
f.write(write)
f.close()
