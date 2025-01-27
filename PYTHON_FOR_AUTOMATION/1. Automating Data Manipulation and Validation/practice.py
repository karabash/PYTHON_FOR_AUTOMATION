import subprocess
def times_repeater(python_verion, pytonfile, amount):
     for i in range(amount):
      print( "page has oppened")
      subprocess.check_call([python_verion, pytonfile])
 
times_repeater("Python3", "example.py", 2)



