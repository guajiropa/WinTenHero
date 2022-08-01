#
# NAME      : sguitwo.py 
# AUTHOR    : Robert James Patterson
# DATE      : 07/31/2022
# SYNOPSIS  : Testing PySimpleGUI, second test
# 

import PySimpleGUI as sg

sg.theme('DarkTanBlue')

# Define window's ccontents.
layout = [  [sg.Text("What is your name?:")],
            [sg.Input(key='-NAME-')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('Quit')]   ] 

# Create the window.
winSG = sg.Window('Test two of PySimpleGUI', layout, no_titlebar=False, alpha_channel= 0.8)

# Display and interact with the window using an 'Event Loop'
while True:
    event, values = winSG.read()
    # Check to see if the user trys to exit the program.
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Write output message to the window.
    winSG['-OUTPUT-'].update('Greetings ' + values['-NAME-'] + "! Thanks for trying PySimpleGUI")

# Finish up and destroy the window.
winSG.close()