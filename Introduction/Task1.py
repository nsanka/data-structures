"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
records = set()
for line in texts:
    records.add(line[0])
    records.add(line[1])

for line in calls:
    records.add(line[0])
    records.add(line[1])

print(f"There are {len(records)} different telephone numbers in the records.")