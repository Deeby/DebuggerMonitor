
#Fuzzing Debugger Monitor v1.0

Watching target's exception and producing the exception context.


##dependencies:

Windbg
comtypes
psutil
PyDbgEng
pywin32


##Usage
``` python
usages()
{

	dbg = DebuggerMonitor("CrashTest.exe 1.txt", "log")

	dbg.run()
	
	if dbg._faultDetected:

		logdir =  dbg.getLogDir()

		print "Saving Samples in %s"% logdir

	del(dbg)

}
```
