
#Fuzzing Debugger Monitor v2.0
@(dbg|fuzzing)

**DebugMonitor** is an agent which monitors the  target process when it crashes, 
and generates exploitable info.


##dependencies:

- Windbg
- comtypes(Python2.7)
- psutil(Python2.7)
- PyDbgEng(Python2.7)
- pywin32(Python2.7)



##Usage

- run.py <sample dir> <target path> <timeout>

- **samp dir:** testcase directory
- **target path:** target process's fullname 
- **timeout:** time to kill the process, 0 means cpukill.
