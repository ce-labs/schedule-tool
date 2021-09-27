# Schedule Tool
# File name: RUN-Scripts.py
# Date last modified: 08/03/2021
# Description: Run the mergeStudentsResults and processResults file in that specific order.

import os
from subprocess import call

actualPath = os.path.dirname(__file__)  # Get current file path

call("..\mergeStudentsResults.py", shell=True)
call(".\processResults.py", shell=True)
