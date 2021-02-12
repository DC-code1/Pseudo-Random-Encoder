import textwrap
import random
random.seed(202090)
table1 = []
for i in range(26):
    table1.append(i)

letters = 'abcdefghijklmnopqrstuvwxyz'
letter_list = list(letters)
dict1 = dict(zip(table1,letter_list))

num = []
for i in range(26):
    num.append(i)
#print(num)
rannum = random.shuffle(table1)

key_list = list(dict1.keys())
val_list = list(dict1.values())

l = []
for i in range(len(letters)):
    nummsg = table1[i]
    x = val_list[nummsg].upper()
    l.append(x)
    #print(x,end=' ')
#print(l)
    
mydict = dict(zip(letters,l))
#print(mydict)
#msg = 'Hello World! Welcome to ITC106, Session 1 of 2021. All the best :)'
#msg = "ITC106: Programming Principles"
msg = ''
with open('Untitled_asn2.txt','r') as x:
    lines = x.readline()
    for lines in x:
        #lines = lines.rstrip() # Not needed as items are in different lines.
        msg += lines
        
    #print(lines)
print('Original content.')
wrappedlines = textwrap.wrap(msg,width = 100)
for lines in wrappedlines:
    print(lines)
    
#print(msg)
print()
print('Encoded message.')

encoded = ''
for letter in msg.lower():
    if letter in mydict:
        encoded += mydict[letter]
    else:
        encoded += letter
wrappedlines = textwrap.wrap(encoded,width = 100)
for lines in wrappedlines:
    print(lines)

print()
print(mydict)
