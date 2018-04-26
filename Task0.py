import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# The first text details
texts_first = texts[0]
# The last call details
calls_last = calls[-1]

print("First record of texts, {} texts {} at time {}".format(
    texts_first[0], texts_first[1], texts_first[2]))

print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    calls_last[0], calls_last[1], calls_last[2], calls_last[3]))
