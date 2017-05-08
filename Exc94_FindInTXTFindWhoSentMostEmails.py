##9.4 Write a program to read through the mbox-short.txt and
##figure out who has the sent the greatest number of mail messages.
##The program looks for 'From ' lines and takes the second word of those lines
##as the person who sent the mail.
##The program creates a Python dictionary that maps the sender's mail address
##to a count of the number of times they appear in the file.
##After the dictionary is produced, the program reads through the dictionary using
##a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        if words[1] not in d:
            d[words[1]] = 1
        else:
            d[words[1]] += 1
                
#print (d)

# find max

dMaxKey = 0
dMaxVal = 0

for key,val in d.items():
    if int(val) > dMaxVal:
        dMaxVal = int(val)
        dMaxKey = key
  #  print (key,val)
    
print (dMaxKey, dMaxVal)
