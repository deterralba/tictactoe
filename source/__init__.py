# this file is executed when a module from source is called outside from the source folder,
# for example when the doc is compiled

import os
import sys

# the folder path is added to the python path
sys.path.insert(0, os.path.dirname(__file__))

print("*** source/__init__.py is executed, source/ was added to the python path")
