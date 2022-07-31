#
# NAME      : sguione.py 
# AUTHOR    : Robert James Patterson
# DATE      : 07/31/2022
# SYNOPSIS  : Testing PySimpleGUI, first test
# 

import PySimpleGUI as sg

# Define window's ccontents.
layout = [  [sg.Text("What is your name?:")],
            [sg.Input()],
            [sg.Button('Ok')]   ] 

# Create the window.
winSG = sg.Window('Test one of PySimpleGUI', layout)

# Display and interact with the window.
event, vals = winSG.read()

# Do something with the information that has been gathered.
print('Greetings', vals[0], ", and thanks for trying PySimpleGUI!")

# Finish up and destroy the window.
winSG.close()