from cmd import Cmd
from App.Generic import ClearScreen

## WORK IN PROGRESS, IM TRYING THIS THING OUT

class Settings(Cmd):
   def do_exit(self, inp):
        print("Bye")
        return True

   def do_add(self, inp):
        print(f"Adding '{inp}'")

# ClearScreen()
Settings().cmdloop()
print("after")
