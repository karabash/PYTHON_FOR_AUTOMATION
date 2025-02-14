'''Using the Python subprocess module is like giving commands to your 
computer using Python instead of typing them directly into the command prompt.
This module makes it easy to automate tasks and integrate other programs with your Python code.'''
import subprocess

def write_times(amount):
    for i in range(amount):
     subprocess.check_call(["python3", "example.py"])

def open_Cmd():
   subprocess.run(['cmd', "python3 practice.py"])

write_times(5)
