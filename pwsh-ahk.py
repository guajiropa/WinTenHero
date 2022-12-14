#
# NAME      : pwsh-ahk.py
# AUTHOR    : Robert James Patterson
# DATE      : 07/14/2022
# SYNOPSIS  : Setup the Powershell environment to allow .ps1 scripts to be executed.
# <<change>>

from ahk import AHK
from ahk.directives import NoTrayIcon


def SetExecutionPolicy(ahk_obj):
    ps_run = 'Run powershell.exe'
    ahk_obj.run_script(ps_run, blocking=False)
    ahk_obj.find_window_by_title(b'Administrator: Windows PowerShell')
    ahk_obj.send("Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser{Enter}")
    ahk.send("Y{Enter}")
    ahk_obj.send("Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine{Enter}")
    ahk_obj.send("Y{Enter}")
    ahk_obj.send("Exit{Enter}")

    return 0

ahk = AHK(directives=[NoTrayIcon])

PolSet = SetExecutionPolicy(ahk)


