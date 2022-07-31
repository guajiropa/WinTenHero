#
# NAME      : main.py <<WinTenHero>>
# AUTHOR    : Robert James Patterson
# DATE      : 07/31/2022
# SYNOPSIS  : Build a Python program that runs AutoHotkey and Powershell to automate tasks for the end-user
#               from a simple GUI interface. 
# 

import sys


if __name__ == "__main__":
    app = Application(sys.argv)
    winHero = Win10HeroForm()
    winHero.show()
    sys.exit(app.exec_())