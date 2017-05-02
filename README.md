
# Fuzzing Debugger Monitor v2.0

`dbg` `fuzzing`

**DebugMonitor** is an agent which monitors the  target process when it crashes, 
and generates exploitable info.


## Dependencies

- Windbg
- comtypes(Python2.7)
- psutil(Python2.7)
- PyDbgEng(Python2.7)
- pywin32(Python2.7)



## Usage

- run.py `sample_dir` `target_path` `timeout`

- **samp_dir:** testcase directory
- **target_path:** target process's fullname 
- **timeout:** time to kill the process, 0 means cpukill.


## CHANGELOG

- 2017.4.28 Add CPUKill that automatically kill target process
- 2017.5.2  Add "!exchain" dbgcontrol command ouput
