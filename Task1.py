"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
import csv

def dubli_list(input):
    """Remove duplicates from the given list"""
    return list(set(input))
numbers = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    for text in list(reader):
            numbers.extend(text[:2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    for call in list(reader):
        numbers.extend(call[:2])
