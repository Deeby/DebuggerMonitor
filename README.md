
#Fuzzing Debugger Monitor v2.0
@(dbg|fuzzing)

**DebugMonitor** is an agent which monitor the  target process when it crashes, and generates exploitable info.


##dependencies:

- Windbg
- comtypes
- psutil
- PyDbgEng
- pywin32



##Usage

- run.py <sample dir> <target path> <timeout>

- samp dir: testcase directory
- target path: target process's fullname 
- timeout: time to kill the process, 0 means cpukill.
