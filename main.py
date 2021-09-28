# Schedule Tool
# File name: main.py
# Date last modified: 08/03/2021
# Description: Run the mergeStudentsResults and processResults file in that specific order.

from src import mergeStudents
from src.results import processResults

mergeStudents.main()
processResults.main()
