
# from modules_learning import examination
# To use the user defined module, first we have to import the pre-defined modules such as OS, SYS.

import os, sys

# To import the user-defined module, we have to provide the directory name, join it with the path and provong all connections into the abspath.

from os.path import dirname, join, abspath

# sys.path.insert(index, object)

sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from examination import exam1


def practice_details():
    print("This function will show the tasks to be practiced.")
    # examination.examination_details()

exam1.examination_details