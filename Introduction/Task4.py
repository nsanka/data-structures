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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Add all number that make outgoing calls
telemarketers = set()
out_nums = set()
for call in calls:
    telemarketers.add(call[0])
    out_nums.add(call[1])

# Remove all number that receive calls
telemarketers.difference_update(out_nums)

# Remove all numbers which send texts and receive texts
for text in texts:
    telemarketers.discard(text[0])
    telemarketers.discard(text[1])

print("These numbers could be telemarketers: ")
for code in sorted(telemarketers):
    print(code)