"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from collections import defaultdict
records = defaultdict(int)
for call in calls:
    records[call[0]] += int(call[3])
    records[call[1]] += int(call[3])

max_num = max(records, key=records.get)
total_time = records[max_num]
print(f"{max_num} spent the longest time, {total_time} seconds, on the phone during September 2016.")