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
phoneTime = {}

for call in calls:
    if call[0] in phoneTime:
        phoneTime[call[0]] += int(call[3])
    else:
        phoneTime[call[0]] = int(call[3])
    if call[1] in phoneTime:
        phoneTime[call[1]] += int(call[3])
    else:
        phoneTime[call[1]] = int(call[3])

longestTimeNumber = calls[0][0]

for number in phoneTime.keys():
    if phoneTime[number] > phoneTime[longestTimeNumber]:
        longestTimeNumber = number

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(longestTimeNumber, phoneTime[longestTimeNumber]))