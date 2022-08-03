import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():       #converting all letters to uppercase - then upper and lower don't count seperately
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)