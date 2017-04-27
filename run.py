import os
import sys
import shutil
from debugger import *

def useage():
    print "run.py <sample dir> <target path> <timeout>"
    exit(1)

#usage run.py C:/seeds notepad.exe  4
if __name__ == "__main__":
    print sys.argv
    if len(sys.argv) < 4 :
        print useage()
    dir = sys.argv[1]
    proc = sys.argv[2]
    to = sys.argv[3]
    for file in os.listdir(dir):
        path = os.path.join(dir,file)
        dbg = DebuggerMonitor(proc+" "+path, "logs")
        time = int(to)
        if time == 0:
            dbg.setCpuKill(True)
        else:
            dbg.setTimeOut(time)
        dbg.run()
        if dbg._faultDetected:
            logdir =  dbg.get_log_dir()
            shutil.copy(path, os.path.join(logdir,file))


