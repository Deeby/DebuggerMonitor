
Fuzzing Debugger Monitor v1.0

Watching target's exception and producing the exception context.


dependencies:

Windbg
comtypes
psutil
PyDbgEng
pywin32



usages()
{

	dbg = DebuggerMonitor("CrashTest.exe 1.txt", "log")

	dbg.run()

	logdir =  dbg.getLogDir()

	print "Saving Samples in %s"% logdir

	del(dbg)

}

